import tkinter as tk

def viewInventory(multiplier,fortune,upgradeInv,score,end=False):
    #Base Variables:
    master = tk.Tk()
    if end:
        master.title("Final Stats:")
    else:
        master.title("Current Stats:")
    texT = f'Score: {score}\n\nUpgrades:\nMultiplier: x{multiplier}\nFortune: {upgradeInv["fortune"][1]}% for x{fortune}'
    missing_upg = 0
    missing_secrets = 0




    #Upgrade Checks:
    if upgradeInv["penalty s"]:
        texT += ('\nStone Penalty Removal')
    else:
        missing_upg += 1
    if upgradeInv["penalty s+"]:
        texT += ('\nPositive Score for Mining Stone')
    else:
        missing_upg += 1
    if upgradeInv["penalty n"]:
        texT += ('\nNetherrack Penalty Removal')
    else:
        missing_upg += 1
    if upgradeInv["penalty n+"]:
        texT += ('\nPositive Score for Mining Netherrack')
    else:
        missing_upg += 1
    if upgradeInv["penalty d"]:
        texT += ('\nDeepslate Penalty Removal')
    else:
        missing_upg += 1
    if upgradeInv["penalty d+"]:
        texT += ('\nPositive Score for Mining Deepslate')
    else:
        missing_upg += 1
    if upgradeInv['penalty e']:
        texT += ('\nEndstone Penalty Removal')
    else:
        missing_upg += 1
    if upgradeInv['penalty e+']:
        texT += ('\nPositive Score for Mining Endstone')
    else:
        missing_upg += 1

    if upgradeInv["luck"]:
        texT += ('\nOre Spawns Increase')
    else:
        missing_upg += 1
    if upgradeInv['luckM']:
        texT += ('\nSecond Ore Spawns Increase')
    else:
        missing_upg += 1

    if upgradeInv["st free"]:
        texT += ('\nStart Mining Freely')
    else:
        missing_upg += 1

    if upgradeInv["diag mine"]:
        texT += ('\nDiagonal Mining')
    else:
        missing_upg += 1
    if upgradeInv["unl mine"]:
        texT += ('\nRemoval of Neccesity of Nearby Air to Mine')
    else:
        missing_upg += 1

    if upgradeInv["auto"][0]:
        texT += ('\nAutomatic Mining')
    else:
        missing_upg += 1

    if upgradeInv["ore ext"]:
        texT += ('\nAllow Pseudo Ore Spawning')
    
    if upgradeInv["time"]:
        texT += ('\nTime Per Round Increase')
    else:
        missing_upg += 1
    if upgradeInv['Xtime']:
        texT += ('\nInfinite Time Per Round')
    else:
        missing_upg += 1
    if upgradeInv["ins nex"]:
        texT += ("\nRemoval of 5-Second Lock on 'Next' Button")
    else:
        missing_upg += 1

    if upgradeInv["tnt"]:
        texT += ('\n3x3 TNT Blast Mining')
    else:
        missing_upg += 1
    if upgradeInv["tnt start"]:
        texT += ('\nStart Round With 5x5 TNT Blast')
    else:
        missing_upg += 1

    if upgradeInv['ext dim']:
        texT += ('\nUnlocked End Dimension')
    else:
        missing_upg += 1

    if upgradeInv["dim pick"][0]:
        texT += ('\nSelect Next Dimension Button')
    else:
        missing_upg += 1
    if upgradeInv["upg re"]:
        texT += ('\nReroll Upgrades Button')
    else:
        missing_upg += 1
    if upgradeInv["stat view"]:
        texT += ('\nStat and Upgrades Viewing Button')
    else:
        missing_upg += 1
    
    if fortune != 3:
        missing_upg += 1
    if upgradeInv['fortune'][1] == 0:
        missing_upg += 4
    elif upgradeInv['fortune'][1] == 25:
        missing_upg += 3
    elif upgradeInv['fortune'][1] == 50:
        missing_upg += 2
    elif upgradeInv['fortune'][1] == 75:
        missing_upg += 1

    texT += f'\n\nMissing Upgrades: {missing_upg}'




    #Secret Checks:
    secrets = []
    if upgradeInv['potato']:
        secrets.append('\nPoisonous Potato Ore')
    else:
        missing_secrets += 1
    
    if upgradeInv['🏆'][0]:
        secrets.append('\nHidden Trophy (for Mining Poisonous Potato Ore)')
    else:
        missing_secrets += 1
    if upgradeInv['penalty p']:
        secrets.append('\nPotone Penalty Removal')
    else:
        missing_secrets += 1
    if upgradeInv['penalty p+']:
        secrets.append('\nPositive Score for Mining Potone')
    else:
        missing_secrets += 1

    if len(secrets) > 0:
        texT += '\n\nSecrets:'
        for secret in secrets:
            texT += secret

    texT += f'\n\nMissing Secrets: {missing_secrets}'



    
    #Open/Start Window:
    text = tk.Label(master, text=texT)
    text.pack(pady=5,padx=5)

    master.mainloop()