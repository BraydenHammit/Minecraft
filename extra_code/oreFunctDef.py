import tkinter as tk

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Overworld:
def defOreO(r,c,root,images,score,nextTimer,ore,button_click,timer,upgradeInv):
    if (r == 15):
        ore = 'bedrock'
        if c == 0:
            button = tk.Button(root, text=round(score,2), bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        elif c == 1:
            button = tk.Button(root, text=f'Next (🔒 {nextTimer})', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        elif c == 2:
            if upgradeInv['Xtime']:
                button = tk.Button(root, text='Time: ∞', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
            else:
                button = tk.Button(root, text=f'Time: {timer}', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
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

        elif ore == 'amethyst':
            button = tk.Button(root, image=images['amethyst'], bg='magenta', command=lambda r=r, c=c: button_click(r,c,'amethyst'))

        elif ore == 'poisonous potato':
            if r <= 8:
                button = tk.Button(root, image=images['poisonousPotato'], bg='gray55', command=lambda r=r, c=c: button_click(r,c,'poisonous potato'))
            else:
                button = tk.Button(root, image=images['deepslatePoisonousPotato'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'poisonous potato'))

    elif r <= 8:
        ore = 'stone'
        button = tk.Button(root, image=images['stone'], bg = 'gray55', command=lambda r=r, c=c: button_click(r,c,'stone'))
    else:
        ore = 'deepslate'
        button = tk.Button(root, image=images['deepslate'], bg = 'gray40', command=lambda r=r, c=c: button_click(r,c,'deepslate'))


    return button, ore

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Nether:
def defOreN(r,c,root,images,score,nextTimer,ore,button_click,timer,upgradeInv):
    if (r == 15) or (r == 0):
        ore = 'bedrock'
        if (c == 0) and (r == 15):
            button = tk.Button(root, text=round(score,2), bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        elif (c == 1) and (r == 15):
            button = tk.Button(root, text=f'Next (🔒 {nextTimer})', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        elif (r == 15) and (c == 2):
            if upgradeInv['Xtime']:
                button = tk.Button(root, text='Time: ∞', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
            else:
                button = tk.Button(root, text=f'Time: {timer}', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        else:
            button = tk.Button(root, image= images['bedrock'], bg = 'gray30', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
    elif ore != 'none':
        if ore == 'quartz':
            button = tk.Button(root, image = images['quartz'], bg='#723232', command=lambda r=r, c=c: button_click(r,c,'quartz'))
        elif ore == 'nether gold':
            button = tk.Button(root, image = images['netherGold'], bg='#723232', command=lambda r=r, c=c: button_click(r,c,'nether gold'))
        elif ore == 'netherite':
            button = tk.Button(root, image = images['netherite'], bg='#523933', command=lambda r=r, c=c: button_click(r,c,'netherite'))
        elif ore == 'gilded blackstone':
            button = tk.Button(root, image = images['gildedBlackstone'], bg='gray2', command=lambda r=r, c=c: button_click(r,c,'gilded blackstone'))
        elif ore == 'glowstone':
            button = tk.Button(root, image = images['glowstone'], bg='yellow', command=lambda r=r, c=c: button_click(r,c,'glowstone'))
    else:
        button = tk.Button(root, image = images['netherrack'], bg='#723232', command=lambda r=r, c=c: button_click(r,c,'netherrack'))
        ore = 'netherrack'

    
    return button, ore

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#End:
def defOreE(r,c,root,images,score,nextTimer,button_click,timer,upgradeInv):
    if (c == 0) and (r == 15):
        button = tk.Button(root, text=round(score,2), bg='#E0DE93', fg="#716F3D", command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    elif (c == 1) and (r == 15):
        button = tk.Button(root, text=f'Next (🔒 {nextTimer})', bg='#E0DE93', fg="#716F3D", command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    elif (r == 15) and (c == 2):
        if upgradeInv['Xtime']:
            button = tk.Button(root, text='Time: ∞', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        else:
            button = tk.Button(root, text=f'Time: {timer}', bg='gray30', fg='gray5', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    else:
        button = tk.Button(root, image = images['endstone'], bg='#E0DE93', command=lambda r=r, c=c: button_click(r,c,'endstone'))
        ore = 'endstone'

    
    return button, ore