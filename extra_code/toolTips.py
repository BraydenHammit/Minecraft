import tkinter as tk

class toolTip:
    def __init__(self, button, text):
        self.button = button
        self.text = text
        self.tooltip = None
        
        self.button.bind("<Enter>", self.show)
        self.button.bind("<Leave>", self.hide)

    def show(self, event=None):
        if self.tooltip or not self.text:
            return
        x = self.button.winfo_rootx() + 20
        y = self.button.winfo_rooty() + self.button.winfo_height() + 5
        self.tooltip = tk.Toplevel(self.button)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(self.tooltip, text=self.text, justify=tk.LEFT, background="#4A4A4A", relief=tk.SOLID, borderwidth=1, font=("ariel", "9", "normal"))
        label.pack(ipadx=4, ipady=2)

    def hide(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None