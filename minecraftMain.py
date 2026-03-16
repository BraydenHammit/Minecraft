import tkinter as tk
import random as ran
from extra_code.scoreFunction import scoreAS
from extra_code.shopFunctions import shopList, buttonDef
from extra_code.oreFunct import oreO, oreN
from extra_code.oreFunctDef import defOreN, defOreO, defOreE
from extra_code.randomDimFunct import dimensionR




start = True
nextR = False
score = 0
multiplier = 1
nextTimer = 5
timer = 15
blocks = []
blocksN = []
upgradeInv = {
    'penalty n': False,
    'penalty s': False,
    'penalty d': False,
    'penalty e': False,
    'penalty n+': False,
    'penalty s+': False,
    'penalty d+': False,
    'penalty e+': False,
    'luck': False,
    'luckM': False,
    'fortune': [False,0],
    'fortune x3': False,
    'st free': False,
    'diag mine': False,
    'tnt': False,                 # reminder: add a tnt sound effect (when you figure out how to add them)
    'tnt start': False,
    'dim pick': [False,'o'],
    'ext dim': False,
    'ore ext': False,
    'potato': False,
    'time': False
}

root = tk.Tk()
root.title("Minecraft")
root.state('zoomed')

intro =  tk.Label(root, text="How to Play:\nYou must start by mining a stone or netherrack block.\nYou can only mine blocks next to blocks you've already mined.\nYou lose score for mining stone, deepslate, and netherrack.\nYour score is shown on the bottom left bedrock,\nand you can go to the next round by clicking 'Next' (next to score).\nYou only have 15 seconds each round (shown next to the next button),\nand when that runs out the round automaticlly ends.\nIn between rounds, you can buy upgrades by spending your score.\nThese upgrades can boost ore spawns, the amount of score you get per ore,\ngain the ability to select what dimension it will be next round (the button is in the shop),\nincrease your mining to a 3x3 area with an explosive blast, apply a fortune enchantment,\ngain the ability to start mining on things other than stone or netherrack,\nremove the score penalties when mining netherrack, stone, endstone, and deepslate,\nunlock the ability to mine diagonally (between blocks) from pre-mined blocks,\nunlock two extra ores (one for each dimension) or an extra dimension, and much more.\n\nOre Values:\nStone, Endstone, & Netherrack = -1\nDeepslate = -1.5\nCoal, Copper, & Nether Gold = 1.75\nRedstone & Lapis = 2.5\nIron, Gold, & Quartz = 3.25\nDiamond = 5\nEmerald & Netherite = 12.5\n\nExtra Semi-Ores:\nGilded Blackstone & Amethyst = 7.5")
startB =  tk.Button(root, text = 'Start', bg='gray85', command= lambda: startGame())
dimensionPickB = tk.Button(root, text='Next Dimension:\nOverworld', bg='#1f5f1f', fg="#0DAA0D", command=lambda: dimensionSwitch())
multButton = tk.Button(root, text=f'Multiplier: {multiplier}', bg='gray30', fg="gray5")
fortButton = tk.Button(root, text=f'Fortune: {upgradeInv["fortune"][1]}%', bg='gray30', fg="gray5")

images = {
            #Rocks:
            'stone': tk.PhotoImage(file='assets/images/stoneImageMinecraft.png'),
            'deepslate': tk.PhotoImage(file='assets/images/deepslateImageMinecraft.png'),
            'bedrock': tk.PhotoImage(file='assets/images/bedrockImageMinecraft.png'),
            'netherrack': tk.PhotoImage(file='assets/images/netherackImageMinecraft.png'),
            'endstone': tk.PhotoImage(file='assets/images/endstoneImageMinecraft.png'),
            #Ores:
            'coal': tk.PhotoImage(file='assets/images/coalImageMinecraft.png'),
            'diamond': tk.PhotoImage(file='assets/images/diamondImageMinecraft.png'),
            'iron': tk.PhotoImage(file='assets/images/ironImageMinecraft.png'),
            'emerald': tk.PhotoImage(file='assets/images/emeraldImageMinecraft.png'),
            'gold': tk.PhotoImage(file='assets/images/goldImageMinecraft.png'),
            'copper': tk.PhotoImage(file='assets/images/copperImageMinecraft.png'),
            'redstone': tk.PhotoImage(file='assets/images/redstoneImageMinecraft.png'),
            'lapis': tk.PhotoImage(file='assets/images/lapisImageMinecraft.png'),
            #Deepslate Ores:
            'deepslateEmerald': tk.PhotoImage(file='assets/images/deepslateEmeraldImageMinecraft.png'),
            'deepslateCoal': tk.PhotoImage(file='assets/images/deepslateCoalImageMinecraft.png'),
            'deepslateDiamond': tk.PhotoImage(file='assets/images/deepslateDiamondImageMinecraft.png'),
            'deepslateGold': tk.PhotoImage(file='assets/images/deepslateGoldImageMinecraft.png'),
            'deepslateIron': tk.PhotoImage(file='assets/images/deepslateIronImageMinecraft.png'),
            'deepslateLapis': tk.PhotoImage(file='assets/images/deepslateLapisImageMinecraft.png'),
            'deepslateRedstone': tk.PhotoImage(file='assets/images/deepslateRedstoneImageMinecraft.png'),
            'deepslateCopper': tk.PhotoImage(file='assets/images/deepslateCopperImageMinecraft.png'),
            #Nether Ores:
            'netherite': tk.PhotoImage(file='assets/images/netheriteImageMinecraft.png'),
            'netherGold': tk.PhotoImage(file='assets/images/netherGoldImageMinecraft.png'),
            'quartz': tk.PhotoImage(file='assets/images/quartzImageMinecraft.png'),
            #Pseudo-Ores:
            'amethyst': tk.PhotoImage(file='assets/images/amethystImageMinecraft.png'),
            'gildedBlackstone': tk.PhotoImage(file='assets/images/gildedBlackstoneImageMinecraft.png'),
            #Un-Added:
            'poisonousPotato': tk.PhotoImage(file='assets/images/poisonousPotatoImageMinecraft.png'),
            'deepslatePoisonousPotato': tk.PhotoImage(file='assets/images/deepslatePoisonousPotatoImageMinecraft.png'),
            'glowstone': tk.PhotoImage(file='assets/images/glowstoneImageMinecraft.png')
            }



