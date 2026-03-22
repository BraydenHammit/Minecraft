import random as ran

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Overworld:
def oreO(upgradeInv,r):
    if upgradeInv['luckM']:
        randomNum = ran.randint(0,35)
    elif upgradeInv['luck']:
        randomNum = ran.randint(0,50)
    else:
        randomNum = ran.randint(0,75)

    if randomNum == 0:
        ore = 'emerald'
    elif randomNum <= 1:
        ore = 'diamond'
    elif randomNum <= 4:
        ore = 'gold'
    elif randomNum <= 9:
        ore = 'iron'
    elif randomNum <= 13:
        ore = 'lapis'
    elif randomNum <= 17:
        ore = 'redstone'
    elif randomNum <= 23:
        ore = 'coal'
    elif randomNum <= 30:
        ore = 'copper'
    elif (randomNum == 32 or randomNum == 31) and upgradeInv['ore ext']:
        ore = 'amethyst'   
    elif randomNum == 33 and upgradeInv['potato'] and ran.randrange(77) == 33:
        ore = 'poisonous potato'
    elif randomNum == 34 and upgradeInv['ruby'][0] and r <= 8:
        ore = 'ruby'
    else:
        ore = 'none'

    return ore

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Nether:
def oreN(upgradeInv):
    if upgradeInv['luckM']:
        randomNum = ran.randint(0,30)
    elif upgradeInv['luck']:
        randomNum = ran.randint(0,40)
    else:
        randomNum = ran.randint(0,65)

    if randomNum == 0:
        ore = 'netherite'
    elif randomNum <= 10:
        ore = 'quartz'
    elif randomNum <= 25:
        ore = 'nether gold'
    elif randomNum == 26 and upgradeInv['ore ext']:
        ore = 'gilded blackstone'
    elif (randomNum == 27 or randomNum == 28) and upgradeInv['ore ext']:
        ore = 'glowstone'
    else:
        ore = 'none'

    return ore

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Poisonous Potato:
def oreP(upgradeInv):
    if upgradeInv['luckM']:
        randomNum = ran.randint(0,35)
    elif upgradeInv['luck']:
        randomNum = ran.randint(0,50)
    else:
        randomNum = ran.randint(0,75)

    if randomNum == 0:
        ore = 'resin'
    elif randomNum <= 2:
        ore = 'diamond'
    elif randomNum <= 7:
        ore = 'gold'
    elif randomNum <= 13:
        ore = 'iron'
    elif randomNum <= 18:
        ore = 'lapis'
    elif randomNum <= 23:
        ore = 'redstone'
    elif randomNum <= 32:
        ore = 'copper'
    else:
        ore = 'none'

    return ore