import tkinter as tk

class toolTip:
    def __init__(self, button, text):
        self.button = button
        self.text = text
        self.tip_window = None
        
        self.button.bind("<Enter>", self.show)
        self.button.bind("<Leave>", self.hide)

    def show(self, event=None):
        if self.tip_window or not self.text:
            return
        x = self.button.winfo_rootx() + 20
        y = self.button.winfo_rooty() + self.button.winfo_height() + 5
        self.tip_window = tk.Toplevel(self.button)
        self.tip_window.wm_overrideredirect(True)
        self.tip_window.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(self.tip_window, text=self.text, justify=tk.LEFT, background="#4A4A4A", relief=tk.SOLID, borderwidth=1, font=("ariel", "9", "normal"))
        label.pack(ipadx=4, ipady=2)

    def hide(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None