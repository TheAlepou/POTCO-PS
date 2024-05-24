# Embedded file name: pirates.leveleditor.worldData.SandboxIsland
from pandac.PandaModules import Point3, VBase3, Vec4
objectStruct = {
    'Objects': {
        '1200614077.2joswilso': {
            'Type': 'Island',
            'Name': 'SandboxIsland',
            'Objects': {
                '1200614146.73joswilso': {
                    'Type': 'Player Spawn Node',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Index': 1,
                    'Pos': Point3(-21.084, -112.742, 9.466),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Spawnables': 'All',
                    'Visual': {
                        'Color': (0.5, 0.5, 0.5, 1),
                        'Model': 'models/misc/smiley'
                    }
                },
                '1200614249.98joswilso': {
                    'Type': 'Dinghy',
                    'Aggro Radius': '20.0000',
                    'Hpr': VBase3(-4.891, 0.0, 0.0),
                    'Location': 'Land',
                    'Pos': Point3(6.563, -129.477, 9.649),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/shipparts/dingy-geometry_High'
                    }
                }
            },
            'Visual': {
                'Model': 'models/islands/wild_island_a_zero'
            }
        }
    },
    'Node Links': [],
    'Layers': {},
    'ObjectIds': {
        '1200614077.2joswilso':
        '["Objects"]["1200614077.2joswilso"]',
        '1200614146.73joswilso':
        '["Objects"]["1200614077.2joswilso"]["Objects"]["1200614146.73joswilso"]',
        '1200614249.98joswilso':
        '["Objects"]["1200614077.2joswilso"]["Objects"]["1200614249.98joswilso"]'
    }
}
