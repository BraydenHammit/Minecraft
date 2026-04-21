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
            button = tk.Button(root, image=images['amethyst'], bg='#9966CC', command=lambda r=r, c=c: button_click(r,c,'amethyst'))

        elif ore == 'poisonous potato':
            if r <= 8:
                button = tk.Button(root, image=images['poisonousPotato'], bg='gray55', command=lambda r=r, c=c: button_click(r,c,'poisonous potato'))
            else:
                button = tk.Button(root, image=images['deepslatePoisonousPotato'], bg='gray40', command=lambda r=r, c=c: button_click(r,c,'poisonous potato'))
        
        elif ore == 'ruby':
            button = tk.Button(root, image=images['ruby'], bg='gray55', command=lambda r=r, c=c: button_click(r,c,'ruby'))

    elif r <= 8:
        ore = 'stone'
        button = tk.Button(root, image=images['stone'], bg = 'gray55', command=lambda r=r, c=c: button_click(r,c,'stone'))
    else:
        ore = 'deepslate'
        button = tk.Button(root, image=images['deepslate'], bg = 'gray40', command=lambda r=r, c=c: button_click(r,c,'deepslate'))

    if (upgradeInv['effic']) and (ore != 'bedrock'):
        button.bind('<Enter>', lambda event, r=r, c=c: button_click(r,c,ore,effic=True))

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
            button = tk.Button(root, image = images['glowstone'], bg='#FFF59D', command=lambda r=r, c=c: button_click(r,c,'glowstone'))
    else:
        button = tk.Button(root, image = images['netherrack'], bg='#723232', command=lambda r=r, c=c: button_click(r,c,'netherrack'))
        ore = 'netherrack'

    if (upgradeInv['effic']) and (ore != 'bedrock'):
        button.bind('<Enter>', lambda event, r=r, c=c: button_click(r,c,ore,effic=True))
    
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
            button = tk.Button(root, text='Time: ∞', bg='#E0DE93', fg='#716F3D', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        else:
            button = tk.Button(root, text=f'Time: {timer}', bg='#E0DE93', fg='#716F3D', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    elif (c == 15) and (r == 15) and not upgradeInv['bedr'][1]:
        button = tk.Button(root, image = images['enderChest'], bg='#E0DE93', command=lambda r=r, c=c: button_click(r,c,'ender chest'))
        ore = 'ender chest'
    elif (c == 14) and (r == 15) and not upgradeInv['ruby'][1]:
        button = tk.Button(root, image = images['trappedChest'], bg='#E0DE93', command=lambda r=r, c=c: button_click(r,c,'trapped chest'))
        ore = 'trapped chest'
    elif (c == 13) and (r == 15) and not upgradeInv['unl mine'][1]:
        button = tk.Button(root, image = images['chest'], bg='#E0DE93', command=lambda r=r, c=c: button_click(r,c,'chest'))
        ore = 'chest'
    else:
        button = tk.Button(root, image = images['endstone'], bg='#E0DE93', command=lambda r=r, c=c: button_click(r,c,'endstone'))
        ore = 'endstone'

    if (upgradeInv['effic']) and (ore != 'bedrock'):
        button.bind('<Enter>', lambda event, r=r, c=c: button_click(r,c,ore,effic=True))

    return button, ore

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Poisonous Potato:
def defOreP(r,c,root,images,score,nextTimer,ore,button_click,timer,upgradeInv):
    if (c == 0) and (r == 15):
        button = tk.Button(root, text=round(score,2), bg='#965628', fg="#592D0E", command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    elif (c == 1) and (r == 15):
        button = tk.Button(root, text=f'Next (🔒 {nextTimer})', bg="#965628", fg="#592D0E", command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    elif (r == 15) and (c == 2):
        if upgradeInv['Xtime']:
            button = tk.Button(root, text='Time: ∞', bg='#965628', fg='#592D0E', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        else:
            button = tk.Button(root, text=f'Time: {timer}', bg='#965628', fg='#592D0E', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    elif ore != 'none':
        if ore == 'resin':
            button = tk.Button(root, image = images['resin'], bg="#965628", command=lambda r=r, c=c: button_click(r,c,'resin'))
        elif ore == 'lapis':
            button = tk.Button(root, image = images['potoneLapis'], bg="#965628", command=lambda r=r, c=c: button_click(r,c,'lapis'))
        elif ore == 'diamond':
            button = tk.Button(root, image = images['potoneDiamond'], bg="#965628", command=lambda r=r, c=c: button_click(r,c,'diamond'))
        elif ore == 'iron':
            button = tk.Button(root, image = images['potoneIron'], bg="#965628", command=lambda r=r, c=c: button_click(r,c,'iron'))
        elif ore == 'gold':
            button = tk.Button(root, image = images['potoneGold'], bg="#965628", command=lambda r=r, c=c: button_click(r,c,'gold'))
        elif ore == 'copper':
            button = tk.Button(root, image = images['potoneCopper'], bg="#965628", command=lambda r=r, c=c: button_click(r,c,'copper'))
        elif ore == 'redstone':
            button = tk.Button(root, image = images['potoneRedstone'], bg="#965628", command=lambda r=r, c=c: button_click(r,c,'redstone'))
        
    else:
        button = tk.Button(root, image = images['potone'], bg="#965628", command=lambda r=r, c=c: button_click(r,c,'potone'))
        ore = 'potone'

    if (upgradeInv['effic']) and (ore != 'bedrock'):
        button.bind('<Enter>', lambda event, r=r, c=c: button_click(r,c,ore,effic=True))
    
    return button, ore

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Moon:
def defOreM(r,c,root,images,score,nextTimer,button_click,timer,upgradeInv):
    if (c == 0) and (r == 15):
        button = tk.Button(root, text=round(score,2), bg='#fbf8d5', fg="#8c8a77", command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    elif (c == 1) and (r == 15):
        button = tk.Button(root, text=f'Next (🔒 {nextTimer})', bg='#fbf8d5', fg="#8c8a77", command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    elif (r == 15) and (c == 2):
        if upgradeInv['Xtime']:
            button = tk.Button(root, text='Time: ∞', bg='#fbf8d5', fg='#8c8a77', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        else:
            button = tk.Button(root, text=f'Time: {timer}', bg='#fbf8d5', fg='#8c8a77', command=lambda r=r, c=c: button_click(r,c,'bedrock'))
        ore = 'bedrock'
    else:
        button = tk.Button(root, image = images['cheese'], bg='#fbf8d5', command=lambda r=r, c=c: button_click(r,c,'cheese'))
        ore = 'cheese'

    if (upgradeInv['effic']) and (ore != 'bedrock'):
        button.bind('<Enter>', lambda event, r=r, c=c: button_click(r,c,ore,effic=True))

    return button, ore