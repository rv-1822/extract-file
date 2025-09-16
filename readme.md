# Script de Liste de Fichiers avec Formatage Avancé

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

Un script Python puissant pour lister récursivement les fichiers avec des options de formatage personnalisées, idéal pour l'organisation et l'analyse de structures de dossiers.

---

## 📋 Table des Matières
- [Fonctionnalités](#-fonctionnalités)
- [Prérequis](#-prérequis)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
  - [Options disponibles](#options-disponibles)
  - [Exemples d'exécution](#exemples-d'exécution)
- [Exemples de Sortie](#-exemples-de-sortie)
- [Personnalisation Avancée](#-personnalisation-avancée)
- [Fonctionnement Interne](#-fonctionnement-interne)
- [Limitations Connues](#-limitations-connues)
- [Licence](#-licence)
- [Contribution](#-contribution)
- [Historique des Versions](#-historique-des-versions)
- [FAQ](#-faq)

---

## 🌟 Fonctionnalités

✅ **Liste récursive complète** : Parcourt tous les sous-dossiers de manière récursive
✅ **Filtrage intelligent** :
   - Par extensions de fichiers (`.txt`, `.pdf`, etc.)
   - Option "toutes extensions" (`all`)
✅ **Formatage avancé des noms** :
   - Remplace automatiquement les ` - ` par ` \ ` dans les noms
   - Exclut les extensions des noms de fichiers dans la sortie
✅ **Options de sortie flexibles** :
   - Avec ou sans chemins complets
   - Fichier de sortie personnalisable (par défaut sur le bureau)
✅ **Gestion des erreurs** :
   - Dossiers inaccessibles
   - Permissions insuffisantes
✅ **Interface interactive** : Guide l'utilisateur pas à pas

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

### Exemples d'Exécution

#### Exemple 1 : Liste complète avec chemins