def startGame():
    global intro, startB
    intro.pack_forget()
    startB.pack_forget()
    nextRound()

def dimensionSwitch():
    global dimensionPickB, upgradeInv
    if upgradeInv['dim pick'][1] == 'o':
        dimensionPickB.configure(text='Next Dimension:\nNether', bg='#723232', fg="#3f1818")
        upgradeInv['dim pick'][1] = 'n'
    elif upgradeInv['dim pick'][1] == 'n':
        if upgradeInv['ext dim']:
            dimensionPickB.configure(text='Next Dimension:\nEnd', bg="#c8bf73", fg="#626047")
            upgradeInv['dim pick'][1] = 'e'
        else:
            dimensionPickB.configure(text='Next Dimension:\nOverworld', bg="#2a782a", fg="#0E2407")
            upgradeInv['dim pick'][1] = 'o'
    elif upgradeInv['dim pick'][1] == 'e':
        dimensionPickB.configure(text='Next Dimension:\nOverworld', bg="#2a782a", fg="#0E2407")
        upgradeInv['dim pick'][1] = 'o'
    




def multiplierUpgrade(a):
    global multiplier, score
    if score >= a*100:
        multiplier += a
        score -= 100*a
        nextRoundA()

def fortuneUpgrade(l,c):
    global upgradeInv, score
    if score >= c:
        upgradeInv['fortune'][0] = True
        upgradeInv['fortune'][1] = l
        score -= c
        nextRoundA()

def invUpgrade(t,c,m):
    global upgradeInv, score
    if score >= c:
        if m:
            upgradeInv[t][0] = True
        else:
            upgradeInv[t] = True
        score -= c
        nextRoundA()






def nextRoundA():
    global upgrades, dimensionPickB
    for _ in upgrades:
        _.grid_forget()

    if upgradeInv['dim pick'][0]:
        dimensionPickB.grid_forget()

    multButton.grid_forget()
    fortButton.grid_forget()

    nextRound()






def button_click(r,c,block):
    global start, score, nextTimer, blocksN, blocks, nextR
    if block != 'bedrock':
        check = ((((blocks[r+1][c] == 'air') or (blocks[r-1][c] == 'air')) or ((blocks[r][c+1] == 'air') or (blocks[r][c-1] == 'air'))) or (start and (block in ('endstone','stone','netherrack'))))
        check2 = ((blocks[r+1][c+1] == 'air') or (blocks[r-1][c-1] == 'air') or (blocks[r-1][c+1] == 'air') or (blocks[r+1][c-1] == 'air')) and upgradeInv['diag mine']
        if check or check2 or (start and upgradeInv['st free']):

            if upgradeInv['tnt start'] and start:
                start = False
                check = [[r-2,c-2],[r-2,c-1],[r-2,c],[r-2,c+1],[r-2,c+2],
                         [r-1,c-2],[r-1,c-1],[r-1,c],[r-1,c+1],[r-1,c+2],
                         [r,c-2],[r,c-1],[r,c],[r,c+1],[r,c+2],
                         [r+1,c-2],[r+1,c-1],[r+1,c],[r+1,c+1],[r+1,c+2],
                         [r+2,c-2],[r+2,c-1],[r+2,c],[r+2,c+1],[r+2,c+2]]
                for rr, cc in check:
                    block = blocksN[rr][cc]
                    if block not in ('bedrock','barrier','air'):
                        blocksN[rr][cc] = 'air'
                        blocks[rr][cc].grid_forget()
                        blocks[rr][cc] = 'air'
                        score += scoreAS(block,upgradeInv,multiplier,score)


            elif upgradeInv['tnt']:
                if start:
                    start = False
                check = [[r+1,c],[r-1,c],[r,c+1],[r,c-1],[r+1,c+1],[r-1,c-1],[r-1,c+1],[r+1,c-1],[r,c]]
                for rr, cc in check:
                    block = blocksN[rr][cc]
                    if block not in ('bedrock','barrier','air'):
                        blocksN[rr][cc] = 'air'
                        blocks[rr][cc].grid_forget()
                        blocks[rr][cc] = 'air'
                        score += scoreAS(block,upgradeInv,multiplier,score)


            else:
                blocks[r][c].grid_forget()
                blocks[r][c] = 'air'
                blocksN[r][c] = 'air'
                if start:
                    start = False
                score += scoreAS(block,upgradeInv,multiplier,score)

            blocks[15][0].configure(text=round(score,2))


    elif (r == 15) and (c == 1) and (nextTimer == 0):
        nextR = True








