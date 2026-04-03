import random as ran
import tkinter as tk

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Score Function:
def scoreAS(block,upgradeInv,multiplier,score,blockT,blockTypes):
    score = 0

    #Base:
    if (block == 'stone'):
        if upgradeInv['penalty s+']:
            score = multiplier
        elif not upgradeInv['penalty s']:  
            score = -1
    elif (block == 'netherrack'):
        if upgradeInv['penalty n+']:
            score = multiplier
        elif not upgradeInv['penalty n']:
            score = -1
    elif (block == 'endstone'):
        if upgradeInv['penalty e+']:
            score = multiplier
        elif not upgradeInv['penalty e']:
            score = -1
    if (block == 'potone'):
        if upgradeInv['penalty p+']:
            score = multiplier
        elif not upgradeInv['penalty p']:  
            score = -1
    elif (block == 'deepslate'):
        if upgradeInv['penalty d+']:
            score = 1.5 * multiplier
        elif not upgradeInv['penalty d']:
            score = -1.5
    elif (block == 'bedrock'):
        if upgradeInv['penalty b+']:
            score = 25 * multiplier
        elif not upgradeInv['penalty b']:
            score = -25
    elif (block == 'coal') or (block == 'nether gold') or (block == 'copper'):
        score = 1.75 * multiplier
    elif (block == 'redstone') or (block == 'lapis'):
        score = 2.5 * multiplier
    elif (block == 'iron') or (block == 'gold') or (block == 'quartz'):
        score = 3.25 * multiplier
    elif (block == 'diamond') or (block == 'glowstone'):
        score = 8 * multiplier
    elif (block == 'amethyst') or (block == 'gilded blackstone'):
        score = 7.5 * multiplier
    elif (block == 'emerald') or (block == 'netherite') or (block == 'resin'):
        score = 12.5 * multiplier
    elif (block == 'poisonous potato'):
        score = 537.25 * multiplier
    elif (block == 'ruby'):
        score = 17.5 * multiplier

    #Multipliers:
    if upgradeInv['fortune'][0] and score > 0:
        #Fortune:
        if ((upgradeInv['fortune'][1] == 100) 
        or (upgradeInv['fortune'][1] == 75 and (ran.randint(1,4) != 1))
        or (upgradeInv['fortune'][1] == 50 and (ran.randint(1,2) == 1))
        or (upgradeInv['fortune'][1] == 25 and (ran.randint(1,4) == 1))):
            if upgradeInv['fortune x3']:
                score = score * 3
            else:
                score = score * 2
        #Bonuses:
        if upgradeInv['gold bonus'] and blockT in blockTypes['golden']:
            score = score * 1.5
        if upgradeInv['gemS bonus'] and blockT in blockTypes['gemS']:
            score = score * 1.5
        if upgradeInv['gemD bonus'] and blockT in blockTypes['gemD']:
            score = score * 1.5
        if upgradeInv['ind bonus'] and blockT in blockTypes['industrial']:
            score = score * 1.5
        if upgradeInv['rock bonus'] and blockT in blockTypes['rock']:
            score = score * 1.5
        if upgradeInv['potato bonus'] and blockT in blockTypes['potato']:
            score = score * 1.5

    elif upgradeInv['rock bonus'] and blockT in blockTypes['rock']:
        score = score / 2
    

        
        
    #-------------------------------    

    return score

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Hidden Ore Scores:
def HOS(upgradeInv,BT):
    hos = tk.Tk()
    hos.title("Hidden Ores:")
    texT='Values:\nPotone = -1\nResin = 12.5'
    if upgradeInv['ruby'][0]:
        texT += '\nRuby = 17.5'
    texT += '\nPoisonous Potato = 537.25'

    texT += '\n\nUpdated Block Types:'
    for key, value in BT.items():
            if key == 'gemD':
                texT += f'\nDull Gems:'
            else:
                texT += f'\n{key.title()}:'
            num = 0
            for val in value:
                if (val != 'ruby') or upgradeInv['ruby'][0]:
                    num += 1
                    if num == 1:
                        texT += f' {val.title()}'
                    else:
                        texT += f', {val.title()}'
            texT += '\n--------------------------------------------------------------------------------'

    text = tk.Label(hos, text=texT)
    text.pack(pady=5,padx=5)
