import tkinter as tk
import random as ran




start = True
score = 0
multiplier = 1000
nextTimer = 5
blocks = []
upgradeInv = {
    'penalty n': False,
    'penalty s': False,
    'penalty d': False,
    'luck': False,
    'st free': False,
    'diag mine': False
}

root = tk.Tk()
root.title("Minecraft")
root.state('zoomed')

intro =  tk.Label(root, text="How to Play:\nYou must start by mining a stone or netherrack block.\nYou can only mine blocks next to blocks you've already mined.\nYou lose score for mining stone, deepslate, and netherrack.\nYour score is shown on the bottom left bedrock,\nand you can go to the next round by clicking 'Next'.\nIn between rounds, you can buy upgrades by spending your score.\nThese upgrades can boost ore spawns, the amount of score you get per ore,\ngain the ability to start mining on things other than stone or netherrack,\nor remove the score penalties when mining netherrack, stone, and deepslate.\n\nOre Values:\nStone & Netherrack = -1\nDeepslate = -1.5\nCoal, Copper, & Nether Gold = 1.75\nRedstone & Lapis = 2.5\nIron, Gold, & Quartz = 3.25\nDiamond = 5\nEmerald & Netherite = 12.5")
startB =  tk.Button(root, text = 'Start', bg='gray85', command= lambda: startGame())

def startGame():
    global intro, startB
    intro.pack_forget()
    startB.pack_forget()
    nextRound()


images = {'stone': tk.PhotoImage(file='assets/images/stoneImageMinecraft.png'),
            'deepslate': tk.PhotoImage(file='assets/images/deepslateImageMinecraft.png'),
            'bedrock': tk.PhotoImage(file='assets/images/bedrockImageMinecraft.png'),
            'netherrack': tk.PhotoImage(file='assets/images/netherackImageMinecraft.png'),
            'deepslateEmerald': tk.PhotoImage(file='assets/images/deepslateEmeraldImageMinecraft.png'),
            'deepslateCoal': tk.PhotoImage(file='assets/images/deepslateCoalImageMinecraft.png'),
            'coal': tk.PhotoImage(file='assets/images/coalImageMinecraft.png'),
            'diamond': tk.PhotoImage(file='assets/images/diamondImageMinecraft.png'),
            'deepslateDiamond': tk.PhotoImage(file='assets/images/deepslateDiamondImageMinecraft.png'),
            'netherite': tk.PhotoImage(file='assets/images/netheriteImageMinecraft.png'),
            'netherGold': tk.PhotoImage(file='assets/images/netherGoldImageMinecraft.png'),
            'quartz': tk.PhotoImage(file='assets/images/quartzImageMinecraft.png'),
            'iron': tk.PhotoImage(file='assets/images/ironImageMinecraft.png'),
            'emerald': tk.PhotoImage(file='assets/images/emeraldImageMinecraft.png'),
            'gold': tk.PhotoImage(file='assets/images/goldImageMinecraft.png'),
            'deepslateGold': tk.PhotoImage(file='assets/images/deepslateGoldImageMinecraft.png'),
            'deepslateIron': tk.PhotoImage(file='assets/images/deepslateIronImageMinecraft.png'),
            'deepslateLapis': tk.PhotoImage(file='assets/images/deepslateLapisImageMinecraft.png'),
            'deepslateRedstone': tk.PhotoImage(file='assets/images/deepslateRedstoneImageMinecraft.png'),
            'deepslateCopper': tk.PhotoImage(file='assets/images/deepslateCopperImageMinecraft.png'),
            'copper': tk.PhotoImage(file='assets/images/copperImageMinecraft.png'),
            'redstone': tk.PhotoImage(file='assets/images/redstoneImageMinecraft.png'),
            'lapis': tk.PhotoImage(file='assets/images/lapisImageMinecraft.png')
            }






def multiplierUpgrade(a):
    global multiplier, score
    if score >= a*100:
        multiplier += a
        score -= 100*a
        nextRoundA()

def invUpgrade(t,c):
    global upgradeInv, score
    if score >= c:
        upgradeInv[t] = True
        score -= c
        nextRoundA()

def skipUpgrade():
    nextRoundA()






def nextRoundA():
    for _ in upgrades:
        _.grid_forget()

    nextRound()






