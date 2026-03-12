import tkinter as tk
import random as ran




start = True
score = 0
multiplier = 1
blocks = []

root = tk.Tk()
root.title("Minecraft")
root.geometry('10000x100000')
root.state('zoomed')

images = {'stone': tk.PhotoImage(file='assets/images/stoneImageMinecraft.png'),
            'deepslate': tk.PhotoImage(file='assets/images/deepslateImageMinecraft.png'),
            'bedrock': tk.PhotoImage(file='assets/images/bedrockImageMinecraft.png'),
            'netherack': tk.PhotoImage(file='assets/images/netherackImageMinecraft.png'),
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
            'deepslateIron': tk.PhotoImage(file='assets/images/deepslateIronImageMinecraft.png')
            }






def multiplierUpgrade(a):
    global multiplier
    global score
    if score >= a*100:
        multiplier += a
        score -= 100*a
        nextRoundA()

def skipUpgrade():
    nextRoundA()






def nextRoundA():
    for _ in upgrades:
        _.grid_forget()

    nextRound()






def button_click(r,c,block):
    global start
    global score
    #print('Block clicked:',block)
    #print(f'Row: {r} \nCol: {c}')
    if (block != 'bedrock') and ((((blocks[r+1][c] == 'air') or (blocks [r-1][c] == 'air')) or ((blocks[r][c+1] == 'air') or (blocks[r][c-1] == 'air'))) or (start and ((block == 'stone')or block == 'netherack'))):
        blocks[r][c].grid_forget()
        blocks[r][c] = 'air'
        if start:
            start = False
        if (block == 'stone') or (block == 'netherack'):
            score -= 1
        elif block == 'deepslate':
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
        blocks[15][0] = tk.Button(root, text=score, bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        blocks[15][0].grid_forget
        blocks[15][0].grid(row=15, column=0, sticky="nsew", padx=5, pady=5)
    #print(f'Score: {score}')
    if (r == 15) and (c == 1):
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
    global upgrades

    upgrades = ['click','click5','click10']
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
            upgrades[upg] = tk.Button(root, text = 'Multiplier Upgrade (x1):\n100 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(1))

        if upgrades[upg] == 'click5':
            upgrades[upg] = tk.Button(root, text = 'Multiplier Upgrade (x5):\n500 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(5))

        if upgrades[upg] == 'click10':
            upgrades[upg] = tk.Button(root, text = 'Multiplier Upgrade (x10):\n1000 Score', bg = 'gray30', fg = 'gray5', command = lambda: multiplierUpgrade(10))

        if upgrades[upg] == 'skip':
            upgrades[upg] = tk.Button(root, text = 'Skip Upgrade:\n0 Score', bg = 'gray30', fg = 'gray5', command = lambda: skipUpgrade())

        upgrades[upg].grid(row=50, column=(upg+1)*3, sticky="nsew", padx=5, pady=5)











def nextRound():
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

                randomNum = ran.randint(0,75)

                if randomNum <= 25:
                    ore = 'copper'
                    if randomNum <= 17:
                        ore = 'coal'
                        if randomNum <= 12:
                            ore = 'redstone'
                            if randomNum <= 9:
                                ore = 'lapis'
                                if randomNum <= 6:
                                    ore = 'iron'
                                    if randomNum <= 3:
                                        ore = 'gold'
                                        if randomNum <= 1:
                                            ore = 'diamond'
                                            if randomNum == 0:
                                                ore = 'emerald'
                else:
                    ore = 'none'


                if (r == 15):
                    if c == 0:
                        button = tk.Button(root, text=score, bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    elif c == 1:
                        button = tk.Button(root, text='Next', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
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
                        button = tk.Button(root, text="", bg='blue', fg='blue', command=lambda r=r, c=c: button_click(r,c,'lapis'))
                    
                    elif ore == 'copper':
                        button = tk.Button(root, text="", bg='dark orange', fg='dark orange', command=lambda r=r, c=c: button_click(r,c,'copper'))
                    
                    elif ore == 'iron':
                        if r <= 8:
                            button = tk.Button(root, image = images["iron"], bg = 'gray55', command=lambda r=r, c=c: button_click(r,c,'iron'))
                        else:
                            button = tk.Button(root, image=images['deepslateIron'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'iron'))

                    elif ore == 'redstone':
                        button = tk.Button(root, text="", bg='red', fg='red', command=lambda r=r, c=c: button_click(r,c,'redstone'))

                elif r <= 8:
                    button = tk.Button(root, image=images['stone'], bg = 'gray55', command=lambda r=r, c=c: button_click(r,c,'stone'))
                else:
                    button = tk.Button(root, image=images['deepslate'], bg = 'gray40', command=lambda r=r, c=c: button_click(r,c,'deepslate'))
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)


            elif dimension == 'nether':
                root.configure(background='#723232')


                randomNum = ran.randint(0,75)

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
                        button = tk.Button(root, text=score, bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    elif (c == 1) and (r == 15):
                        button = tk.Button(root, text='Next', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
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
                    button = tk.Button(root, image = images['netherack'], bg='#723232', command=lambda r=r, c=c: button_click(r,c,'netherack'))
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)


        else:
            blocks[r].append('barrier')

nextRound()

root.mainloop()