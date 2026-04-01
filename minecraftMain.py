#Imports:
import tkinter as tk
import random as ran
import subprocess as sp
import platform as plt
from tkinter import scrolledtext as st
from extra_code.scoreFunction import scoreAS, HOS
from extra_code.shopFunctions import shopList, buttonDef
from extra_code.oreFunct import oreO, oreN, oreP
from extra_code.oreFunctDef import defOreN, defOreO, defOreE, defOreP
from extra_code.dimFuncts import dimensionR, dimButton
from extra_code.invView import viewInventory
from extra_code.popups import wrongStartBlock, notAfford
from extra_code.settings import openSettings
from extra_code.introText import intro

#Variables:
if plt.system() == 'Darwin':
    sys = 'm' #MacBook
elif plt.system() == 'Windows':
    sys = 'w' #Windows
else:
    sys = 'o' #Other
start = True
nextR = False
score = 0
multiplier = 1
fortune = 1
nextTimer = 5
timer = 15
attemptedBedrock = 0
failedUpg = 0
aMine = None
nextLock = None
timerAfter = None
blocks = []
blocksN = []
dimension = None

settings = {
    'tnt': True,
    'tnt start': True,
    'auto mine': True 
}

blockTypes = {
    'golden': ['gold','deepslate gold','potone gold','gilded blackstone','nether gold','glowstone'],
    'gemS': ['diamond','deepslate diamond','potone diamond','emerald','deepslate emerald', 'amethyst','ruby'],
    'gemD': ['lapis','deepslate lapis','potone lapis','quartz','resin'],
    'industrial': ['iron','deepslate iron','potone iron','coal','deepslate coal', 'copper','deepslate copper', 'potone copper','redstone','deepslate redstone', 'potone redstone'],
    'rock': ['stone','deepslate','potone','bedrock','endstone','netherrack','netherite','glowstone'],
    'potato': ['potone','potone copper','potone gold','potone iron','potone redstone','potone lapis','potone diamond','resin','poisonous potato','deepslate poisonous potato']
}

blocksMined = {
            #Rocks:
            'stone': 0,
            'deepslate': 0,
            'bedrock': 0,
            'netherrack': 0,
            'endstone': 0,
            #Ores:
            'coal': 0,
            'diamond': 0,
            'iron': 0,
            'emerald': 0,
            'gold': 0,
            'copper': 0,
            'redstone': 0,
            'lapis': 0,
            #Deepslate Ores:
            'deepslate emerald': 0,
            'deepslate coal': 0,
            'deepslate diamond': 0,
            'deepslate gold': 0,
            'deepslate iron': 0,
            'deepslate lapis': 0,
            'deepslate redstone': 0,
            'deepslate copper': 0,
            #Nether Ores:
            'netherite': 0,
            'nether gold': 0,
            'quartz': 0,
            #Pseudo-Ores:
            'amethyst': 0,
            'gilded blackstone': 0,
            'glowstone': 0,
            #Hidden:
            'poisonous potato': 0,
            'deepslate poisonous potato': 0,
            'resin': 0,
            'potone diamond': 0,
            'potone iron': 0,
            'potone gold': 0,
            'potone copper': 0,
            'potone redstone': 0,
            'potone lapis': 0,
            'potone': 0,
            'ruby': 0
}

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
    #Block Type Bonuses:
    'gold bonus': False,
    'gemS bonus': False,
    'gemD bonus': False,
    'ind bonus': False,
    'rock bonus': False,
    #Luck:
    'luck': False,
    'luckM': False,
    'fortune': [False,0],
    'fortune x3': False,
    #Mining:
    'st free': False,
    'diag mine': False,
    'tnt': False,
    'tnt start': False,
    'auto': [False,False],
    'autoF': False,
    #Time:
    'time': False,
    'Xtime': False,
    'ins nex': False,
    #Extras:
    'ext dim': False,
    'ore ext': False,
    #Shop Buttons:
    'dim pick': [False,'r'],
    'upg re': False,
    'stat view': False,
    #Secret:
    'potato': False,
    '🏆': [False,None,False],
    'unl mine': [False,False,False],
    'bedr': [False,False,False],
    'ruby': [False,False,False],
    #Mini-Secret:
    'potato bonus': False,
    'penalty p': False,
    'penalty p+': False,
    'penalty b': False,
    'penalty b+': False
}

