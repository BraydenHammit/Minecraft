import tkinter as tk

def close(TK,s,play):
    play(s,'click')
    TK.destroy()

def openSettings(upgradeInv,settings,root,sounds,play):
    master = tk.Toplevel(root)
    master.title("Settings")
    tntV = tk.BooleanVar(value=settings['tnt'])
    tntSV = tk.BooleanVar(value=settings['tnt start'])
    autoV = tk.BooleanVar(value=settings['auto mine'])
    efficV = tk.BooleanVar(value=settings['effic'])
    ok = tk.Button(master,text='Ok', bg='gray85', command = lambda: close(master,sounds['click'],play))
    label = tk.Label(master, text='None of your upgrades are togglable!')
    tnt = tk.Checkbutton(master, text="TNT Mining", variable=tntV)
    tntS = tk.Checkbutton(master, text="TNT Start", variable=tntSV)
    auto = tk.Checkbutton(master, text="Auto Mining", variable=autoV)
    effic = tk.Checkbutton(master, text="Efficiency", variable=efficV)
    if settings['tnt']:
        tnt.select()
    if settings['tnt start']:
        tntS.select()
    if settings['auto mine']:
        auto.select()
    if settings['effic']:
        effic.select()

    if upgradeInv['tnt']:
        tnt.pack(pady=5)
    if upgradeInv['tnt start']:
        tntS.pack(pady=5)
    if upgradeInv['auto'][0]:
        auto.pack(pady=5)
    if upgradeInv['effic']:
        effic.pack(pady=5)
    if not (upgradeInv['auto'][0] or upgradeInv['tnt start'] or upgradeInv['tnt'] or upgradeInv['effic']):
        label.pack(pady=5)
    ok.pack(pady=5)

    root.wait_window(master)

    settings = {
        'tnt': tntV.get(),
        'tnt start': tntSV.get(),
        'auto mine': autoV.get(),
        'effic': efficV.get()
    }

    return settings