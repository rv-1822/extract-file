import os
from pathlib import Path
import re

def lister_fichiers_recursifs(dossier, fichier_sortie, extensions, avec_chemins=True):
    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        for racine, _, fichiers in os.walk(dossier):
            for fichier in fichiers:
                if extensions == ['all'] or any(fichier.endswith(ext) for ext in extensions):
                    # Supprimer l'extension et remplacer les ' - ' par ' \ '
                    nom_sans_ext = os.path.splitext(fichier)[0]
                    nom_modifie = re.sub(r' - ', ' \\ ', nom_sans_ext)

                    # Écrire selon l'option de chemins
                    if avec_chemins:
                        f.write(f"{os.path.join(racine, nom_modifie)}\n")
                    else:
                        f.write(f"{nom_modifie}\n")

# Chemin du bureau Windows
bureau = str(Path.home() / "Desktop")
fichier_sortie = os.path.join(bureau, "liste_fichiers.txt")

# Saisie utilisateur
dossier_a_scanner = input("Chemin du dossier à scanner : ").strip('"')
extensions_input = input("Extensions à filtrer (séparées par des virgules, ou 'all') : ").strip()
chemins_input = input("Inclure les chemins complets ? (o/n) : ").strip().lower()

# Traitement des options
avec_chemins = chemins_input == 'o'

# Traitement des extensions
if extensions_input.lower() == 'all':
    extensions = ['all']
else:
    extensions = [ext.strip().lower() for ext in extensions_input.split(',')]
    extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]

# Vérification et exécution
if os.path.isdir(dossier_a_scanner):
    lister_fichiers_recursifs(dossier_a_scanner, fichier_sortie, extensions, avec_chemins)
    option_chemins = "avec chemins" if avec_chemins else "sans chemins"
    print(f"Liste sauvegardée ({option_chemins}, sans extensions) : {fichier_sortie}")
else:
    print("Erreur : Dossier introuvable.")
