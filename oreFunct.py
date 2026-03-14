import random as ran

def oreO(upgradeInv):
    if upgradeInv['luck']:
        randomNum = ran.randint(0,50)
    else:
        randomNum = ran.randint(0,75)


    if (randomNum == 32 or randomNum == 31) and upgradeInv['ore ext']:
        ore = 'amethyst'
    elif randomNum <= 30:
        ore = 'copper'
        if randomNum <= 23:
            ore = 'coal'
            if randomNum <= 17:
                ore = 'redstone'
                if randomNum <= 13:
                    ore = 'lapis'
                    if randomNum <= 9:
                        ore = 'iron'
                        if randomNum <= 4:
                            ore = 'gold'
                            if randomNum <= 1:
                                ore = 'diamond'
                                if randomNum == 0:
                                    ore = 'emerald'
    else:
        ore = 'none'

    return ore



def oreN(upgradeInv):
    if upgradeInv['luck']:
                    randomNum = ran.randint(0,40)
    else:
                    randomNum = ran.randint(0,65)

    if (randomNum == 27 or randomNum == 26) and upgradeInv['ore ext']:
            ore = 'gilded blackstone'
    elif randomNum <= 25:
        ore = 'nether gold'
        if randomNum <= 10:
            ore = 'quartz'
            if randomNum == 0:
                ore = 'netherite'
    else:
        ore = 'none'

    return ore