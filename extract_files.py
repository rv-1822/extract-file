import os
from pathlib import Path

def lister_fichiers_recursifs(dossier, fichier_sortie, extensions):
    with open(fichier_sortie, 'w', encoding='utf-8') as f:
        for racine, _, fichiers in os.walk(dossier):
            for fichier in fichiers:
                if extensions == ['all'] or any(fichier.endswith(ext) for ext in extensions):
                    chemin_complet = os.path.join(racine, fichier)
                    f.write(f"{chemin_complet}\n")

# Chemin du bureau Windows
bureau = str(Path.home() / "Desktop")
fichier_sortie = os.path.join(bureau, "liste_fichiers.txt")

# Saisie utilisateur
dossier_a_scanner = input("Chemin du dossier à scanner : ").strip('"')
extensions_input = input("Extensions à extraire (séparées par des virgules, ou 'all') : ").strip()

# Traitement des extensions
if extensions_input.lower() == 'all':
    extensions = ['all']
else:
    extensions = [ext.strip().lower() for ext in extensions_input.split(',')]
    # Ajouter un point devant chaque extension si absent
    extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]

# Vérification et exécution
if os.path.isdir(dossier_a_scanner):
    lister_fichiers_recursifs(dossier_a_scanner, fichier_sortie, extensions)
    print(f"Liste sauvegardée : {fichier_sortie}")
else:
    print("Erreur : Dossier introuvable.")