root = tk.Tk()
if ran.randrange(777) == 333:
    root.title("Minceraft")
else:
    root.title("Minecraft")
if sys != 'o':
    root.state('zoomed')
else: #Using codespace
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

scrollIntro = st.ScrolledText(root, wrap=tk.WORD, font = ("Comic Sans MS", 12), width=60, height=20, highlightthickness=2, highlightbackground="black", relief="flat")
intro = intro(blockTypes)
startB =  tk.Button(root, text = 'Start', bg='gray85', command= lambda: startGame())
key =  tk.Button(root, height=1, width=1, text = '🔑', bg='gray85', command= lambda: keyClick('o'))
keyE =  tk.Button(root, height=1, width=1, text = '🗝', bg='gray85', command= lambda: keyClick('e'))
keyN =  tk.Button(root, height=1, width=1, text = '❓', bg='gray85', command= lambda: keyClick('n'))
dimensionPickB = tk.Button(root, text='Next Dimension:\nRandom', bg="#942465", fg="#550A2A", command=lambda: dimensionSwitch())
upgReroll = tk.Button(root, text='Reroll Upgrades', bg='gray85', fg="gray5", command=lambda: nextShop(True))
multButton = tk.Button(root, text=f'Multiplier: x{multiplier}', bg='gray85', fg="gray5", command=lambda: button_click(1,0,'bedrock'))
fortButton = tk.Button(root, text=f'Fortune: {upgradeInv["fortune"][1]}% for x{fortune}', bg='gray85', fg="gray5", command=lambda: button_click(2,0,'bedrock'))
upgradeInv['🏆'][1] = tk.Button(root, text='Secret Trophy 🏆', bg='gray85', fg="gray5", command=lambda: trophyButton(sounds['level']))
settingsB = tk.Button(root, text='Settings', bg='gray85', fg="gray5", command=lambda: settingsButton(sounds['click']))

images = {
            #Unique:
            'commandBlock': tk.PhotoImage(file='assets/images/commandBlockImageMinecraft.png'),
            'icon': tk.PhotoImage(file='assets/images/iconImageMinecraft.png'),
            'iconI': 'assets/images/iconImageMinecraft.ico',
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
                #Poisonous Potato:
                'poisonousPotato': tk.PhotoImage(file='assets/images/poisonousPotatoImageMinecraft.png'),
                'deepslatePoisonousPotato': tk.PhotoImage(file='assets/images/deepslatePoisonousPotatoImageMinecraft.png'),
                'resin': tk.PhotoImage(file='assets/images/resinImageMinecraft.png'),
                'potoneDiamond': tk.PhotoImage(file='assets/images/potoneDiamondImageMinecraft.png'),
                'potoneIron': tk.PhotoImage(file='assets/images/potoneIronImageMinecraft.png'),
                'potoneGold': tk.PhotoImage(file='assets/images/potoneGoldImageMinecraft.png'),
                'potoneCopper': tk.PhotoImage(file='assets/images/potoneCopperImageMinecraft.png'),
                'potoneRedstone': tk.PhotoImage(file='assets/images/potoneRedstoneImageMinecraft.png'),
                'potoneLapis': tk.PhotoImage(file='assets/images/potoneLapisImageMinecraft.png'),
                'potone': tk.PhotoImage(file='assets/images/potoneImageMinecraft.png'),
                #Other:
                'chest': tk.PhotoImage(file='assets/images/chestImageMinecraft.png'),
                'enderChest': tk.PhotoImage(file='assets/images/enderChestImageMinecraft.png'),
                'trappedChest': tk.PhotoImage(file='assets/images/trappedChestImageMinecraft.png'),
                'cheese': tk.PhotoImage(file='assets/images/cheeseImageMinecraft.png'),
                'craftingTable': tk.PhotoImage(file='assets/images/craftingTableImageMinecraft.png'),
                'ruby': tk.PhotoImage(file='assets/images/rubyImageMinecraft.png')
            }

