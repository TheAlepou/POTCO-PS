# Embedded file name: pirates.leveleditor.worldData.CaveAWorld
from pandac.PandaModules import Point3, VBase3
objectStruct = {
    'Objects': {
        '1172099793.11sdnaik': {
            'Type': 'Region',
            'Name': 'default',
            'Objects': {
                '1172100047.36sdnaik': {
                    'Type': 'Island',
                    'File': 'CaveAIsland',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Objects': {
                        '1173476857.61sdnaik': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-16.196, -200.091, -16.353),
                            'Radi': [2658, 3658, 4658],
                            'Scale': VBase3(1.0, 1.0, 1.0)
                        }
                    },
                    'Pos': Point3(-140.641, 184.738, 0.0),
                    'Visual': {
                        'Model': 'models/islands/wild_island_b_zero'
                    }
                }
            },
            'Visual': {}
        }
    },
    'Layers': {},
    'ObjectIds': {
        '1172099793.11sdnaik':
        '["Objects"]["1172099793.11sdnaik"]',
        '1172100047.36sdnaik':
        '["Objects"]["1172099793.11sdnaik"]["Objects"]["1172100047.36sdnaik"]',
        '1173476857.61sdnaik':
        '["Objects"]["1172099793.11sdnaik"]["Objects"]["1172100047.36sdnaik"]["Objects"]["1173476857.61sdnaik"]'
    }
}
