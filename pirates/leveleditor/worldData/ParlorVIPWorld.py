# Embedded file name: pirates.leveleditor.worldData.ParlorVIPWorld
from pandac.PandaModules import Point3, VBase3
objectStruct = {
    'Objects': {
        '1161659527.38Shochet': {
            'Type': 'Region',
            'Name': 'ParlorVIPWorld',
            'Objects': {
                '1161660338.41Shochet': {
                    'Type': 'Island',
                    'File': 'ParlorVIPIsland',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Objects': {
                        '1161660371.52Shochet': {
                            'Type': 'LOD Sphere',
                            'Hpr': Point3(0.0, 0.0, 0.0),
                            'Pos': Point3(-0.0, 0.0, 10.194),
                            'Radi': [159, 1159, 2159],
                            'Scale': VBase3(1.0, 1.0, 1.0)
                        }
                    },
                    'Pos': Point3(34.974, 6.715, -13.161),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/islands/wild_island_a_zero'
                    }
                }
            },
            'Visual': {}
        }
    },
    'Layers': {},
    'ObjectIds': {
        '1161659527.38Shochet':
        '["Objects"]["1161659527.38Shochet"]',
        '1161660338.41Shochet':
        '["Objects"]["1161659527.38Shochet"]["Objects"]["1161660338.41Shochet"]',
        '1161660371.52Shochet':
        '["Objects"]["1161659527.38Shochet"]["Objects"]["1161660338.41Shochet"]["Objects"]["1161660371.52Shochet"]'
    }
}