command = tk.Button(root, height=1, width=105, image=images['commandBlock'], bg="#e18a4c", command=lambda: commandButton(sounds['click']))
if sys == 'm':
    root.iconphoto(True, images['icon'])
elif sys == 'w':
    root.iconbitmap(images['iconI'])

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
    'relic': "assets/sounds/relic.wav",
    'pigstep': 'assets/sounds/pigstep.wav',
    'lava chicken': 'assets/sounds/lavaChicken.wav',
    'tears': "assets/sounds/tears.wav",
    'and action': "assets/sounds/andAction.wav",
    #Block-Break:
    'break block': 'assets/sounds/block_break.wav',
    'tnt': 'assets/sounds/tnt.wav',
    'xp': 'assets/sounds/xp.wav',
    'glass': 'assets/sounds/glass.wav',
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
    elif sys == 'm':
        soundsPlaying[t] = sp.Popen(["afplay", '-v', str(v), f])

def stopPlaying(t):
    if t:                     #if sound playing (t) has a value (is not None),
        t.terminate()         #terminate it (end the sound)
    t = None                  #sound stopped, so t is None


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Button Functions:
def startGame():
    scrollIntro.pack_forget()
    startB.destroy()
    stopPlaying(soundsPlaying['shopMusic'])
    play(sounds['click'],'click')
    nextRound()

def dimensionSwitch():
    global dimensionPickB, upgradeInv
    play(sounds['click'],'click')
    dimButton(upgradeInv,dimensionPickB)

def trophyButton(sound):
    play(sound,'click')
    HOS(upgradeInv)

def commandButton(sound):
    play(sound,'click')
    viewInventory(multiplier,fortune,upgradeInv,score,blocksMined,sounds,play)

def settingsButton(sound):
    global settings
    play(sound,'click')
    settings = openSettings(upgradeInv,settings,root,sounds,play)

def keyClick(t):
    global upgradeInv, key, keyE, keyN
    if t == 'o':
        upgradeInv['unl mine'][2] = True
        key.destroy()
    elif t == 'e':
        upgradeInv['bedr'][2] = True
        keyE.destroy()
    elif t == 'n':
        upgradeInv['ruby'][2] = True
        keyN.destroy()
    play(sounds['level'],'click')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Upgrade Functions:
def multiplierUpgrade(a):
    global multiplier, score, failedUpg
    if score >= a*500:
        multiplier += a
        score -= 500*a
        nextRoundA()
    else:
        play(sounds['break'],'click')
        notAfford(root,sounds,play)
        failedUpg += 1

def fortuneUpgrade(l,c):
    global upgradeInv, score, fortune, failedUpg
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
        notAfford(root,sounds,play)
        failedUpg += 1

