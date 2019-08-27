# A python program tool for extracting the structural hierarchy of the building elements within an IFC into the metadata format of the xeokit-sdk.

![](https://www.plateforme-tipee.com/wp-content/themes/tipee/img/logo.png)


## Usage

```
$ python main.py --ifc_input MAISON_EP_0.ifc --json_output metaModel.json
```

## JSON

Example:

```json
{
  "id": "0001",
  "project_id": "0m7dsGszf588Nx0jOsYoXj",
  "type": "IfcProject",
  "meta_objects": [
    {
      "id": "0KsWlSZqr1J8RaEJrb86Du",
      "name": "Mur de base:Générique - Ext. 200 mm:250674",
      "type": "IfcWallStandardCase",
      "parent": "0m7dsGszf588Nx0jR9TDNz"
    },
    {
      "id": "0KsWlSZqr1J8RaEJrb86Fd",
      "name": "Mur de base:Générique - Ext. 200 mm:250797",
      "type": "IfcWallStandardCase",
      "parent": "0m7dsGszf588Nx0jR9TDNz"
    },
    {
      "id": "0KsWlSZqr1J8RaEJrb86HC",
      "name": "Mur de base:Générique - Ext. 200 mm:250886",
      "type": "IfcWallStandardCase",
      "parent": "0m7dsGszf588Nx0jR9TDNz"
    },
    {
      "id": "0KsWlSZqr1J8RaEJrb86GL",
      "name": "Mur de base:Générique - Ext. 200 mm:250975",
      "type": "IfcWallStandardCase",
      "parent": "0m7dsGszf588Nx0jR9TDNz"
    },
    {
      "id": "0KsWlSZqr1J8RaEJrb86IN",
      "name": "Mur de base:Int. Brique 40 mm:251101",
      "type": "IfcWallStandardCase",
      "parent": "0m7dsGszf588Nx0jR9TDNz"
    },
    {
      "id": "0KsWlSZqr1J8RaEJrb86Kv",
      "name": "Mur de base:Int. Brique 40 mm:251251",
      "type": "IfcWallStandardCase",
      "parent": "0m7dsGszf588Nx0jR9TDNz"
    },
    {
      "id": "0KsWlSZqr1J8RaEJrb86Nb",
      "name": "Sol:Dalle en béton - 250 mm:251311",
      "type": "IfcSlab",
      "parent": "0m7dsGszf588Nx0jR9TDNz"
    }
  ]
 }
```

## Credits

Created by [Tipee][0] for the [xeokit-sdk][1] using the [IfcOpenShell][2] libraries.

[0]: http://plateforme-tipee.com
[1]: https://github.com/xeokit/xeokit-sdk
[2]: https://github.com/IfcOpenShell/IfcOpenShell