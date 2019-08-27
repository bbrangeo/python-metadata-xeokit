# coding: utf8
import json

import ifcopenshell as ifcopenshell


class MetaModel(object):
    def __init__(self, id, project_id, type, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.project_id = project_id
        self.type = type
        # self.meta_objects = []

    @property
    def __repr__(self):
        return repr(
            {'id': self.id, 'project_id': self.project_id, 'type': self.type})


class MetaObject(object):
    def __init__(self, id, name, type, parent, **kwargs):
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.type = type
        self.parent = parent
        # self.meta_objects = []

    @property
    def __repr__(self):
        return repr({'id': self.id, 'name': self.name, 'type': self.type, 'parent': self.parent})


class IfcParse(object):
    """
    classdocs
    """

    def __init__(self, ifc_input_):
        """
        Constructor
        """

        self.ifc_input = ifc_input_
        self.ifcfile = ifcopenshell.open(self.ifc_input)
        self.project = self.ifcfile.by_type("IfcProject")[0]
        self.metaModel = MetaModel(id=self.project.Name, project_id=self.project.GlobalId, type=self.project.is_a())

    def extract_hierarchy(self, object_definition):

        metaObjectsList = []
        parentObject = MetaObject(id=object_definition.GlobalId, name=object_definition.Name,
                                  type=object_definition.is_a(), parent=None)

        # if str(object_definition.is_a()) != "IfcProject":
        metaObjectsList.append(parentObject.__dict__)

        if object_definition.is_a("IfcSpatialStructureElement"):
            for cE in object_definition.ContainsElements:
                for rE in cE.RelatedElements:
                    mo = MetaObject(id=rE.GlobalId, name=rE.Name,
                                    type=rE.is_a(), parent=object_definition.GlobalId)
                    metaObjectsList.append(mo.__dict__)

        for iD in object_definition.IsDecomposedBy:
            for rO in iD.RelatedObjects:
                childrens = self.extract_hierarchy(rO)
                metaObjectsList.append(childrens)
                # pprint(item.get_info(recursive=True))

        return metaObjectsList

    def to_json(self, json_output_):
        metaObjects = self.extract_hierarchy(self.project)
        self.metaModel.meta_objects = metaObjects
        f = open(json_output_, 'w')
        json_data = json.dumps(self.metaModel.__dict__, default=lambda o: o.__dict__, indent=4)
        f.write(json_data)
        return self.metaModel


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Process')
    parser.add_argument('--ifc_input', metavar='ifc', help='ifc_input')
    parser.add_argument('--json_output', metavar='json', help='json_filename', default='metaModel.json')

    args = parser.parse_args()
    ifc_input = args.ifc_input
    json_output = args.json_output

    projet = IfcParse(ifc_input)
    projet.to_json(json_output)
