# Script de Liste de Fichiers avec Formatage Avancé

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

Un script Python  pour lister récursivement les fichiers avec des options de formatage personnalisées.

---

## 📌 Prérequis

- **Python** : Version 3.x (testé avec Python 3.8+)
- **Système d'exploitation** : Windows (optimisé pour les chemins Windows, mais adaptable pour Linux/macOS)
- **Bibliothèques** : Utilise uniquement les bibliothèques standard (`os`, `pathlib`, `re`)

---

## 🛠 Installation

1. **Télécharger le script** :
   - Copiez le code source dans un fichier nommé `lister_fichiers.py`
   - Ou clonez ce dépôt (si disponible)

2. **Placement** :
   - Placez le script dans un dossier de votre choix
   - Aucune installation supplémentaire n'est nécessaire

3. **Exécution** :
   - Double-cliquez sur le fichier (si Python est associé)
   - Ou exécutez via la ligne de commande :
     ```bash
     python lister_fichiers.py
     ```

---

## 🚀 Utilisation

### Options Disponibles

| Option | Description | Exemple de Valeur |
|--------|-------------|-------------------|
| **Dossier à scanner** | Chemin du dossier racine | `C:\MesDocuments` ou `"C:\Dossiers\Mon Projet"` |
| **Extensions** | Filtre par extensions | `all` ou `.txt,.pdf,.jpg` |
| **Chemins complets** | Inclure les chemins ? | `o` (oui) ou `n` (non) |
|Format de sortie |(txt/csv)| `txt` ou `csv`|


<h2>&#9881; Personnalisation</h2>

1. **Changer le séparateur**

* Ligne ~20 : Modifiez ' \\ ' par votre séparateur (Exemple avec │ )

      nom_modifie = re.sub(r' - ', ' │ ', nom_sans_ext)  

2. **Ajouter des colonnes CSV**

* Dans la section CSV, ajoutez des colonnes :

      writer.writerow(["Nom", "Chemin", "Taille", "Date"])

* Puis complétez avec :

      taille = os.path.getsize(os.path.join(racine, fichier))
      date = os.path.getmtime(os.path.join(racine, fichier))
      writer.writerow([nom_modifie, os.path.join(racine, nom_modifie), taille, date])

