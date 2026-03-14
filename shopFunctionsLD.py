import tkinter as tk

def shopList(upgradeInv):
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

    if not upgradeInv["ore ext"]:
        upgrades.append('ore ext')

    if not upgradeInv["tnt"]:
        upgrades.append('tnt')



    return upgrades