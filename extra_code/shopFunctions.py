import tkinter as tk

def shopList(upgradeInv):
    upgrades = ['click','click5','click10']

    if not upgradeInv["penalty s"]:
        upgrades.append('penalty s')
    if not upgradeInv["penalty n"]:
        upgrades.append('penalty n')
    if not upgradeInv["penalty d"]:
        upgrades.append('penalty d')

    if not upgradeInv["luck"]:
        upgrades.append('luck')

    if not upgradeInv["st free"]:
        upgrades.append('st free')

    if not upgradeInv["diag mine"]:
        upgrades.append('diag mine')

    if not upgradeInv["ore ext"]:
        upgrades.append('ore ext')

    if not upgradeInv["tnt"]:
        upgrades.append('tnt')

    if not upgradeInv["fortune"][0]:
        upgrades.append('fortune1')
    elif upgradeInv['fortune'][1] == 25:
        upgrades.append('fortune2')
    elif upgradeInv['fortune'][1] == 50:
        upgrades.append('fortune3')
    elif upgradeInv['fortune'][1] == 75:
        upgrades.append('fortuneM')

    if not upgradeInv['ext dim']:
        upgrades.append('ext dim')
    elif not upgradeInv['penalty e']:
        upgrades.append('penalty e')



    return upgrades




    

def buttonDef(upg, root, multiplierUpgrade, invUpgrade, nextRoundA, fortuneUpgrade):
        if upg == 'click':
            upg = tk.Button(root, text = '🔨\nMultiplier Upgrade (x1):\n100 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(1))
        if upg == 'click5':
            upg = tk.Button(root, text = '⛏\nMultiplier Upgrade (x5):\n500 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(5))
        if upg == 'click10':
            upg = tk.Button(root, text = '🛠\nMultiplier Upgrade (x10):\n1000 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(10))

        if upg == 'fortune1':
            upg = tk.Button(root, text = '💵\nFortune (25%):\n450 Score', bg = 'gray30', fg = 'gray5', command = lambda: fortuneUpgrade(25,450))
        if upg == 'fortune2':
            upg = tk.Button(root, text = '💸\nFortune (50%):\n675 Score', bg = 'gray30', fg = 'gray5', command = lambda: fortuneUpgrade(50,675))
        if upg == 'fortune3':
            upg = tk.Button(root, text = '💰\nFortune (75%):\n725 Score', bg = 'gray30', fg = 'gray5', command = lambda: fortuneUpgrade(75,725))
        if upg == 'fortuneM':
            upg = tk.Button(root, text = '💰\nFortune (100%):\n1125 Score', bg = 'gray30', fg = 'gray5', command = lambda: fortuneUpgrade(100,1125))

        if upg == 'penalty s':
            upg = tk.Button(root, text = '🪨\nRemove Stone Penalty:\n250 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty s',250,False))
        if upg == 'penalty n':
            upg = tk.Button(root, text = '🧱\nRemove Netherrack Penalty:\n150 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty n',150,False))
        if upg == 'penalty d':
            upg = tk.Button(root, text = '🪦\nRemove Deepslate Penalty:\n350 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty d',350,False))
        if upg == 'penalty e':
            upg = tk.Button(root, text = '🗿\nRemove Endstone Penalty:\n1 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty e',1,False))

        if upg == 'luck':
            upg = tk.Button(root, text = '🍀\nIncrease Ore Spawns:\n5000 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('luck',5000,False))

        if upg == 'st free':
            upg = tk.Button(root, text = '🔓\nUnbind Starting Point:\n375 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('st free',375,False))

        if upg == 'diag mine':
            upg = tk.Button(root, text = '🔀\nMine Diagonally:\n325 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('diag mine',325,False))

        if upg == 'ore ext':
            upg = tk.Button(root, text = '💎\nUnlock Pseudo-Ores:\n750 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('ore ext',750,False))
        
        if upg == 'tnt':
            upg = tk.Button(root, text = '🧨\nBlast Radius Mining:\n3750 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('tnt',3750,False))

        if upg == 'dim pick':
            upg = tk.Button(root, text = '🌌\nChoose Next Dimension:\n1250 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('dim pick',1250,True))

        if upg == 'ext dim':
            upg = tk.Button(root, text = '🪐\nExtra Dimension:\n75 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('ext dim',75,False))


        if upg == 'skip':
            upg = tk.Button(root, text = '☑️\nSkip Upgrade:\n0 Score', bg = 'gray30', fg = 'gray5', command = lambda: nextRoundA())

        return upg