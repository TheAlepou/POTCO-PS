# Embedded file name: pirates.leveleditor.worldData.del_fuego_building_int_tavern_1
from pandac.PandaModules import Point3, VBase3, Vec4
objectStruct = {
    'Objects': {
        '1153435103.16dzlu0': {
            'Type': 'Building Interior',
            'Name': '',
            'AdditionalData': ['interior_tavern_b'],
            'Instanced': True,
            'Objects': {
                '1175733248.0dxschafe': {
                    'Type': 'Townsperson',
                    'Category': 'Commoner',
                    'Aggro Radius': '12.0000',
                    'AnimSet': 'idleC',
                    'CustomModel': 'None',
                    'DNA': '1175733248.0dxschafe',
                    'Hpr': VBase3(-40.38, 0.0, 0.0),
                    'Patrol Radius': '12.0000',
                    'Pos': Point3(-44.291, -9.565, 1.0),
                    'Respawns': True,
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Start State': 'Idle',
                    'Team': 'Villager'
                },
                '1175733376.0dxschafe': {
                    'Type': 'Townsperson',
                    'Category': 'Bartender',
                    'Aggro Radius': '12.0000',
                    'AnimSet': 'idleB',
                    'CustomModel': 'None',
                    'DNA': '1175733376.0dxschafe',
                    'Hpr': VBase3(-75.11, 0.0, 0.0),
                    'Patrol Radius': '12.0000',
                    'Pos': Point3(-49.368, 3.21, 1.0),
                    'Private Status': 'All',
                    'Respawns': True,
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Start State': 'Idle',
                    'Team': 'Villager'
                },
                '1190745843.48dxschafe': {
                    'Type': 'Parlor Game',
                    'Category': 'Blackjack',
                    'BetMultiplier': '10',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-6.074, 0.012, 1.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Model': 'models/props/table_bar_round_parlor'
                    }
                },
                '1190745899.7dxschafe': {
                    'Type': 'Effect Node',
                    'EffectName': 'torch_effect',
                    'Hpr': Point3(0.0, 0.0, 0.0),
                    'Pos': Point3(-16.194, -15.241, 1.0),
                    'Scale': VBase3(1.0, 1.0, 1.0),
                    'Visual': {
                        'Color': (0, 0, 0.65, 1),
                        'Model': 'models/misc/smiley'
                    }
                }
            },
            'Visual': {
                'Model': 'models/buildings/interior_tavern_b'
            }
        }
    },
    'Node Links': [],
    'Layers': {},
    'ObjectIds': {
        '1153435103.16dzlu0':
        '["Objects"]["1153435103.16dzlu0"]',
        '1175733248.0dxschafe':
        '["Objects"]["1153435103.16dzlu0"]["Objects"]["1175733248.0dxschafe"]',
        '1175733376.0dxschafe':
        '["Objects"]["1153435103.16dzlu0"]["Objects"]["1175733376.0dxschafe"]',
        '1190745843.48dxschafe':
        '["Objects"]["1153435103.16dzlu0"]["Objects"]["1190745843.48dxschafe"]',
        '1190745899.7dxschafe':
        '["Objects"]["1153435103.16dzlu0"]["Objects"]["1190745899.7dxschafe"]'
    }
}
