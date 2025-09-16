import os
from pathlib import Path
import re
import csv

def lister_fichiers_recursifs(dossier, fichier_sortie, extensions, avec_chemins=True, format_sortie='txt'):
    mode_ecriture = 'w'
    encoding = 'utf-8'

    if format_sortie.lower() == 'csv':
        mode_ecriture = 'w'
        encoding = 'utf-8-sig'  # Pour Excel

    with open(fichier_sortie, mode_ecriture, encoding=encoding, newline='') as f:
        if format_sortie.lower() == 'csv':
            writer = csv.writer(f)
            writer.writerow(["Nom du Fichier", "Chemin Complet" if avec_chemins else ["Nom du Fichier"]])

        for racine, _, fichiers in os.walk(dossier):
            for fichier in fichiers:
                if extensions == ['all'] or any(fichier.endswith(ext) for ext in extensions):
                    # Supprimer l'extension et remplacer les ' - ' par ' \ '
                    nom_sans_ext = os.path.splitext(fichier)[0]
                    nom_modifie = re.sub(r' - ', ' \\ ', nom_sans_ext)

                    if format_sortie.lower() == 'csv':
                        if avec_chemins:
                            writer.writerow([nom_modifie, os.path.join(racine, nom_modifie)])
                        else:
                            writer.writerow([nom_modifie])
                    else:  # TXT
                        if avec_chemins:
                            f.write(f"{os.path.join(racine, nom_modifie)}\n")
                        else:
                            f.write(f"{nom_modifie}\n")

# Chemin du bureau Windows
bureau = str(Path.home() / "Desktop")

# Saisie utilisateur
dossier_a_scanner = input("Chemin du dossier à scanner : ").strip('"')
extensions_input = input("Extensions à filtrer (séparées par des virgules, ou 'all') : ").strip()
format_sortie = input("Format de sortie (txt/csv) : ").strip().lower()
chemins_input = input("Inclure les chemins complets ? (o/n) : ").strip().lower()

# Traitement des options
avec_chemins = chemins_input == 'o'
fichier_sortie = os.path.join(bureau, f"liste_fichiers.{format_sortie}")

# Traitement des extensions
if extensions_input.lower() == 'all':
    extensions = ['all']
else:
    extensions = [ext.strip().lower() for ext in extensions_input.split(',')]
    extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]

# Vérification et exécution
if os.path.isdir(dossier_a_scanner):
    lister_fichiers_recursifs(dossier_a_scanner, fichier_sortie, extensions, avec_chemins, format_sortie)
    option_chemins = "avec chemins" if avec_chemins else "sans chemins"
    print(f"Liste sauvegardée ({option_chemins}, format {format_sortie.upper()}) : {fichier_sortie}")
else:
    print("Erreur : Dossier introuvable.")
