import random as ran

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Random Dimension Function:
def dimensionR(upgradeInv,root):
    bgs = {
        'nether': '#723232',
        'overworld': 'grey',
        'end': "#D7D597",
        'moon': "#dad7bb",
        'poisonous potato': "#8D4C1F"
    }

    if upgradeInv['dim pick'][0]:
        if upgradeInv['dim pick'][1] == 'n':
            dimension = 'nether'
        elif upgradeInv['dim pick'][1] == 'o':
            dimension = 'overworld'
        elif upgradeInv['dim pick'][1] == 'e':
            dimension = 'end'
        elif upgradeInv['dim pick'][1] == 'p':
            dimension = 'poisonous potato'
        elif upgradeInv['dim pick'][1] == 'm':
            dimension = 'moon'
        elif upgradeInv['dim pick'][1] == 'r':
            dims = ['overworld','nether']
            if upgradeInv['ext dim']:
                dims.append('end')
            if upgradeInv['🏆'][0]:
                dims.append('poisonous potato')
            dimension = ran.choice(dims)


    elif ran.randint(0,4) == 1:
        if ran.randint(0,2) == 1 and upgradeInv['ext dim']:
            dimension = 'end'
        else:
            dimension = 'nether'
    else:
        dimension = 'overworld'
    
    root.configure(background=bgs[dimension])

    return dimension

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Dimension Switch Button:
def dimButton(upgradeInv,dimensionPickB):
    if upgradeInv['dim pick'][1] == 'o':
        dimensionPickB.configure(text='Next Dimension:\nNether', fg="#A83A3A", bg="#3f1818")
        upgradeInv['dim pick'][1] = 'n'
    elif upgradeInv['dim pick'][1] == 'n':
        if upgradeInv['ext dim']:
            dimensionPickB.configure(text='Next Dimension:\nEnd', fg="#c8bf73", bg="#626047")
            upgradeInv['dim pick'][1] = 'e'
        else:
            dimensionPickB.configure(text='Next Dimension:\nRandom', bg="#942465", fg="#550A2A")
            upgradeInv['dim pick'][1] = 'r'
    elif upgradeInv['dim pick'][1] == 'e':
        if upgradeInv['🏆'][0]:
            dimensionPickB.configure(text='Next Dimension:\nPoisonous Potato', fg="#e7851c", bg="#724017")
            upgradeInv['dim pick'][1] = 'p'
        else:
            dimensionPickB.configure(text='Next Dimension:\nRandom', bg="#942465", fg="#550A2A")
            upgradeInv['dim pick'][1] = 'r'
    elif upgradeInv['dim pick'][1] == 'p':
        dimensionPickB.configure(text='Next Dimension:\nRandom', bg="#942465", fg="#550A2A")
        upgradeInv['dim pick'][1] = 'r'
    elif upgradeInv['dim pick'][1] == 'r':
        dimensionPickB.configure(text='Next Dimension:\nOverworld', bg='#1f5f1f', fg="#0DAA0D")
        upgradeInv['dim pick'][1] = 'o'