def nextRoundPre():
    root.configure(background='grey')

    for eachCol in blocks:

        for eachRow in eachCol:

            if (eachRow == 'air') or (eachRow == 'barrier'):
                continue

            eachRow.grid_forget()

    blocks[15][0].grid(row=15, column=0, sticky="nsew", padx=5, pady=5)
    blocks[15][0].configure(text=f'Score: {score}')
    multButton.configure(text=f'Multiplier: {multiplier}')
    multButton.grid(row=14,column=0, sticky="nsew", padx=5, pady=5)
    fortButton.configure(text=f'Fortune: {upgradeInv["fortune"][1]}%')
    fortButton.grid(row=13,column=0, sticky="nsew", padx=5, pady=5)

    nextShop()












def nextShop():
    global upgrades, upgradeInv, dimensionPickB

    upgrades = shopList(upgradeInv)

    if not upgradeInv["dim pick"][0]:
        upgrades.append('dim pick')
    else:
        dimensionPickB.grid(row=0, column=15)

    choices = []

    for _ in range(3):
        choiceExt = ran.randint(0,len(upgrades)-1)
        choice = upgrades[choiceExt]
        upgrades.pop(choiceExt)
        choices.append(choice)
    choices.append('skip')

    upgrades = choices

    for i, upg in enumerate(upgrades):
        upgrades[i] = buttonDef(upg, root, multiplierUpgrade, invUpgrade, nextRoundA, fortuneUpgrade)

        upgrades[i].grid(row=10, column=(i+1)*3, sticky="nsew", padx=5, pady=5)





def nextTime():
    global nextTimer
    nextTimer -= 1
    if nextTimer > 0:
        blocks[15][1].configure(text=f'Next (🔒 {nextTimer})')
        root.after(1000,nextTime)
    else:
        blocks[15][1].configure(text='Next')

def timeCount():
    global timer, nextR, start
    timer = round(timer-0.1,1)
    if timer > 0 and not nextR:
        blocks[15][2].configure(text=f'Time: {timer}')
        root.after(100,timeCount)
    else:
        if upgradeInv['time']:
            timer = 30
        else:
            timer = 15
        nextR = False
        start = True
        nextRoundPre()





def nextRound():
    global nextTimer, blocksN, blocks
    nextTimer = 5
    blocks = []
    blocksN = []
    dimension = dimensionR(upgradeInv, root)


    for r in range(16):
        root.grid_rowconfigure(r, weight=1)
        blocks.append([])
        blocksN.append([])

        for c in range(16):
            root.grid_columnconfigure(c, weight=1)

            if dimension == 'overworld':

                ore = oreO(upgradeInv)
                button, ore = defOreO(r,c,root,images,score,nextTimer,ore,button_click,timer)

                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)
                blocksN[r].append(ore)

            elif dimension == 'nether':

                ore = oreN(upgradeInv)
                button, ore = defOreN(r,c,root,images,score,nextTimer,ore,button_click,timer)

                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)
                blocksN[r].append(ore)

            elif dimension == 'end':

                button, ore = defOreE(r,c,root,images,score,nextTimer,button_click,timer)

                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)
                blocksN[r].append(ore)




        else:
            blocks[r].append('barrier')         # add barrier so c-1 and c+1 checks never cause index errors
            blocksN[r].append('barrier')
            blocks[r].append('barrier')         
            blocksN[r].append('barrier')

    else:
        blocks.append([])
        blocksN.append([])
        blocks.append([])
        blocksN.append([])
        for _ in range(18):
            blocks[16].append('barrier')
            blocksN[16].append('barrier')
            blocks[17].append('barrier')
            blocksN[17].append('barrier')


    root.after(1000,nextTime)
    root.after(100,timeCount)





intro.pack(pady=150)
startB.pack(pady=50)

root.mainloop()