import tkinter as tk
import random as ran

start = True
score = 0
multiplier = 1
blocks = []

root = tk.Tk()
root.title("Minecraft")
root.geometry('10000x100000')

stoneImage = tk.PhotoImage(file='assets/images/stoneImageMinecraft.png')
deepslateImage = tk.PhotoImage(file='assets/images/deepslateImageMinecraft.png')
bedrockImage = tk.PhotoImage(file='assets/images/bedrockImageMinecraft.png')
netherackImage = tk.PhotoImage(file='assets/images/netherackImageMinecraft.png')


def button_click(r,c,block):
    global start
    global score
    print('Block clicked:',block)
    print(f'Row: {r} \nCol: {c}')
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
        blocks[15][0] = tk.Button(root, text=score, bg='dark slate gray', fg='slate gray', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        blocks[15][0].grid_forget
        blocks[15][0].grid(row=15, column=0, sticky="nsew", padx=5, pady=5)
    print(f'Score: {score}')
    if (r == 15) and (c == 1):
        start = True
        nextRoundPre()



def nextRoundPre():
    global blocks
    print('Next Round Pre')

    for eachCol in blocks:

        for eachRow in eachCol:

            if (eachRow == 'air') or (eachRow == 'barrier'):
                continue

            eachRow.grid_forget()

    print(blocks)
    blocks = []

    nextShop()




def nextShop():
    #add options to buy upgrades like multipliers and ____
    nextRound()




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
                        if randomNum <= 11:
                            ore = 'redstone'
                            if randomNum <= 8:
                                ore = 'lapis'
                                if randomNum <= 5:
                                    ore = 'iron'
                                    if randomNum <= 2:
                                        ore = 'gold'
                                        if randomNum <= 1:
                                            ore = 'diamond'
                                            if randomNum == 0:
                                                ore = 'emerald'
                else:
                    ore = 'none'


                if (r == 15):
                    if c == 0:
                        button = tk.Button(root, text=score, bg='dark slate gray', fg='slate gray', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    elif c == 1:
                        button = tk.Button(root, text='Next', bg='dark slate gray', fg='slate gray', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    else:
                        button = tk.Button(root, image=bedrockImage, bg='gray30', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                elif ore != 'none':
                    if ore == 'diamond':
                        button = tk.Button(root, text="", bg='cyan', fg='cyan', command=lambda r=r, c=c: button_click(r,c,'diamond'))
                    elif ore == 'gold':
                        button = tk.Button(root, text="", bg='yellow', fg='yellow', command=lambda r=r, c=c: button_click(r,c,'gold'))
                    elif ore == 'emerald':
                        button = tk.Button(root, text="", bg='lime', fg='lime', command=lambda r=r, c=c: button_click(r,c,'emerald'))
                    elif ore == 'coal':
                        button = tk.Button(root, text="", bg='black', fg='black', command=lambda r=r, c=c: button_click(r,c,'coal'))
                    elif ore == 'lapis':
                        button = tk.Button(root, text="", bg='blue', fg='blue', command=lambda r=r, c=c: button_click(r,c,'lapis'))
                    elif ore == 'copper':
                        button = tk.Button(root, text="", bg='dark orange', fg='dark orange', command=lambda r=r, c=c: button_click(r,c,'copper'))
                    elif ore == 'iron':
                        button = tk.Button(root, text="", bg='tan', fg='tan', command=lambda r=r, c=c: button_click(r,c,'iron'))
                    elif ore == 'redstone':
                        button = tk.Button(root, text="", bg='red', fg='red', command=lambda r=r, c=c: button_click(r,c,'redstone'))
                elif r <= 8:
                    button = tk.Button(root, image=stoneImage, bg = 'gray70', command=lambda r=r, c=c: button_click(r,c,'stone'))
                else:
                    button = tk.Button(root, image=deepslateImage, bg = 'gray', command=lambda r=r, c=c: button_click(r,c,'deepslate'))
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)


            elif dimension == 'nether':
                root.configure(background='red')


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
                        button = tk.Button(root, text=score, bg='dark slate gray', fg='slate gray', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    elif (c == 1) and (r == 15):
                        button = tk.Button(root, text='Next', bg='dark slate gray', fg='slate gray', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                    else:
                        button = tk.Button(root, image=bedrockImage, bg = 'gray30', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
                elif ore != 'none':
                    if ore == 'quartz':
                        button = tk.Button(root, text="", bg='white', fg='white', command=lambda r=r, c=c: button_click(r,c,'quartz'))
                    elif ore == 'nether gold':
                        button = tk.Button(root, text="", bg='yellow', fg='yellow', command=lambda r=r, c=c: button_click(r,c,'nether gold'))
                    elif ore == 'netherite':
                        button = tk.Button(root, text="", bg='saddle brown', fg='saddle brown', command=lambda r=r, c=c: button_click(r,c,'netherite'))
                else:
                    button = tk.Button(root, image = netherackImage, bg='#723232', command=lambda r=r, c=c: button_click(r,c,'netherack'))
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
                blocks[r].append(button)


        else:
            blocks[r].append('barrier')

nextRound()

root.mainloop()