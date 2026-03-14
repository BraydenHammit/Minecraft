from minecraft import multiplierUpgrade, invUpgrade, nextRoundA
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



    return upgrades
    

def buttonDefine(upg, root):
        if upg == 'click':
            upg = tk.Button(root, text = '🔨\nMultiplier Upgrade (x1):\n100 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(1))
        if upg == 'click5':
            upg = tk.Button(root, text = '⛏\nMultiplier Upgrade (x5):\n500 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(5))
        if upg == 'click10':
            upg = tk.Button(root, text = '🛠\nMultiplier Upgrade (x10):\n1000 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(10))


        if upg == 'penalty s':
            upg = tk.Button(root, text = '🪨\nRemove Stone Penalty:\n250 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty s',250,False))
        if upg == 'penalty n':
            upg = tk.Button(root, text = '🧱\nRemove Netherrack Penalty:\n150 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty n',150,False))
        if upg == 'penalty d':
            upg = tk.Button(root, text = '🪦\nRemove Deepslate Penalty:\n350 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty d',350,False))

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


        if upg == 'skip':
            upg = tk.Button(root, text = '☑️\nSkip Upgrade:\n0 Score', bg = 'gray30', fg = 'gray5', command = lambda: nextRoundA())

        return upg