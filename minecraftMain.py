#Imports:
import tkinter as tk
import random as ran
import subprocess as sp
import platform as plt
from extra_code.scoreFunction import scoreAS, HOS
from extra_code.shopFunctions import shopList, buttonDef
from extra_code.oreFunct import oreO, oreN, oreP
from extra_code.oreFunctDef import defOreN, defOreO, defOreE, defOreP
from extra_code.dimFuncts import dimensionR, dimButton

#Variables:
if plt.system() in ('Darwin','Linux'):
    sys = 'm/l'
elif plt.system() == 'Windows':
    sys = 'w'
start = True
nextR = False
score = 0
multiplier = 1
fortune = 1
nextTimer = 5
timer = 15
blocks = []
blocksN = []

upgradeInv = {
    #Penalties:
    'penalty n': False,
    'penalty s': False,
    'penalty d': False,
    'penalty e': False,
    'penalty n+': False,
    'penalty s+': False,
    'penalty d+': False,
    'penalty e+': False,
    #Luck:
    'luck': False,
    'luckM': False,
    'fortune': [False,0],
    'fortune x3': False,
    #Mining:
    'st free': False,
    'diag mine': False,
    'unl mine': False,
    'tnt': False,
    'tnt start': False,
    'auto': [False,False],
    #Time:
    'time': False,
    'Xtime': False,
    'ins nex': False,
    #Extras:
    'ext dim': False,
    'ore ext': False,
    #Shop Buttons:
    'dim pick': [False,'o'],
    'upg re': False,
    #Secret:
    'potato': False,
    '🏆': [False,None,False],
    'penalty p': False,
    'penalty p+': False,

}

root = tk.Tk()
root.title("Minecraft")
root.state('zoomed')

intro =  tk.Label(root, text="How to Play:\nYou must start by mining a stone or netherrack block.\nYou can only mine blocks next to blocks you've already mined.\nYou lose score for mining stone, deepslate, and netherrack.\nYour score is shown on the bottom left bedrock,\nand you can go to the next round by clicking 'Next' (next to score).\nYou only have 15 seconds each round (shown next to the 'Next' button),\nand when that runs out the round automaticlly ends.\nIn between rounds, you can buy upgrades by spending your score.\nThese upgrades can boost ore spawns, the amount of score you get per ore,\ngain the ability to select what dimension it will be next round (the button is in the shop),\nincrease your mining to a 3x3 area with an explosive blast, apply a fortune enchantment,\ngain the ability to start mining on things other than stone or netherrack,\nremove the score penalties when mining netherrack, stone, endstone, and deepslate,\nunlock the ability to mine diagonally (between blocks) from pre-mined blocks,\nunlock three extra ores (one Overwold, two Nether) or an extra dimension, and much more.\n\nRock Values:\nStone, Endstone, & Netherrack = -1\nDeepslate = -1.5\nBedrock = ???\n\nOre Values:\nCoal, Copper, & Nether Gold = 1.75\nRedstone & Lapis = 2.5\nIron, Gold, & Quartz = 3.25\nDiamond = 5\nEmerald & Netherite = 12.5\n\nExtra Semi-Ores:\nGlowstone = 5\nGilded Blackstone & Amethyst = 7.5")
startB =  tk.Button(root, text = 'Start', bg='gray85', command= lambda: startGame())
dimensionPickB = tk.Button(root, text='Next Dimension:\nOverworld', bg='#1f5f1f', fg="#0DAA0D", command=lambda: dimensionSwitch())
upgReroll = tk.Button(root, text='Reroll Upgrades', bg='gray30', fg="gray5", command=lambda: nextShop(True))
multButton = tk.Button(root, text=f'Multiplier: x{multiplier}', bg='gray30', fg="gray5", command=lambda: button_click(1,0,'bedrock'))
fortButton = tk.Button(root, text=f'Fortune: {upgradeInv["fortune"][1]}% for x{fortune}', bg='gray30', fg="gray5", command=lambda: button_click(2,0,'bedrock'))
upgradeInv['🏆'][1] = tk.Button(root, text='Secret Trophy 🏆', bg='gray30', fg="gray5", command=lambda: trophyButton())

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
            'glowstone': tk.PhotoImage(file='assets/images/glowstoneImageMinecraft.png'),
            #Secret:
            'poisonousPotato': tk.PhotoImage(file='assets/images/poisonousPotatoImageMinecraft.png'),
            'deepslatePoisonousPotato': tk.PhotoImage(file='assets/images/deepslatePoisonousPotatoImageMinecraft.png'),
            'resin': tk.PhotoImage(file='assets/images/resinImageMinecraft.png'),
            'potoneDiamond': tk.PhotoImage(file='assets/images/potoneDiamondImageMinecraft.png'),
            'potoneIron': tk.PhotoImage(file='assets/images/potoneIronImageMinecraft.png'),
            'potoneGold': tk.PhotoImage(file='assets/images/potoneGoldImageMinecraft.png'),
            'potoneCopper': tk.PhotoImage(file='assets/images/potoneCopperImageMinecraft.png'),
            'potoneRedstone': tk.PhotoImage(file='assets/images/potoneRedstoneImageMinecraft.png'),
            'potoneLapis': tk.PhotoImage(file='assets/images/potoneLapisImageMinecraft.png'),
            'potone': tk.PhotoImage(file='assets/images/potoneImageMinecraft.png')
            }

