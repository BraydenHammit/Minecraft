import tkinter as tk

#Base Functions:
def close(TK,s,play,moon=False,u=None):
    if moon:
      u['moon'] = True
    if s != None:
      play(s,'click')
    TK.destroy()

def timeDown(button,TK,s,play,time,root):
   time -= 1
   if time <= 0:
    close(TK,s,play)
   else:
    try:
      button.configure(text=f'Ok ({time})')
      root.after(1000,lambda: timeDown(button,TK,s,play,time,root))
    except:
      close(TK,s,play)


#Incorrect Start Block:
def wrongStartBlock(root,sounds,play,dimension):
    master = tk.Toplevel(root)
    master.title("Pop-Up")
    master.geometry('200x100')
    time = 3
    ok = tk.Button(master,text=f'Ok ({time})', bg='gray85', command = lambda: close(master,sounds['click'],play))
    if dimension == 'overworld':
      label = tk.Label(master, text='Must Start on stone!')
    elif dimension == 'nether':
      label = tk.Label(master, text='Must Start on netherrack!')
    elif dimension == 'end':
      label = tk.Label(master, text='Must Start on endstone!')
    elif dimension == 'moon':
      label = tk.Label(master, text='Must Start on cheese!')
    elif dimension == 'poisonous potato':
      label = tk.Label(master, text='Must Start on potone!')

    label.pack(pady=5)
    ok.pack(pady=5)

    root.after(1000,lambda: timeDown(ok,master,None,play,time,root))
    root.wait_window(master)

#Shop Error:
def notAfford(root,sounds,play):
    master = tk.Toplevel(root)
    master.title("Pop-Up")
    master.geometry('200x100')
    time = 3
    ok = tk.Button(master,text=f'Ok ({time})', bg='gray85', command = lambda: close(master,sounds['click'],play))
    label = tk.Label(master, text='Not enough score!')

    label.pack(pady=5)
    ok.pack(pady=5)

    root.after(1000,lambda: timeDown(ok,master,None,play,time,root))
    root.wait_window(master)

#Moon Dimensiom:
def moonWindow(root,sounds,play,img,upgs):
    master = tk.Toplevel(root)
    master.title("Pop-Up")
    master.geometry('200x100')
    ok = tk.Button(master,text=f'Craft a Rocket', bg='gray85', command = lambda: close(master,sounds['click'],play,moon=True,u=upgs))
    craftTabel = tk.Label(master, image=img)

    craftTabel.pack(pady=5)
    ok.pack(pady=5)

    root.wait_window(master)