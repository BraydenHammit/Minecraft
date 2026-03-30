import tkinter as tk

def close(TK,s,play):
    play(s,'click')
    TK.destroy()

def wrongStartBlock(root,sounds,play,dimension):
    master = tk.Toplevel(root)
    master.title("Pop-Up")
    ok = tk.Button(master,text='Ok', bg='gray85', command = lambda: close(master,sounds['click'],play))
    if dimension == 'overworld':
      label = tk.Label(master, text='Must Start on stone!')
    elif dimension == 'nether':
      label = tk.Label(master, text='Must Start on netherrack!')
    elif dimension == 'end':
      label = tk.Label(master, text='Must Start on endstone!')
    elif dimension == 'poisonous potato':
      label = tk.Label(master, text='Must Start on potone!')

    label.pack(pady=5)
    ok.pack(pady=5)

    root.wait_window(master)
