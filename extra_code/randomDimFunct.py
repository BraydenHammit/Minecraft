import random as ran

def dimensionR(upgradeInv,root):
    if upgradeInv['dim pick'][0]:
        if upgradeInv['dim pick'][1] == 'n':
            dimension = 'nether'
            root.configure(background='#723232')
        elif upgradeInv['dim pick'][1] == 'o':
            dimension = 'overworld'
            root.configure(background='grey')

    elif ran.randint(0,4) == 1:
        dimension = 'nether'
        root.configure(background='#723232')
    else:
        dimension = 'overworld'
        root.configure(background='grey')

    return dimension