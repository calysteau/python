# Convertisseur TIF vers COG en Python

## � propos
TIFtoCOG est un outil en ligne de commande pour convertir efficacement des fichiers GeoTIFF en Cloud Optimized GeoTIFF (COG). Cet outil vise � faciliter le processus de conversion pour permettre une meilleure int�gration et accessibilit� des donn�es g�ospatiales dans divers environnements de cloud computing.

## Fonctionnalit�s
- Conversion de fichiers GeoTIFF en COG.
- Prise en charge de la compression LZW.
- Gestion optimis�e des grandes collections de donn�es g�ospatiales.
- Conservation des m�tadonn�es et de la qualit� des donn�es d'origine.

## Pr�requis
- Python 3.6 ou sup�rieur.
- Biblioth�que Rasterio. Vous pouvez l'installer via pip :
```
pip install rasterio
```

## Installation
Clonez le d�p�t GitHub ou t�l�chargez le code source :
``` 
git clone https://github.com/calysteau/python
```

## Utilisation
Configurer l'environnement :
Assurez-vous que Python et Rasterio sont install�s sur votre syst�me.

Ex�cution du script :
Utilisez la ligne de commande pour ex�cuter le script :

```
python tiftocog.py --repertoire_geotiff chemin_vers_geotiff --repertoire_cog chemin_vers_cog
```

- chemin_vers_geotiff : R�pertoire contenant vos fichiers GeoTIFF.
- chemin_vers_cog : R�pertoire de sortie pour les fichiers COG.

## V�rification des r�sultats :
V�rifiez le r�pertoire de sortie pour vous assurer que les fichiers COG ont �t� cr��s correctement.

## Exemple
```
python tiftocog.py --repertoire_geotiff ./data/geotiff --repertoire_cog ./data/cog
```

## Contribution
Les contributions au projet sont les bienvenues. Veuillez consulter les lignes directrices de contribution avant de soumettre une pull request.

## Licence
Ce projet est sous licence MIT. Pour plus d'informations, veuillez consulter le fichier `LICENSE` inclus.

## Contact
Pour toute question ou collaboration, veuillez contacter CALYSTEAU � contact@calysteau.fr