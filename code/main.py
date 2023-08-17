import tkinter as tk
from tkinter import ttk
from argparse import Namespace
from gui import open_gui

import tkinter as tk
from tkinter import messagebox
from gui import open_gui

def on_button_click(annotation, autoimmunity, topology):
    # Esempio di cosa puoi fare con i parametri
    result = f"Annotation: {annotation}\nAutoimmunity: {autoimmunity}\nTopology: {topology}"
    messagebox.showinfo("Risultato", result)

root = tk.Tk()
root.title("Main")

# Apri la GUI e passa la funzione di callback
open_gui(root, on_button_click)

root.mainloop()