sounds = {
    #Shop Music:
    'subwoofer lullaby': 'assets/sounds/subwooferLullaby.wav',
    'mice on venus': 'assets/sounds/miceOnVenus.wav',
    'aria math': 'assets/sounds/ariaMath.wav',
    'minecraft': 'assets/sounds/minecraft.wav',
    'sweden': 'assets/sounds/sweden.wav',
    #Round Music:
    'precipice': 'assets/sounds/precipice.wav',
    'otherside': 'assets/sounds/otherside.wav',
    'pigstep': 'assets/sounds/pigstep.wav',
    'lava chicken': 'assets/sounds/lavaChicken.wav',
    'tears': "assets/sounds/tears.wav",
    #Block-Break:
    'break block': 'assets/sounds/block_break.wav',
    'tnt': 'assets/sounds/tnt.wav',
    'xp': 'assets/sounds/xp.wav',
    #Click:
    'click': 'assets/sounds/click.wav',
    'break': 'assets/sounds/decline.wav',
    'level': 'assets/sounds/levelUp.wav' 
}

soundsPlaying = {
    'break block': None,
    'shopMusic': None,
    'roundMusic': None,
    'click': None
}


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Sound Playing:
def play(f,t,v=1.0):
    global soundsPlaying
    if sys == 'w':
        soundsPlaying[t] = sp.Popen(["powershell","-c",f'(New-Object Media.SoundPlayer "{f}").PlaySync();'], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
    elif sys == 'm/l':
        soundsPlaying[t] = sp.Popen(["afplay", '-v', str(v), f])

def stopPlaying(t):
    if t:                     #if sound playing (t) has a value (is not None),
        t.terminate()         #terminate it (end the sound)
    t = None                  #sound stopped, so t is None


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Button Functions:
def startGame():
    intro.destroy()
    startB.destroy()
    stopPlaying(soundsPlaying['shopMusic'])
    play(sounds['click'],'click')
    nextRound()

def dimensionSwitch():
    global dimensionPickB, upgradeInv
    play(sounds['click'],'click')
    dimButton(upgradeInv,dimensionPickB)

def trophyButton():
    play(sounds['level'],'click')
    HOS()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Upgrade Functions:
def multiplierUpgrade(a):
    global multiplier, score
    if score >= a*100:
        multiplier += a
        score -= 100*a
        nextRoundA()
    else:
        play(sounds['break'],'click')

def fortuneUpgrade(l,c):
    global upgradeInv, score, fortune
    if score >= c:
        upgradeInv['fortune'][0] = True
        upgradeInv['fortune'][1] = l
        score -= c
        if  upgradeInv['fortune x3']:
            fortune = 3
        else:
            fortune = 2

        nextRoundA()
    else:
        play(sounds['break'],'click')

def invUpgrade(t,c,m):
    global upgradeInv, score, timer, fortune
    if score >= c:
        if m:
            upgradeInv[t][0] = True
        else:
            upgradeInv[t] = True
        score -= c
        if t == 'time':
            timer = 30
        if t == 'fortune x3':
            fortune = 3
        nextRoundA()
    else:
        play(sounds['break'],'click')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#After Shop Closes:
def nextRoundA():
    global upgrades, dimensionPickB
    for _ in upgrades:
        _.grid_forget()

    stopPlaying(soundsPlaying['shopMusic'])
    play(sounds['click'],'click')

    if upgradeInv['dim pick'][0]:
        dimensionPickB.grid_forget()
    if upgradeInv['upg re']:
        upgReroll.grid_forget()

    multButton.grid_forget()
    fortButton.grid_forget()
    upgradeInv['🏆'][1].grid_forget()

    nextRound()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def button_click(r,c,block):
    global start, score, nextTimer, blocksN, blocks, nextR, upgradeInv
    if block != 'bedrock':
        check = ((blocks[r+1][c] == 'air') or (blocks[r-1][c] == 'air') or (blocks[r][c+1] == 'air') or (blocks[r][c-1] == 'air')) or (start and (block in ('endstone','stone','netherrack','potone')))
        check2 = ((blocks[r+1][c+1] == 'air') or (blocks[r-1][c-1] == 'air') or (blocks[r-1][c+1] == 'air') or (blocks[r+1][c-1] == 'air')) and upgradeInv['diag mine']
        if check or check2 or (start and upgradeInv['st free']) or (upgradeInv['unl mine'] and not start):

            if upgradeInv['tnt start'] and start:
                play(sounds['tnt'],'break block')
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
                        if block == 'poisonous potato':
                            upgradeInv['🏆'][2] = True


            elif upgradeInv['tnt']:
                play(sounds['tnt'],'break block')
                start = False
                check = [[r+1,c-1], [r+1,c], [r+1,c+1],
                         [r,c-1],    [r,c],   [r,c+1],
                         [r-1,c-1], [r-1,c], [r-1,c+1]]
                for rr, cc in check:
                    block = blocksN[rr][cc]
                    if block not in ('bedrock','barrier','air'):
                        blocksN[rr][cc] = 'air'
                        blocks[rr][cc].grid_forget()
                        blocks[rr][cc] = 'air'
                        score += scoreAS(block,upgradeInv,multiplier,score)
                        if block == 'poisonous potato':
                            upgradeInv['🏆'][2] = True


            else:
                blocks[r][c].grid_forget()
                blocks[r][c] = 'air'
                blocksN[r][c] = 'air'
                start = False
                score += scoreAS(block,upgradeInv,multiplier,score)
                if block in ('netherrack','stone','endstone','deepslate'):
                    play(sounds['break block'],'break block')
                else:
                    play(sounds['xp'],'break block')
                if block == 'poisonous potato':
                    upgradeInv['🏆'][2] = True

            blocks[15][0].configure(text=round(score,2))


    elif (r == 15) and (c == 1):
        if(nextTimer <= 0):
            play(sounds['click'],'click')
            if upgradeInv['Xtime']:
                start = True
                nextRoundPre()
            else:
                nextR = True
        else:
            play(sounds['break'],'click')

    else:
            play(sounds['break'],'click')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Shop Start-Up:
def nextRoundPre():
    root.configure(background='grey')

    stopPlaying(soundsPlaying['roundMusic'])

    for eachCol in blocks:

        for eachRow in eachCol:

            if (eachRow == 'air') or (eachRow == 'barrier'):
                continue

            eachRow.grid_forget()

    blocks[15][0].grid(row=15, column=0, sticky="nsew", padx=5, pady=5)
    blocks[15][0].configure(text=f'Score: {score}',bg='gray30',fg='gray5')
    multButton.configure(text=f'Multiplier: x{multiplier}')
    multButton.grid(row=14,column=0, sticky="nsew", padx=5, pady=5)
    fortButton.configure(text=f'Fortune: {upgradeInv["fortune"][1]}% for x{fortune}')
    fortButton.grid(row=13,column=0, sticky="nsew", padx=5, pady=5)
    if upgradeInv['🏆'][0]:
        upgradeInv['🏆'][1].grid(row=12,column=0, sticky="nsew", padx=5, pady=5)

    nextShop(False)


def nextShop(r):
    global upgrades

    if r: #If Rerolling:
        play(sounds['click'],'click')
        for e in upgrades:
            e.grid_forget()
    else:   #1st Time In Shop (This Round):
        play(sounds[ran.choice(['subwoofer lullaby','aria math','mice on venus','minecraft','sweden'])],'shopMusic',v=2.5)

    upgrades = shopList(upgradeInv,dimensionPickB,upgReroll,r)

    
    #Pick Random Upgrades:
    choices = []
    for _ in range(3):
        choiceExt = ran.randint(0,len(upgrades)-1)
        choice = upgrades[choiceExt]
        upgrades.pop(choiceExt)         #remove choice so upgrade can only be shown once per shop
        choices.append(choice)
    if upgradeInv['🏆'][2] and not upgradeInv['🏆'][0]:
        choices.append('🏆')
    else:
        choices.append('skip')


    upgrades = choices
    for i, upg in enumerate(upgrades):
        upgrades[i] = buttonDef(upg, root, multiplierUpgrade, invUpgrade, nextRoundA, fortuneUpgrade)
        upgrades[i].grid(row=8, column=(i+1)*3, sticky="nsew", padx=5, pady=5)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Timer Functions:
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

def autoMine():
    if not start:
        global blocks, blocksN, score
        check1, check2 = False, False
        valid = []
        num = len(blocks)
        for r in range(num):
            for c in range(num):
                if blocksN[r][c] not in ('bedrock','air','barrier'):
                    check1 = (blocks[r+1][c] == 'air') or (blocks[r-1][c] == 'air') or (blocks[r][c+1] == 'air') or (blocks[r][c-1] == 'air')
                    check2 = ((blocks[r+1][c+1] == 'air') or (blocks[r-1][c-1] == 'air') or (blocks[r-1][c+1] == 'air') or (blocks[r+1][c-1] == 'air')) and upgradeInv['diag mine']
                    if (check1 or check2):
                        valid.append([r,c])

        else:
            if len(valid) > 0:
                r = ran.choice(valid)[0]
                c = ran.choice(valid)[1]
                blockN = blocksN[r][c]
                block = blocks[r][c]
                if blockN not in ('bedrock','air','barrier'):
                    block.grid_forget()
                    blocks[r][c] = 'air'
                    blocksN[r][c] = 'air'
                    score += scoreAS(blockN,upgradeInv,multiplier,score)
                    if blockN in ('netherrack','stone','endstone','deepslate'):
                        play(sounds['break block'],'break block')
                    else:
                        play(sounds['xp'],'break block')
                    if blockN == 'poisonous potato':
                        upgradeInv['🏆'][2] = True

    root.after(1000,autoMine)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Round Function:
def nextRound():
    global nextTimer, blocksN, blocks
    nextTimer = 5
    blocks = []
    blocksN = []
    dimension = dimensionR(upgradeInv, root)

    #Define+Grid Button Layout:
    for r in range(16):
        root.grid_rowconfigure(r, weight=1)
        blocks.append([])
        blocksN.append([])

        for c in range(16):
            root.grid_columnconfigure(c, weight=1)

            if dimension == 'overworld':
                ore = oreO(upgradeInv)
                button, ore = defOreO(r,c,root,images,score,nextTimer,ore,button_click,timer,upgradeInv)
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)
                blocksN[r].append(ore)


            elif dimension == 'nether':
                ore = oreN(upgradeInv)
                button, ore = defOreN(r,c,root,images,score,nextTimer,ore,button_click,timer,upgradeInv)
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)
                blocksN[r].append(ore)


            elif dimension == 'end':
                button, ore = defOreE(r,c,root,images,score,nextTimer,button_click,timer,upgradeInv)
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)
                blocksN[r].append(ore)
            
            elif dimension == 'poisonous potato':
                ore = oreP(upgradeInv)
                button, ore = defOreP(r,c,root,images,score,nextTimer,ore,button_click,timer,upgradeInv)
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)
                blocksN[r].append(ore)


        else:
            blocks[r].append('barrier')         # add barrier so c-1 and c+1 checks never cause index errors
            blocksN[r].append('barrier')
            blocks[r].append('barrier')         # add 2nd barrier so c-2 and c+2 tnt checks never cause index errors
            blocksN[r].append('barrier')

    else:
        blocks.append([])
        blocksN.append([])
        blocks.append([])
        blocksN.append([])
        for _ in range(18):
            blocks[16].append('barrier')      # add barrier so r-1 and r+1 tnt checks never cause index errors
            blocksN[16].append('barrier')
            blocks[17].append('barrier')        # add 2nd barrier so r-2 and r+2 tnt start checks never cause index errors
            blocksN[17].append('barrier')


    #Start Timers (Timer+Next):
    if upgradeInv['ins nex']:    
        nextTimer = 0
        blocks[15][1].configure(text='Next')
    if not upgradeInv['Xtime']:
        root.after(100,timeCount)
    root.after(1000,nextTime)
    if upgradeInv['auto'][0] and not upgradeInv['auto'][1]:    
        root.after(1000,autoMine)
        upgradeInv['auto'][1] = True

    #Start Round Music:
    if dimension == 'overworld':
        play(sounds[ran.choice(['precipice','otherside'])],'roundMusic')
    elif dimension == 'nether':
        play(sounds[ran.choice(['pigstep','lava chicken'])],'roundMusic')
    elif dimension == 'end':
        play(sounds['tears'],'roundMusic')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Start/Open Window:
intro.pack(pady=150)
startB.pack(pady=50)
play(sounds[ran.choice(['subwoofer lullaby','aria math','mice on venus','minecraft','sweden'])],'shopMusic',v=2.5)
root.mainloop()


#After Window Closed:
stopPlaying(soundsPlaying['roundMusic'])
stopPlaying(soundsPlaying['shopMusic'])
stopPlaying(soundsPlaying['click'])
stopPlaying(soundsPlaying['break block'])