def invUpgrade(t,c,m):
    global upgradeInv, score, timer, fortune,failedUpg
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
        notAfford(root,sounds,play)
        failedUpg += 1


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#After Shop Closes:
def nextRoundA():
    global upgrades, dimensionPickB, dimension
    for _ in upgrades:
        _.destroy()

    stopPlaying(soundsPlaying['shopMusic'])
    play(sounds['click'],'click')

    if upgradeInv['dim pick'][0]:
        dimensionPickB.grid_forget()
    if upgradeInv['upg re']:
        upgReroll.grid_forget()
    try:
        keyE.grid_forget()
    except:
        None
    try:
        key.grid_forget()
    except:
        None

    command.grid_forget()
    settingsB.grid_forget()
    multButton.grid_forget()
    fortButton.grid_forget()
    upgradeInv['🏆'][1].grid_forget()

    nextRound()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def button_click(r,c,block):
    global start, score, nextTimer, blocksN, blocks, nextR, upgradeInv, attemptedBedrock, blocksMined
    if (block not in ('ender chest','chest','trapped chest','air')) and (block != 'bedrock' or upgradeInv['bedr'][0]) and (not(r == 15 and c in (0,1,2))):
        check = ((blocks[r+1][c] == 'air') or (blocks[r-1][c] == 'air') or (blocks[r][c+1] == 'air') or (blocks[r][c-1] == 'air')) or (start and (block in ('endstone','stone','netherrack','potone')))
        check2 = ((blocks[r+1][c+1] == 'air') or (blocks[r-1][c-1] == 'air') or (blocks[r-1][c+1] == 'air') or (blocks[r+1][c-1] == 'air')) and upgradeInv['diag mine']
        if check or check2 or (start and upgradeInv['st free']) or (upgradeInv['unl mine'][0] and not start):

            if upgradeInv['bedr'][0] and block == 'bedrock':
                check = ((blocks[r+1][c] == 'air') or (blocks[r-1][c] == 'air') or (blocks[r][c+1] == 'air') or (blocks[r][c-1] == 'air')) or (start and (block in ('endstone','stone','netherrack','potone')))
                check2 = ((blocks[r+1][c+1] == 'air') or (blocks[r-1][c-1] == 'air') or (blocks[r-1][c+1] == 'air') or (blocks[r+1][c-1] == 'air')) and upgradeInv['diag mine']
                if check or check2 or (start and upgradeInv['st free']) or (upgradeInv['unl mine'][0] and not start):
                    if not isinstance(blocks[r][c], str):
                        blocks[r][c].destroy()
                    blocks[r][c] = 'air'
                    blocksN[r][c] = 'air'
                    start = False
                    score += scoreAS('bedrock',upgradeInv,multiplier,score,'bedrock',blockTypes)
                    play(sounds['glass'],'break block')
                    blocksMined['bedrock'] += 1

            elif (upgradeInv['tnt start'] and start) and settings['tnt start']:
                play(sounds['tnt'],'break block')
                start = False
                check = [[r-2,c-2],[r-2,c-1],[r-2,c],[r-2,c+1],[r-2,c+2],
                         [r-1,c-2],[r-1,c-1],[r-1,c],[r-1,c+1],[r-1,c+2],
                         [r,c-2],[r,c-1],[r,c],[r,c+1],[r,c+2],
                         [r+1,c-2],[r+1,c-1],[r+1,c],[r+1,c+1],[r+1,c+2],
                         [r+2,c-2],[r+2,c-1],[r+2,c],[r+2,c+1],[r+2,c+2]]
                for rr, cc in check:
                    block = blocksN[rr][cc]
                    if ('chest' not in block) and block not in ('bedrock','barrier','air'):
                        blocksN[rr][cc] = 'air'
                        if not isinstance(blocks[rr][cc], str):
                            blocks[rr][cc].destroy()
                        blocks[rr][cc] = 'air'
                        if block == 'poisonous potato':
                            upgradeInv['🏆'][2] = True
                        if rr >= 9 and dimension == 'overworld' and block not in ('bedrock','deepslate','amethyst'):
                            blockM = 'deepslate '+block
                        elif dimension == 'poisonous potato' and block not in ('potone','resin'):
                            blockM = 'potone '+block
                        else: 
                            blockM = block
                        blocksMined[blockM] += 1
                        score += scoreAS(block,upgradeInv,multiplier,score,blockM,blockTypes)
                        
                            


            elif upgradeInv['tnt'] and settings['tnt']:
                play(sounds['tnt'],'break block')
                start = False
                check = [[r+1,c-1], [r+1,c], [r+1,c+1],
                         [r,c-1],    [r,c],   [r,c+1],
                         [r-1,c-1], [r-1,c], [r-1,c+1]]
                for rr, cc in check:
                    block = blocksN[rr][cc]
                    if ('chest' not in block) and block not in ('bedrock','barrier','air'):
                        blocksN[rr][cc] = 'air'
                        if not isinstance(blocks[rr][cc], str):
                            blocks[rr][cc].destroy()
                        blocks[rr][cc] = 'air'
                        if block == 'poisonous potato':
                            upgradeInv['🏆'][2] = True
                        if rr >= 9 and dimension == 'overworld' and block not in ('bedrock','deepslate','amethyst'):
                            blockM = 'deepslate '+block
                        elif dimension == 'poisonous potato' and block not in ('potone','resin'):
                            blockM = 'potone '+block
                        else: 
                            blockM = block
                        blocksMined[blockM] += 1
                        score += scoreAS(block,upgradeInv,multiplier,score,blockM,blockTypes)
                        


            else:
                if not isinstance(blocks[r][c], str):
                    blocks[r][c].destroy()
                blocks[r][c] = 'air'
                blocksN[r][c] = 'air'
                start = False
                if block == 'poisonous potato':
                    upgradeInv['🏆'][2] = True
                if r >= 9 and dimension == 'overworld' and block not in ('bedrock','deepslate','amethyst'):
                    blockM = 'deepslate '+block
                elif dimension == 'poisonous potato' and block not in ('potone','resin'):
                    blockM = 'potone '+block
                else: 
                    blockM = block
                blocksMined[blockM] += 1
                if block in ('netherrack','stone','endstone','deepslate','potone'):
                    play(sounds['break block'],'break block')
                else:
                    play(sounds['xp'],'break block')
                score += scoreAS(block,upgradeInv,multiplier,score,blockM,blockTypes)

            blocks[15][0].configure(text=round(score,2))

        elif  block != 'bedrock' and start and (block not in ('stone','endstone','netherrack','potone')) and (not upgradeInv['st free']):
            wrongStartBlock(root,sounds,play,dimension)


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

    
    elif block == 'chest' and upgradeInv['unl mine'][2]:
        upgradeInv['unl mine'][1] = True
        blocks[r][c].configure(image = images['endstone'], bg='#E0DE93', command=lambda r=r, c=c: button_click(r,c,'endstone'))
        play(sounds['level'],'click')

    elif block == 'ender chest' and upgradeInv['bedr'][2]:
        upgradeInv['bedr'][1] = True
        blocks[r][c].configure(image = images['endstone'], bg='#E0DE93', command=lambda r=r, c=c: button_click(r,c,'endstone'))
        play(sounds['level'],'click')

    elif block == 'trapped chest' and upgradeInv['ruby'][2]:
        upgradeInv['ruby'][1] = True
        blocks[r][c].configure(image = images['endstone'], bg='#E0DE93', command=lambda r=r, c=c: button_click(r,c,'endstone'))
        play(sounds['level'],'click')

    else:
        if block == 'bedrock':
            attemptedBedrock += 1
        play(sounds['break'],'click')



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Shop Start-Up:
def nextRoundPre():
    global key, keyE, keyN
    root.configure(background='grey')

    stopPlaying(soundsPlaying['roundMusic'])

    for eachCol, val in enumerate(blocks):

        for eachRow, val in enumerate(val):

            if (val == 'air') or (val == 'barrier') or (eachRow == 0 and eachCol == 15):
                continue

            val.destroy()

    blocks[15][0].grid(row=15, column=0, sticky="nsew", padx=5, pady=5)
    blocks[15][0].configure(text=f'Score: {round(score,2)}',bg='gray85',fg='gray5')
    settingsB.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    multButton.configure(text=f'Multiplier: x{round(multiplier,2)}')
    multButton.grid(row=14,column=0, sticky="nsew", padx=5, pady=5)
    fortButton.configure(text=f'Fortune: {upgradeInv["fortune"][1]}% for x{fortune}')
    fortButton.grid(row=13,column=0, sticky="nsew", padx=5, pady=5)
    if failedUpg >= 37 and (not upgradeInv['unl mine'][2]) and upgradeInv['diag mine']:
        key.grid(row=15,column=15, sticky="nsew", padx=5, pady=5)
    if attemptedBedrock >= 73 and not upgradeInv['bedr'][2]:
        keyE.grid(row=15,column=15, sticky="nsew", padx=5, pady=5)
    if upgradeInv['🏆'][0]:
        upgradeInv['🏆'][1].grid(row=12,column=0, sticky="nsew", padx=5, pady=5)
    for k, v in blocksMined.items():
        if k != 'ruby' and v == 0:
            break
    else:
        if not upgradeInv['ruby'][2]:
            keyN.grid(row=15,column=15, sticky="nsew", padx=5, pady=5)

    nextShop(False)


