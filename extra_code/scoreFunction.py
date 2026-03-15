import random as ran

def scoreAS(block,upgradeInv,multiplier,score):
    score = 0

    if (block == 'stone'):
        if upgradeInv['penalty s+']:
            score = 1
        elif not upgradeInv['penalty s']:
            score = -1
    elif (block == 'netherrack'):
        if upgradeInv['penalty n+']:
            score = 1
        elif not upgradeInv['penalty n']:
            score = -1
    elif (block == 'endstone'):
        if upgradeInv['penalty e+']:
            score = 1
        elif not upgradeInv['penalty e']:
            score = -1
    elif (block == 'deepslate'):
        if upgradeInv['penalty d+']:
            score = 1.5
        elif not upgradeInv['penalty d']:
            score = -1.5
    elif (block == 'coal') or (block == 'nether gold') or (block == 'copper'):
        score = 1.75 * multiplier
    elif (block == 'redstone') or (block == 'lapis'):
        score = 2.5 * multiplier
    elif (block == 'iron') or (block == 'gold') or (block == 'quartz'):
        score = 3.25 * multiplier
    elif (block == 'diamond'):
        score = 5 * multiplier
    elif (block == 'amethyst') or (block == 'gilded blackstone'):
        score = 7.5 * multiplier
    elif (block == 'emerald') or (block == 'netherite'):
        score = 12.5 * multiplier

    if upgradeInv['fortune'][0] and score > 0:
        if ((upgradeInv['fortune'][1] == 100) 
        or (upgradeInv['fortune'][1] == 75 and (ran.randint(1,4) != 1))
        or (upgradeInv['fortune'][1] == 50 and (ran.randint(1,2) == 1))
        or (upgradeInv['fortune'][1] == 25 and (ran.randint(1,4) == 1))):
            score = score * 2
        
           

    return score