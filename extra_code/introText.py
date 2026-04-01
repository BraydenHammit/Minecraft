def intro(bt):
    #Starting Text:
    intro = '''How to Play:
You must start by mining a stone or netherrack block. You can only mine blocks next to blocks you've already mined. You lose score for mining stone, deepslate, and netherrack. Your score is shown on the bottom left bedrock, and you can go to the next round by clicking 'Next' (next to score). You only have 15 seconds each round (shown next to the 'Next' button), and when that runs out the round automaticlly ends. In between rounds, you can buy upgrades by spending your score.
\nUpgrade examples:
Boost ore spawns, the amount of score you get per ore, gain the ability to select what dimension it will be next round (the button is in the shop), increase your mining to a 3x3 area with an explosive blast, apply a fortune enchantment, gain the ability to start mining on things other than stone or netherrack, remove the score penalties when mining netherrack, stone, endstone, and deepslate, unlock the ability to mine diagonally (between blocks) from pre-mined blocks, unlock three extra ores (one Overwold, two Nether) or an extra dimension, and much more.
\nRock Values:\nStone, Endstone, & Netherrack = -1\nDeepslate = -1.5\nBedrock = -25\n\nOre Values:\nCoal, Copper, & Nether Gold = 1.75\nRedstone & Lapis = 2.5\nIron, Gold, & Quartz = 3.25\nDiamond = 8\nEmerald & Netherite = 12.5
\nExtra Semi-Ores:\nGlowstone = 8\nGilded Blackstone & Amethyst = 7.5'''

    #Block Types (Soft-Coded):
    intro += '\n\nBlock Types:'
    for key, value in bt.items():
        if key != 'potato':
            if key == 'gemD':
                intro += f'\nDull Gems:'
            else:
                intro += f'\n{key.title()}:'
            num = 0
            for val in value:
                if ('potone' not in val) and ('potato' not in val) and (val not in ('resin','ruby','cheese')):
                    num += 1
                    if num == 1:
                        intro += f' {val.title()}'
                    else:
                        intro += f', {val.title()}'
            intro += '\n--------------------------------------------------------------------------------'

    return intro