def nextShop(r):
    global upgrades, dimensionPickB, command, upgReroll

    if r: #If Rerolling:
        play(sounds['click'],'click')
        for e in upgrades:
            e.destroy()
    else:   #1st Time In Shop (This Round):
        play(sounds[ran.choice(['subwoofer lullaby','aria math','mice on venus','minecraft','sweden'])],'shopMusic',v=2.5)

    upgrades = shopList(blocksMined,upgradeInv,dimensionPickB,upgReroll,command,r)

    
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
    global nextTimer, nextLock
    nextTimer -= 1
    if nextTimer > 0:
        blocks[15][1].configure(text=f'Next (🔒 {nextTimer})')
        nextLock = root.after(1000,nextTime)
    else:
        blocks[15][1].configure(text='Next')

def timeCount():
    global timer, nextR, start, timerAfter
    timer = round(timer-0.1,1)
    if timer > 0 and not nextR:
        blocks[15][2].configure(text=f'Time: {timer}')
        timerAfter = root.after(100,timeCount)
    else:
        if upgradeInv['time']:
            timer = 30
        else:
            timer = 15
        nextR = False
        start = True
        nextRoundPre()

def autoMine():
    global aMine
    if (not start) and settings['auto mine']:
        global blocks, blocksN, score
        check1, check2 = False, False
        valid = []
        num = len(blocks)
        for r in range(num):
            for c in range(num):
                if blocksN[r][c] not in ('bedrock','air','barrier','chest','ender chest','trapped chest'):
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
                if blockN not in ('bedrock','air','barrier','chest','ender chest','trapped chest'):
                    if not isinstance(block, str):
                        block.destroy()
                    blocks[r][c] = 'air'
                    blocksN[r][c] = 'air'
                    if blockN in ('netherrack','stone','endstone','deepslate','potone'):
                        play(sounds['break block'],'break block')
                    else:
                        play(sounds['xp'],'break block')
                    if blockN == 'poisonous potato':
                        upgradeInv['🏆'][2] = True
                    if r >= 9 and dimension == 'overworld' and blockN not in ('bedrock','deepslate','amethyst'):
                        blockM = 'deepslate '+blockN
                    elif dimension == 'poisonous potato' and blockN not in ('potone','resin'):
                        blockM = 'potone '+blockN
                    else: 
                        blockM = blockN
                    blocksMined[blockM] += 1
                    score += scoreAS(blockN,upgradeInv,multiplier,score,blockM)
                    blocks[15][0].configure(text=round(score,2))
    if upgradeInv['autoF']:
        aMine = root.after(250,autoMine)
    else:
        aMine = root.after(1000,autoMine)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Round Function:
