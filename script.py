import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import webbrowser
import os


selected_files = []

def select_images():
    global selected_files
    selected_files = filedialog.askopenfilenames(
        title='Sélectionner des images',
        initialdir='/Images',
        filetypes=[("Images", "*.png *.jpg *.jpeg *.gif")]
    )

def select_pdf():
    global selected_files
    if not os.path.exists("data"):
        messagebox.showerror("Erreur", f"le dossier 'data' n'existe pas. Selectionner une image et convertisser votre image en pdf")
    else: 
        selected_files = filedialog.askopenfilenames(
            title='Sélectionner des images',
            initialdir=f'{os.getcwd()}/data',
            filetypes=[]
        )
        if selected_files:
            for pdf_file in selected_files:
                webbrowser.open_new(pdf_file)

def affichage(base_name):
    label = tk.Label(root, text=f"Fichier PDF créé : {base_name}.pdf", justify="left", font=("Arial", 14), fg="blue", bg="lightgray", wraplength=300)
    label.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    label_2.grid_forget()
    select_button.grid_forget()
    convert_button.grid_forget()

    def retour():
        select_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        convert_button.grid(row=1, column=2, padx=5, pady=5)
        return_button.grid_forget()
        label.grid_forget()
        label_2.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    return_button = tk.Button(root, text="Retour", command=retour)
    return_button.grid(row=1, column=0, padx=5, pady=5)

def convert():
    global selected_files
    if not os.path.exists("data"):
        os.makedirs("data")
    for filename in selected_files:
        image = Image.open(filename)
        image = image.convert('RGB')
        base_name = os.path.splitext(os.path.basename(filename))[0]
        image.save(f"./data/{base_name}.pdf")
        affichage(base_name)
        
root = tk.Tk()
root.iconbitmap("Pdf.ico")
root.title("Convertisseur PDF")
root.resizable(False, False)

label_2 = tk.Label(root, text="Convertisseur PDF", font=("Arial", 14), fg="blue", bg="lightgray", wraplength=300)
label_2.grid(row=0, column=1, padx=20, pady=20, sticky="nesw")

select_button = tk.Button(root, text='Sélectionner des images', command=select_images)
select_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

select_button_pdf = tk.Button(root, text='Sélectionner Mon PDF', command=select_pdf)
select_button_pdf.grid(row=1, column=1, padx=5, pady=5, sticky="w")

convert_button = tk.Button(root, text='Convertir en PDF', command=convert)
convert_button.grid(row=1, column=2, padx=5, pady=5, sticky="w")

root.mainloop()