def button_click(r,c,block):
    global start, score, nextTimer
    if block != 'bedrock':
        check = ((((blocks[r+1][c] == 'air') or (blocks [r-1][c] == 'air')) or ((blocks[r][c+1] == 'air') or (blocks[r][c-1] == 'air'))) or (start and ((block == 'stone')or block == 'netherrack')))
        checkD = ((blocks[r+1][c+1] == 'air') or (blocks[r-1][c-1] == 'air') or (blocks[r-1][c+1] == 'air') or (blocks[r+1][c-1] == 'air')) and upgradeInv['diag mine']
        if check or checkD or (start and upgradeInv['st free']):
            blocks[r][c].grid_forget()
            blocks[r][c] = 'air'
            if start:
                start = False

            if (block == 'stone') and (not upgradeInv['penalty s']):
                score -= 1
            elif (block == 'netherrack') and (not upgradeInv['penalty n']):
                score -= 1
            elif (block == 'deepslate' and (not upgradeInv['penalty d'])):
                score -= 1.5
            elif (block == 'coal') or (block == 'nether gold') or (block == 'copper'):
                score += 1.75 * multiplier
            elif (block == 'redstone') or (block == 'lapis'):
                score += 2.5 * multiplier
            elif (block == 'iron') or (block == 'gold') or (block == 'quartz'):
                score += 3.25 * multiplier
            elif (block == 'diamond'):
                score += 5 * multiplier
            elif (block == 'emerald') or (block == 'netherite'):
                score += 12.5 * multiplier
            blocks[15][0] = tk.Button(root, text=round(score,2), bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
            blocks[15][0].grid(row=15, column=0, sticky="nsew", padx=5, pady=5)

    elif (r == 15) and (c == 1) and (nextTimer == 0):
        start = True
        nextRoundPre()








def nextRoundPre():
    root.configure(background='grey')

    global blocks
    #print('Next Round Pre')

    for eachCol in blocks:

        for eachRow in eachCol:

            if (eachRow == 'air') or (eachRow == 'barrier'):
                continue

            eachRow.grid_forget()

    blocks[15][0].grid(row=15, column=0, sticky="nsew", padx=5, pady=5)

    #print(blocks)
    blocks = []

    nextShop()












def nextShop():
    global upgrades, upgradeInv

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
    choices = []

    for _ in range(3):
        choiceExt = ran.randint(0,len(upgrades)-1)
        choice = upgrades[choiceExt]
        upgrades.pop(choiceExt)
        choices.append(choice)
    choices.append('skip')

    upgrades = choices

    for upg in range(len(upgrades)):
        if upgrades[upg] == 'click':
            upgrades[upg] = tk.Button(root, text = '🔨\nMultiplier Upgrade (x1):\n100 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(1))
        if upgrades[upg] == 'click5':
            upgrades[upg] = tk.Button(root, text = '⛏\nMultiplier Upgrade (x5):\n500 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(5))
        if upgrades[upg] == 'click10':
            upgrades[upg] = tk.Button(root, text = '🛠\nMultiplier Upgrade (x10):\n1000 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(10))


        if upgrades[upg] == 'penalty s':
            upgrades[upg] = tk.Button(root, text = '🪨\nRemove Stone Penalty:\n250 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty s',250))
        if upgrades[upg] == 'penalty n':
            upgrades[upg] = tk.Button(root, text = '🧱\nRemove Netherrack Penalty:\n150 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty n',150))
        if upgrades[upg] == 'penalty d':
            upgrades[upg] = tk.Button(root, text = '🪦\nRemove Deepslate Penalty:\n350 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('penalty d',350))

        if upgrades[upg] == 'luck':
            upgrades[upg] = tk.Button(root, text = '🍀\nIncrease Ore Spawns:\n5000 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('luck',5000))

        if upgrades[upg] == 'st free':
            upgrades[upg] = tk.Button(root, text = '🔓\nUnbind Starting Point:\n375 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('st free',375))

        if upgrades[upg] == 'diag mine':
            upgrades[upg] = tk.Button(root, text = '🔀\nMine Diagonally:\n325 Score', bg = 'gray30', fg = 'gray5', command = lambda: invUpgrade('diag mine',325))


        if upgrades[upg] == 'skip':
            upgrades[upg] = tk.Button(root, text = 'Skip Upgrade:\n0 Score', bg = 'gray30', fg = 'gray5', command = lambda: skipUpgrade())

        upgrades[upg].grid(row=10, column=(upg+1)*3, sticky="nsew", padx=5, pady=5)





def nextTime():
    global nextTimer
    nextTimer -= 1
    if nextTimer > 0:
        blocks[15][1].configure(text=f'Next (🔒 {nextTimer})')
        root.after(1000,nextTime)
    else:
        blocks[15][1].configure(text='Next')





def nextRound():
    global nextTimer
    nextTimer = 5

    if ran.randint(0,4) == 1:
        dimension = 'nether'
    else:
        dimension = 'overworld'


    for r in range(16):
        root.grid_rowconfigure(r, weight=1)
        blocks.append([])

        for c in range(16):
            root.grid_columnconfigure(c, weight=1)

            if dimension == 'overworld':
                root.configure(background='grey')

                if upgradeInv['luck']:
                    randomNum = ran.randint(0,50)
                else:
                    randomNum = ran.randint(0,75)

                if randomNum <= 30:
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


                if (r == 15):
                    if c == 0:
                        button = tk.Button(root, text=round(score,2), bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    elif c == 1:
                        button = tk.Button(root, text=f'Next (🔒 {nextTimer})', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    else:
                        button = tk.Button(root, image=images['bedrock'], bg='gray30', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                elif ore != 'none':
                    
                    if ore == 'diamond':
                        if r <= 8:
                            button = tk.Button(root, image = images['diamond'], bg='gray55', command=lambda r=r, c=c: button_click(r,c,'diamond'))
                        else:
                            button = tk.Button(root, bg='gray40', image = images['deepslateDiamond'], command=lambda r=r, c=c: button_click(r,c,'diamond'))
                    
                    elif ore == 'gold':
                        if r <= 8:
                            button = tk.Button(root, image=images['gold'], bg='gray55', command=lambda r=r, c=c: button_click(r,c,'gold'))
                        else:
                            button = tk.Button(root, image=images['deepslateGold'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'gold'))
                    
                    elif ore == 'emerald':
                        if r <= 8:
                            button = tk.Button(root, image=images['emerald'], bg='gray55', command=lambda r=r, c=c: button_click(r,c,'emerald'))
                        else:
                            button = tk.Button(root, image=images['deepslateEmerald'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'emerald'))
                    
                    elif ore == 'coal':
                        if r <= 8:
                            button = tk.Button(root, image = images['coal'], bg='gray55', command=lambda r=r, c=c: button_click(r,c,'coal'))
                        else:
                            button = tk.Button(root, image = images['deepslateCoal'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'coal'))
                    
                    elif ore == 'lapis':
                        if r <= 8:
                            button = tk.Button(root, image=images['lapis'], bg='gray55',  command=lambda r=r, c=c: button_click(r,c,'lapis'))
                        else:
                            button = tk.Button(root, image = images['deepslateLapis'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'lapis'))
                    
                    elif ore == 'copper':
                        if r <= 8:
                            button = tk.Button(root, image=images['copper'], bg='gray55', command=lambda r=r, c=c: button_click(r,c,'copper'))
                        else:
                            button = tk.Button(root, image=images['deepslateCopper'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'copper'))
                    
                    elif ore == 'iron':
                        if r <= 8:
                            button = tk.Button(root, image = images["iron"], bg = 'gray55', command=lambda r=r, c=c: button_click(r,c,'iron'))
                        else:
                            button = tk.Button(root, image=images['deepslateIron'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'iron'))

                    elif ore == 'redstone':
                        if r <= 8:
                            button = tk.Button(root, image=images['redstone'], bg='gray55', command=lambda r=r, c=c: button_click(r,c,'redstone'))
                        else:
                            button = tk.Button(root, image=images['deepslateRedstone'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'redstone'))

                elif r <= 8:
                    button = tk.Button(root, image=images['stone'], bg = 'gray55', command=lambda r=r, c=c: button_click(r,c,'stone'))
                else:
                    button = tk.Button(root, image=images['deepslate'], bg = 'gray40', command=lambda r=r, c=c: button_click(r,c,'deepslate'))

                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)


            elif dimension == 'nether':
                root.configure(background='#723232')


                if upgradeInv['luck']:
                    randomNum = ran.randint(0,40)
                else:
                    randomNum = ran.randint(0,65)

                if randomNum <= 25:
                    ore = 'nether gold'
                    if randomNum <= 10:
                        ore = 'quartz'
                        if randomNum == 0:
                            ore = 'netherite'
                else:
                    ore = 'none'


                if (r == 15) or (r == 0):
                    if (c == 0) and (r == 15):
                        button = tk.Button(root, text=round(score,2), bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    elif (c == 1) and (r == 15):
                        button = tk.Button(root, text=f'Next (🔒 {nextTimer})', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    else:
                        button = tk.Button(root, image= images['bedrock'], bg = 'gray30', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                elif ore != 'none':
                    if ore == 'quartz':
                        button = tk.Button(root, image = images['quartz'], bg='#723232', command=lambda r=r, c=c: button_click(r,c,'quartz'))
                    elif ore == 'nether gold':
                        button = tk.Button(root, image = images['netherGold'], bg='#723232', command=lambda r=r, c=c: button_click(r,c,'nether gold'))
                    elif ore == 'netherite':
                        button = tk.Button(root, image = images['netherite'], bg='#523933', command=lambda r=r, c=c: button_click(r,c,'netherite'))
                else:
                    button = tk.Button(root, image = images['netherrack'], bg='#723232', command=lambda r=r, c=c: button_click(r,c,'netherrack'))
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)


        else:
            blocks[r].append('barrier')         # add barrier so c-1 and c+1 checks never cause index errors

    root.after(1000,nextTime)


intro.pack(pady=150)
startB.pack(pady=50)

root.mainloop()