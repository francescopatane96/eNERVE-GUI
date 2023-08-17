import tkinter as tk
from tkinter import ttk
from argparse import Namespace
from tkinter import filedialog

def browse_proteome1():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        proteome1_var.set(filename)

def browse_proteome2():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        proteome2_var.set(filename)

def open_gui(parent, callback):
    def button_click():
        
        annotation=annotation_var.get()
        autoimmunity=autoimmunity_var.get()
        topology=topology_var.get()
        e_value=e_value_var.get()
        minlength=minlength_var.get()
        mismatch=mismatch_var.get()
        mouse=mouse_var.get()
        proteome1=proteome1_var.get()
        proteome2=proteome2_var.get()
        padlimit=padlimit_var.get()
        razor=razor_var.get()
        antigenlimit=antigenlimit_var.get()
        loclimit=loclimit_var.get()
        min_loop_length=min_loop_length_var.get()
        select=select_var.get()
        substitution=substitution_var.get()
        transmem_doms_limit=transmem_doms_limit_var.get()
        antigen=antigen_var.get()
        working_dir=working_dir_var.get()
        NERVE_dir=NERVE_dir_var.get()
        iFeature_dir=iFeature_dir_var.get()
        DeepFri_dir=DeepFri_dir_var.get()
        epitopes=epitopes_var.get()
        mhci_length=mhci_length_var.get()
        mhcii_length=mhcii_length_var.get()
        mhci_overlap=mhci_overlap_var.get()
        mhcii_overlap=mhcii_overlap_var.get()
        epitope_percentile=epitope_percentile_var.get()
        
        callback(annotation)
   


    gui_window = tk.Toplevel(parent)
    gui_window.title("eNERVE v1.0")

    # Creazione di un frame per migliorare la disposizione
    frame = ttk.Frame(gui_window, padding=10)
    frame.pack()

    # Stili di testo
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 10))
    style.configure("TButton", font=("Helvetica", 10, "bold"), background="#007bff", foreground="white")

    # Dichiarazione delle variabili StringVar per ciascun argomento
    annotation_var = tk.StringVar()
    autoimmunity_var = tk.StringVar()
    topology_var = tk.StringVar()
    e_value_var = tk.DoubleVar()
    minlength_var = tk.IntVar()
    mismatch_var = tk.IntVar()
    mouse_var = tk.StringVar()
    proteome1_var = tk.StringVar()
    proteome2_var = tk.StringVar()
    padlimit_var = tk.DoubleVar()
    razor_var = tk.StringVar()
    antigenlimit_var = tk.DoubleVar()
    loclimit_var = tk.DoubleVar()
    min_loop_length_var = tk.IntVar()
    select_var = tk.StringVar()
    substitution_var = tk.IntVar()
    transmem_doms_limit_var = tk.IntVar()
    antigen_var = tk.StringVar()
    working_dir_var = tk.StringVar()
    NERVE_dir_var = tk.StringVar()
    iFeature_dir_var = tk.StringVar()
    DeepFri_dir_var = tk.StringVar()
    epitopes_var = tk.StringVar()
    mhci_length_var = tk.IntVar()
    mhcii_length_var = tk.IntVar()
    mhci_overlap_var = tk.IntVar()
    mhcii_overlap_var = tk.IntVar()
    epitope_percentile_var = tk.DoubleVar()


    # Creazione dei widget per i parametri
    ttk.Label(frame, text="Annotation:").grid(row=0, column=0, sticky="w")
    annotation_frame = ttk.Frame(frame)
    annotation_frame.grid(row=0, column=1, sticky="w")
    annotation_true = ttk.Radiobutton(annotation_frame, text="True", variable=annotation_var,   value="True")
    annotation_true.pack(side="left")
    annotation_false = ttk.Radiobutton(annotation_frame, text="False", variable=annotation_var, value="False")
    annotation_false.pack(side="left")

    ttk.Label(frame, text="Autoimmunity:").grid(row=1, column=0, sticky="w")
    autoimmunity_entry = ttk.Entry(frame, textvariable=autoimmunity_var)
    autoimmunity_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Topology:").grid(row=2, column=0, sticky="w")
    topology_entry = ttk.Entry(frame, textvariable=topology_var)
    topology_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="E-Value:").grid(row=3, column=0, sticky="w")
    e_value_entry = ttk.Entry(frame, textvariable=e_value_var)
    e_value_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Min Length:").grid(row=4, column=0, sticky="w")
    minlength_entry = ttk.Entry(frame, textvariable=minlength_var)
    minlength_entry.grid(row=4, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Mismatch:").grid(row=5, column=0, sticky="w")
    mismatch_entry = ttk.Entry(frame, textvariable=mismatch_var)
    mismatch_entry.grid(row=5, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Mouse:").grid(row=6, column=0, sticky="w")
    mouse_frame = ttk.Frame(frame)
    mouse_frame.grid(row=6, column=1, sticky="w")
    mouse_true = ttk.Radiobutton(mouse_frame, text="True", variable=mouse_var, value="True")
    mouse_true.pack(side="left")
    mouse_false = ttk.Radiobutton(mouse_frame, text="False", variable=mouse_var, value="False")
    mouse_false.pack(side="left")
    
    ttk.Label(frame, text="Proteome1:").grid(row=7, column=0, sticky="w")
    proteome1_entry = ttk.Entry(frame, textvariable=proteome1_var, state="readonly")
    proteome1_entry.grid(row=7, column=1, sticky="w", padx=10, pady=5)
    proteome1_browse_button = ttk.Button(frame, text="Browse", command=browse_proteome1)
    proteome1_browse_button.grid(row=7, column=2, sticky="w", padx=5)
    
    ttk.Label(frame, text="Proteome2:").grid(row=8, column=0, sticky="w")
    proteome2_entry = ttk.Entry(frame, textvariable=proteome2_var, state="readonly")
    proteome2_entry.grid(row=8, column=1, sticky="w", padx=10, pady=5)
    proteome2_browse_button = ttk.Button(frame, text="Browse", command=browse_proteome2)
    proteome2_browse_button.grid(row=8, column=2, sticky="w", padx=5)

    ttk.Label(frame, text="Pad Limit:").grid(row=9, column=0, sticky="w")
    padlimit_entry = ttk.Entry(frame, textvariable=padlimit_var)
    padlimit_entry.grid(row=9, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Razor:").grid(row=10, column=0, sticky="w")
    razor_frame = ttk.Frame(frame)
    razor_frame.grid(row=10, column=1, sticky="w")
    razor_true = ttk.Radiobutton(razor_frame, text="True", variable=razor_var, value="True")
    razor_true.pack(side="left")
    razor_false = ttk.Radiobutton(razor_frame, text="False", variable=razor_var, value="False")
    razor_false.pack(side="left")

    ttk.Label(frame, text="Antigen Limit:").grid(row=11, column=0, sticky="w")
    antigenlimit_entry = ttk.Entry(frame, textvariable=antigenlimit_var)
    antigenlimit_entry.grid(row=11, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Loc Limit:").grid(row=12, column=0, sticky="w")
    loclimit_entry = ttk.Entry(frame, textvariable=loclimit_var)
    loclimit_entry.grid(row=12, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Min Loop Length:").grid(row=13, column=0, sticky="w")
    min_loop_length_entry = ttk.Entry(frame, textvariable=min_loop_length_var)
    min_loop_length_entry.grid(row=13, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Select:").grid(row=14, column=0, sticky="w")
    select_frame = ttk.Frame(frame)
    select_frame.grid(row=14, column=1, sticky="w")
    select_true = ttk.Radiobutton(select_frame, text="True", variable=select_var, value="True")
    select_true.pack(side="left")
    select_false = ttk.Radiobutton(select_frame, text="False", variable=select_var, value="False")
    select_false.pack(side="left")

    ttk.Label(frame, text="Substitution:").grid(row=15, column=0, sticky="w")
    substitution_entry = ttk.Entry(frame, textvariable=substitution_var)
    substitution_entry.grid(row=15, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Transmem Doms Limit:").grid(row=16, column=0, sticky="w")
    transmem_doms_limit_entry = ttk.Entry(frame, textvariable=transmem_doms_limit_var)
    transmem_doms_limit_entry.grid(row=16, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Antigen:").grid(row=17, column=0, sticky="w")
    antigen_frame = ttk.Frame(frame)
    antigen_frame.grid(row=17, column=1, sticky="w")
    antigen_true = ttk.Radiobutton(antigen_frame, text="True", variable=antigen_var, value="True")
    antigen_true.pack(side="left")
    antigen_false = ttk.Radiobutton(antigen_frame, text="False", variable=antigen_var, value="False")
    antigen_false.pack(side="left")

    ttk.Label(frame, text="Working Dir:").grid(row=18, column=0, sticky="w")
    working_dir_entry = ttk.Entry(frame, textvariable=working_dir_var)
    working_dir_entry.grid(row=18, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="NERVE Dir:").grid(row=19, column=0, sticky="w")
    NERVE_dir_entry = ttk.Entry(frame, textvariable=NERVE_dir_var)
    NERVE_dir_entry.grid(row=19, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="iFeature Dir:").grid(row=20, column=0, sticky="w")
    iFeature_dir_entry = ttk.Entry(frame, textvariable=iFeature_dir_var)
    iFeature_dir_entry.grid(row=20, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="DeepFri Dir:").grid(row=21, column=0, sticky="w")
    DeepFri_dir_entry = ttk.Entry(frame, textvariable=DeepFri_dir_var)
    DeepFri_dir_entry.grid(row=21, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Epitopes:").grid(row=22, column=0, sticky="w")
    epitopes_frame = ttk.Frame(frame)
    epitopes_frame.grid(row=22, column=1, sticky="w")
    epitopes_true = ttk.Radiobutton(epitopes_frame, text="True", variable=epitopes_var, value="True")
    epitopes_true.pack(side="left")
    epitopes_false = ttk.Radiobutton(epitopes_frame, text="False", variable=epitopes_var, value="False")
    epitopes_false.pack(side="left")

    ttk.Label(frame, text="MHC I Length:").grid(row=23, column=0, sticky="w")
    mhci_length_entry = ttk.Entry(frame, textvariable=mhci_length_var)
    mhci_length_entry.grid(row=23, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="MHC II Length:").grid(row=24, column=0, sticky="w")
    mhcii_length_entry = ttk.Entry(frame, textvariable=mhcii_length_var)
    mhcii_length_entry.grid(row=24, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="MHC I Overlap:").grid(row=25, column=0, sticky="w")
    mhci_overlap_entry = ttk.Entry(frame, textvariable=mhci_overlap_var)
    mhci_overlap_entry.grid(row=25, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="MHC II Overlap:").grid(row=26, column=0, sticky="w")
    mhcii_overlap_entry = ttk.Entry(frame, textvariable=mhcii_overlap_var)
    mhcii_overlap_entry.grid(row=26, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(frame, text="Epitope Percentile:").grid(row=27, column=0, sticky="w")
    epitope_percentile_entry = ttk.Entry(frame, textvariable=epitope_percentile_var)
    epitope_percentile_entry.grid(row=27, column=1, sticky="w", padx=10, pady=5)



    # Pulsante Esegui
    run_button = ttk.Button(frame, text="RUN", command=button_click)
    run_button.grid(row=28, columnspan=2, pady=10, sticky='e')

    
# Esempio di utilizzo
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Launcher")

    def on_button_click(args):
        open_main_window(args)

    open_gui(root, on_button_click)

    root.mainloop()

