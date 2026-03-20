import random as ran
import tkinter as tk

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Score Function:
def scoreAS(block,upgradeInv,multiplier,score):
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
            score = 100 * multiplier
        elif not upgradeInv['penalty b']:
            score = -100
    elif (block == 'coal') or (block == 'nether gold') or (block == 'copper'):
        score = 1.75 * multiplier
    elif (block == 'redstone') or (block == 'lapis'):
        score = 2.5 * multiplier
    elif (block == 'iron') or (block == 'gold') or (block == 'quartz'):
        score = 3.25 * multiplier
    elif (block == 'diamond') or (block == 'glowstone'):
        score = 5 * multiplier
    elif (block == 'amethyst') or (block == 'gilded blackstone'):
        score = 7.5 * multiplier
    elif (block == 'emerald') or (block == 'netherite') or (block == 'resin'):
        score = 12.5 * multiplier
    elif (block == 'poisonous potato'):
        score = 537.25 * multiplier

    #Fortune:
    if upgradeInv['fortune'][0] and score > 0:
        if ((upgradeInv['fortune'][1] == 100) 
        or (upgradeInv['fortune'][1] == 75 and (ran.randint(1,4) != 1))
        or (upgradeInv['fortune'][1] == 50 and (ran.randint(1,2) == 1))
        or (upgradeInv['fortune'][1] == 25 and (ran.randint(1,4) == 1))):
            if upgradeInv['fortune x3']:
                score = score * 3
            else:
                score = score * 2
        
    #-------------------------------    

    return score

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Hidden Ore Scores:
def HOS():
    hos = tk.Tk()
    hos.title("Hidden Ore Values:")
    hos.geometry('500x60')

    text = tk.Label(hos, text='Potone = -1\nResin = 12.5\nPoisonous Potato = 537.25')
    text.pack(pady=5,padx=5)