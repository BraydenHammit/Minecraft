import random as ran

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Random Dimension Function:
def dimensionR(upgradeInv,root):
    if upgradeInv['dim pick'][0]:
        if upgradeInv['dim pick'][1] == 'n':
            dimension = 'nether'
            root.configure(background='#723232')
        elif upgradeInv['dim pick'][1] == 'o':
            dimension = 'overworld'
            root.configure(background='grey')
        elif upgradeInv['dim pick'][1] == 'e':
            dimension = 'end'
            root.configure(background="#D7D597")

    elif ran.randint(0,4) == 1:
        if ran.randint(0,2) == 1 and upgradeInv['ext dim']:
            dimension = 'end'
            root.configure(background="#D7D597")
        else:
            dimension = 'nether'
            root.configure(background='#723232')
    else:
        dimension = 'overworld'
        root.configure(background='grey')

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
            dimensionPickB.configure(text='Next Dimension:\nOverworld', bg='#1f5f1f', fg="#0DAA0D")
            upgradeInv['dim pick'][1] = 'o'
    elif upgradeInv['dim pick'][1] == 'e':
        dimensionPickB.configure(text='Next Dimension:\nOverworld', bg='#1f5f1f', fg="#0DAA0D")
        upgradeInv['dim pick'][1] = 'o'