# Convertisseur d'images en PDF

Ce programme permet de convertir des images (PNG, JPG, JPEG, GIF) en fichiers PDF et de les enregistrer dans un dossier "data". Il offre également la possibilité d'ouvrir le dossier "data" pour visualiser les fichiers PDF générés.

## Modules utilisés

-   `tkinter` : Bibliothèque pour créer des interfaces graphiques.
-   `filedialog` (de `tkinter`) : Module pour ouvrir des boîtes de dialogue de sélection de fichiers.
-   `messagebox` (de `tkinter`) : Module pour afficher des boîtes de dialogue de messages.
-   `PIL` (Python Imaging Library) : Bibliothèque pour traiter les images.
-   `webbrowser` : Module pour ouvrir des fichiers avec le navigateur web par défaut.
-   `os` : Module pour interagir avec le système d'exploitation.


## Utilisation

1.  Exécutez le script.
2.  Cliquez sur "Sélectionner des images" pour choisir une images.
3.  Cliquez sur "Convertir en PDF" pour convertir les images sélectionnées en fichiers PDF.
4.  Un label affichera le nom du fichier PDF généré, et un bouton "Retour" permettra de revenir à l'interface principale.
5.  Cliquez sur "Sélectionner Mon PDF" pour ouvrir le dossier "data" et visualiser les fichiers PDF générés.

## Remarques

-   Le dossier "data" sera créé automatiquement s'il n'existe pas.
-   Les fichiers PDF générés seront ouverts avec le navigateur web par défaut du système.
-   Le programme utilise la bibliothèque `PIL` (Python Imaging Library) pour traiter les images.
-   Les boîtes de dialogue de sélection de fichiers et les messages d'erreur sont gérés par les modules `filedialog` et `messagebox` de `tkinter`.
