# Convertisseur TIF vers COG en Python

## À propos
TIFtoCOG est un outil en ligne de commande pour convertir efficacement des fichiers GeoTIFF en Cloud Optimized GeoTIFF (COG). Cet outil vise à faciliter le processus de conversion pour permettre une meilleure intégration et accessibilité des données géospatiales dans divers environnements de cloud computing.

## Fonctionnalités
- Conversion de fichiers GeoTIFF en COG.
- Prise en charge de la compression LZW.
- Gestion optimisée des grandes collections de données géospatiales.
- Conservation des métadonnées et de la qualité des données d'origine.

## Prérequis
- Python 3.6 ou supérieur.
- Bibliothèque Rasterio. Vous pouvez l'installer via pip :
```
pip install rasterio
```

## Installation
Clonez le dépôt GitHub ou téléchargez le code source :
``` 
git clone https://github.com/calysteau/python
```

## Utilisation
Configurer l'environnement :
Assurez-vous que Python et Rasterio sont installés sur votre système.

Exécution du script :
Utilisez la ligne de commande pour exécuter le script :

```
python tiftocog.py --repertoire_geotiff chemin_vers_geotiff --repertoire_cog chemin_vers_cog
```

- chemin_vers_geotiff : Répertoire contenant vos fichiers GeoTIFF.
- chemin_vers_cog : Répertoire de sortie pour les fichiers COG.

## Vérification des résultats :
Vérifiez le répertoire de sortie pour vous assurer que les fichiers COG ont été créés correctement.

## Exemple
```
python tiftocog.py --repertoire_geotiff ./data/geotiff --repertoire_cog ./data/cog
```

## Contribution
Les contributions au projet sont les bienvenues. Veuillez consulter les lignes directrices de contribution avant de soumettre une pull request.

## Licence
Ce projet est sous licence MIT. Pour plus d'informations, veuillez consulter le fichier `LICENSE` inclus.

## Contact
Pour toute question ou collaboration, veuillez contacter CALYSTEAU à contact@calysteau.fr