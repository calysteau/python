# Convertisseur PNG vers WebP en Python

Ce script Python vous permet de convertir facilement des images au format PNG en images au format WebP tout en conservant la transparence alpha. Il prend en charge la conversion récursive de tous les fichiers PNG d'un répertoire source et conserve la structure des sous-répertoires.

## Fonctionnalités

- Conversion de fichiers PNG en images WebP.
- Conservation de la transparence alpha des images PNG.
- Conversion récursive de tous les fichiers PNG dans un répertoire source.
- Conservation de la structure des sous-répertoires dans le répertoire de sortie.

## Dépendances

Ce script utilise les dépendances suivantes :

- [Pillow](https://python-pillow.org/): Une bibliothèque Python pour le traitement d'images.
- [tqdm](https://github.com/tqdm/tqdm): Une bibliothèque pour afficher une barre de progression pendant le traitement (facultatif, mais recommandé).

## Installation

1. Assurez-vous d'avoir Python installé sur votre système. Vous pouvez télécharger Python à partir du site officiel : [python.org](https://www.python.org/downloads/).

2. Installez les dépendances en utilisant `pip`. Ouvrez une invite de commande ou un terminal et exécutez les commandes suivantes :

```
pip install Pillow
pip install tqdm
````

3. Clonez ou téléchargez ce dépôt GitHub sur votre ordinateur.

4. Exécutez le script en utilisant Python en spécifiant les répertoires d'entrée et de sortie comme arguments. Par exemple :
```
python PNGtoWEBP.py --repertoire_png "chemin/vers/vos/images/png" --repertoire_webp "chemin/vers/votre/dossier/de/sortie"
```

Assurez-vous de personnaliser les chemins d'accès aux répertoires en fonction de vos besoins.

## Auteur

CALYSTEAU

## Licence

Ce script est sous licence MIT.
