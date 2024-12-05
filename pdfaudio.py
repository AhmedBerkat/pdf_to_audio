import pyttsx3
import PyPDF2
from tkinter.filedialog import *

# Sélectionner un fichier PDF
book = askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])

pdfreader = PyPDF2.PdfReader(book) 
player = pyttsx3.init()  # Initialiser le moteur audio
if book :
# Lire et convertir chaque page en audio
 for i in pdfreader.pages:
        text = i.extract_text()
        player.say(text)
        player.runAndWait()
else:
    print("Aucun fichier sélectionné.")