def nextRound():
    global nextTimer, blocksN, blocks, aMine, timerAfter, nextLock, dimension
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
                ore = oreO(upgradeInv,r)
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
        timerAfter = root.after(100,timeCount)
    nextLock = root.after(1000,nextTime)
    if upgradeInv['auto'][0] and not upgradeInv['auto'][1]:    
        aMine = root.after(1000,autoMine)
        upgradeInv['auto'][1] = True

    #Start Round Music:
    if dimension == 'overworld':
        play(sounds[ran.choice(['precipice','otherside','relic'])],'roundMusic')
    elif dimension == 'nether':
        play(sounds[ran.choice(['pigstep','lava chicken'])],'roundMusic')
    elif dimension == 'end':
        play(sounds['tears'],'roundMusic',v=2)
    elif dimension == 'poisonous potato':
        play(sounds['and action'],'roundMusic',v=1.5)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Start/Open Window:
scrollIntro.pack(padx=30, pady=30)
scrollIntro.insert(tk.INSERT, intro)
scrollIntro.configure(state='disabled')
startB.pack(pady=10)
play(sounds[ran.choice(['subwoofer lullaby','aria math','mice on venus','minecraft','sweden'])],'shopMusic',v=2.5)
root.mainloop()


#After Window Closed:
stopPlaying(soundsPlaying['roundMusic'])
stopPlaying(soundsPlaying['shopMusic'])
stopPlaying(soundsPlaying['click'])
stopPlaying(soundsPlaying['break block'])
