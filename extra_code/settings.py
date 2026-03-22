import tkinter as tk

def close(TK):
    TK.destroy()

def openSettings(upgradeInv,settings):
    #Base Variables:
    master = tk.Tk()
    master.title("Settings")
    tntV = tk.BooleanVar(value=settings['tnt'])
    tntSV = tk.BooleanVar(value=settings['tnt start'])
    autoV = tk.BooleanVar(value=settings['auto mine'])
    ok = tk.Button(master,text='Ok', bg='gray85', command = lambda: close(master))
    label = tk.Label(master, text='None of your upgrades are togglable!')
    tnt = tk.Checkbutton(master, text="TNT Mining", variable=tntV)
    tntS = tk.Checkbutton(master, text="TNT Start", variable=tntSV)
    auto = tk.Checkbutton(master, text="Auto Mining", variable=autoV)
    if settings['tnt']:
        tnt.select()
    if settings['tnt start']:
        tntS.select()
    if settings['auto mine']:
        auto.select()

    if upgradeInv['tnt']:
        tnt.pack(pady=5)
    if upgradeInv['tnt start']:
        tntS.pack(pady=5)
    if upgradeInv['auto'][0]:
        auto.pack(pady=5)
    if not (upgradeInv['auto'][0] or upgradeInv['tnt start'] or upgradeInv['tnt']):
        label.pack(pady=5)
    ok.pack(pady=5)

    master.mainloop()

    settings = {
        'tnt': tntV.get(),
        'tnt start': tntSV.get(),
        'auto mine': autoV.get()
    }

    return settings