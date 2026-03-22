import tkinter as tk
import random as ran

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Upgrade List:
def shopList(blocksMined,upgradeInv,dimensionPickB,upgReroll,command,r):
    upgrades = ['click','click5','click10']

    if not upgradeInv["penalty s"]:
        upgrades.append('penalty s')
    elif not upgradeInv["penalty s+"]:
        upgrades.append('penalty s+')
    if not upgradeInv["penalty n"]:
        upgrades.append('penalty n')
    elif not upgradeInv["penalty n+"]:
        upgrades.append('penalty n+')
    if not upgradeInv["penalty d"]:
        upgrades.append('penalty d')
    elif not upgradeInv["penalty d+"]:
        upgrades.append('penalty d+')

    if not upgradeInv["luck"]:
        upgrades.append('luck')
    elif not upgradeInv['luckM']:
        upgrades.append('luckM')

    if not upgradeInv["st free"]:
        upgrades.append('st free')

    if not upgradeInv["diag mine"]:
        upgrades.append('diag mine')
    elif (not upgradeInv['unl mine'][0]) and (upgradeInv['unl mine'][1]):
        upgrades.append('unl mine')

    if (upgradeInv['bedr'][1]):
        if (not upgradeInv['bedr'][0]):
            upgrades.append('bedr')
        elif not upgradeInv["penalty b"]:
            upgrades.append('penalty b')
        elif not upgradeInv["penalty b+"]:
            upgrades.append('penalty b+')

    if not upgradeInv["auto"][0]:
        upgrades.append('auto')

    if not upgradeInv["ore ext"]:
        upgrades.append('ore ext')
    
    if not upgradeInv["time"]:
        upgrades.append('time')
    elif not upgradeInv['Xtime']:
        upgrades.append('Xtime')
    if not upgradeInv["ins nex"]:
        upgrades.append('ins nex')

    if not upgradeInv["tnt"]:
        upgrades.append('tnt')
    if not upgradeInv["tnt start"]:
        upgrades.append('tnt start')

    if not upgradeInv["fortune"][0]:
        upgrades.append('fortune1')
    elif upgradeInv['fortune'][1] == 25:
        upgrades.append('fortune2')
    elif upgradeInv['fortune'][1] == 50:
        upgrades.append('fortune3')
    elif upgradeInv['fortune'][1] == 75:
        upgrades.append('fortuneM')

    if upgradeInv['fortune'][0] and not upgradeInv['fortune x3']:
        upgrades.append('fortune x3')

    if not upgradeInv['ext dim']:
        upgrades.append('ext dim')
    elif not upgradeInv['penalty e']:
        upgrades.append('penalty e')
    elif not upgradeInv['penalty e+']:
        upgrades.append('penalty e+')

    if upgradeInv['ore ext'] and upgradeInv['ext dim'] and not upgradeInv['potato'] and ran.randrange(33) == 7:
        upgrades.append('potato')
    
    if upgradeInv['🏆'][0]:
        if not upgradeInv['penalty p']:
            upgrades.append('penalty p')
        elif not upgradeInv['penalty p+']:
            upgrades.append('penalty p+')


    if not upgradeInv["dim pick"][0]:
        upgrades.append('dim pick')
    elif not r:
        dimensionPickB.grid(row=0, column=16, sticky="nsew", pady=5, padx=5)
    if not upgradeInv["upg re"]:
        upgrades.append('upg re')
    elif not r:
        if upgradeInv['dim pick'][0]:
            upgReroll.grid(row=1, column=16, sticky="nsew", pady=5, padx=5)
        else:
            upgReroll.grid(row=0, column=16, sticky="nsew", pady=5, padx=5)
    if not upgradeInv["stat view"]:
        upgrades.append('stat view')
    elif not r:
        if upgradeInv['dim pick'][0] and upgradeInv["upg re"]:
            command.grid(row=2, column=16, sticky="nsew", pady=5, padx=5)
        elif upgradeInv['dim pick'][0] or upgradeInv["upg re"]:
            command.grid(row=1, column=16, sticky="nsew", pady=5, padx=5)
        else:
            command.grid(row=0, column=16, sticky="nsew", pady=5, padx=5)

    if (not upgradeInv['ruby'][0]) and (upgradeInv['ruby'][1]):
        upgrades.append('ruby')



    return upgrades

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Button Defining:
def buttonDef(upg, root, multiplierUpgrade, invUpgrade, nextRoundA, fortuneUpgrade):

        if upg == 'click':
            upg = tk.Button(root, text = '🔨\nMultiplier Upgrade (x1):\n100 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(1))
        if upg == 'click5':
            upg = tk.Button(root, text = '⛏\nMultiplier Upgrade (x5):\n500 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(5))
        if upg == 'click10':
            upg = tk.Button(root, text = '🛠\nMultiplier Upgrade (x10):\n1000 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(10))

        if upg == 'fortune1':
            upg = tk.Button(root, text = '🪙\nFortune (25%):\n450 Score', bg = 'gray30', fg = 'gray5', command = lambda: fortuneUpgrade(25,450))
        if upg == 'fortune2':
            upg = tk.Button(root, text = '💵\nFortune (50%):\n675 Score', bg = 'gray30', fg = 'gray5', command = lambda: fortuneUpgrade(50,675))
        if upg == 'fortune3':
            upg = tk.Button(root, text = '💸\nFortune (75%):\n725 Score', bg = 'gray30', fg = 'gray5', command = lambda: fortuneUpgrade(75,725))
        if upg == 'fortuneM':
            upg = tk.Button(root, text = '💰\nFortune (100%):\n1125 Score', bg = 'gray30', fg = 'gray5', command = lambda: fortuneUpgrade(100,1125))
        if upg == 'fortune x3':
            upg = tk.Button(root, text = '💳\nTriple Fortune:\n825 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('fortune x3',825,False))

        if upg == 'penalty s':
            upg = tk.Button(root, text = '🪨\nRemove Stone Penalty:\n250 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty s',250,False))
        if upg == 'penalty n':
            upg = tk.Button(root, text = '🧱\nRemove Netherrack Penalty:\n150 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty n',150,False))
        if upg == 'penalty d':
            upg = tk.Button(root, text = '🪦\nRemove Deepslate Penalty:\n350 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty d',350,False))
        if upg == 'penalty e':
            upg = tk.Button(root, text = '🗿\nRemove Endstone Penalty:\n1 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty e',1,False))
        if upg == 'penalty p':
            upg = tk.Button(root, text = '🏺\nRemove Potone Penalty:\n33 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty p',33,False))
        if upg == 'penalty b':
            upg = tk.Button(root, text = '🕋\nRemove Bedrock Penalty:\n77 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty b',77,False))

        if upg == 'penalty s+':
            upg = tk.Button(root, text = '📎\nPositive Score Stone:\n500 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty s+',500,False))
        if upg == 'penalty n+':
            upg = tk.Button(root, text = '🚨\nPositive Score Netherrack:\n300 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty n+',300,False))
        if upg == 'penalty d+':
            upg = tk.Button(root, text = '🔗\nPositive Score Deepslate:\n700 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty d+',700,False))
        if upg == 'penalty e+':
            upg = tk.Button(root, text = '🔩\nPositive Score Endstone:\n150 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty e+',150,False))
        if upg == 'penalty p+':
            upg = tk.Button(root, text = '☣️\nPositive Score Potone:\n250 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty p+',250,False))
        if upg == 'penalty b+':
            upg = tk.Button(root, text = '💍\nPositive Score Bedrock:\n333 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty b+',333,False))

        if upg == 'luck':
            upg = tk.Button(root, text = '☘️\nEnhance Ore Spawns:\n5000 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('luck',5000,False))
        if upg == 'luckM':
            upg = tk.Button(root, text = '🍀\nEnhance Ore Spawns+:\n7500 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('luckM',7500,False))

        if upg == 'st free':
            upg = tk.Button(root, text = '🔓\nUnbind Starting Point:\n375 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('st free',375,False))
        if upg == 'diag mine':
            upg = tk.Button(root, text = '🔀\nMine Diagonally:\n325 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('diag mine',325,False))
        if upg == 'unl mine':
            upg = tk.Button(root, text = '🌀\nIntangabilitic Mining:\n2675 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('unl mine',2675,True))
        if upg == 'auto':
            upg = tk.Button(root, text = '⚙️\nAutomatic Mining:\n4150 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('auto',4150,True))
        if upg == 'bedr':
            upg = tk.Button(root, text = '🗜\nBedrock Minability:\n300 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('bedr',300,True))
        
        if upg == 'tnt':
            upg = tk.Button(root, text = '🧨\nBlast Radius Mining:\n3750 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('tnt',3750,False))
        if upg == 'tnt start':
            upg = tk.Button(root, text = '💣\nExplosive Start (5x5):\n2750 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('tnt start',2750,False))

        if upg == 'ext dim':
            upg = tk.Button(root, text = '🪐\nExtra Dimension:\n75 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('ext dim',75,False))
        if upg == 'potato':
            upg = tk.Button(root, text = '🃏\n???:\n666 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('potato',666,False))
        if upg == 'ore ext':
            upg = tk.Button(root, text = '💎\nUnlock Pseudo-Ores:\n750 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('ore ext',750,False))
        if upg == 'ruby':
            upg = tk.Button(root, text = '♦️\nUnlock Ruby Ore:\n675 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('ruby',675,True))

        if upg == 'time':
            upg = tk.Button(root, text = '🕰\nMore Round Time:\n475 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('time',475,False))
        if upg == 'Xtime':
            upg = tk.Button(root, text = '⏰\nInfinite Round Time:\n550 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('Xtime',550,False))
        if upg == 'ins nex':
            upg = tk.Button(root, text = "🔑\nInstant 'Next' Unlock:\n425 Score", bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('ins nex',425,False))

        if upg == 'dim pick':
            upg = tk.Button(root, text = '🌌\nChoose Next Dimension:\n1250 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('dim pick',1250,True))
        if upg == 'upg re':
            upg = tk.Button(root, text = '♻️\nUpgrade Rerolling:\n3150 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('upg re',3150,False))
        if upg == 'stat view':
            upg = tk.Button(root, text = '👁\nStat & Upgrade Viewing:\n50 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('stat view',50,False))


        if upg == 'skip':
            upg = tk.Button(root, text = '☑️\nSkip Upgrade:\n0 Score', bg = 'gray30', fg = 'gray5', command = lambda: nextRoundA())

        if upg == '🏆':
            upg = tk.Button(root, text = '🏆\nHidden Trophy:\n0 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('🏆',0,True))

        return upg