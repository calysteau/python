import argparse
import os
from tqdm import tqdm
import rasterio
from rasterio.shutil import copy
from rasterio.enums import Resampling

# Créer un analyseur d'arguments
parser = argparse.ArgumentParser(description='Convertir des fichiers GeoTIFF en Cloud Optimized GeoTIFF (COG).')
parser.add_argument('--repertoire_geotiff', required=True, help='Répertoire contenant les fichiers GeoTIFF à convertir.')
parser.add_argument('--repertoire_cog', required=True, help='Répertoire de sortie pour les fichiers COG convertis.')
args = parser.parse_args()

# Répertoires pour les fichiers GeoTIFF et COG
repertoire_geotiff = args.repertoire_geotiff
repertoire_cog = args.repertoire_cog

# Créer le répertoire de sortie pour les COG
if not os.path.exists(repertoire_cog):
    os.makedirs(repertoire_cog)

# Fonction pour convertir un fichier GeoTIFF en COG
def convertir_geotiff_en_cog(chemin_fichier_geotiff, repertoire_cog):
    with rasterio.open(chemin_fichier_geotiff) as src:
        profile = src.profile.copy()
        profile.update(driver='GTiff', tiled=True, blockxsize=512, blockysize=512, compress='LZW')

        chemin_relatif = os.path.relpath(chemin_fichier_geotiff, repertoire_geotiff)
        chemin_sans_extension, _ = os.path.splitext(chemin_relatif)
        chemin_fichier_cog = os.path.join(repertoire_cog, chemin_sans_extension + ".tif")

        os.makedirs(os.path.dirname(chemin_fichier_cog), exist_ok=True)

        copy(src, chemin_fichier_cog, copy_src_overviews=True, **profile)

# Compter le nombre total de fichiers GeoTIFF
total_fichiers_geotiff = sum(1 for _, _, fichiers in os.walk(repertoire_geotiff) for fichier in fichiers if fichier.endswith(".tif"))

# Barre de progression
barre_de_progression = tqdm(total=total_fichiers_geotiff, unit="fichier")

# Parcourir et convertir les fichiers GeoTIFF en COG
for dossier, _, fichiers in os.walk(repertoire_geotiff):
    for fichier in fichiers:
        if fichier.endswith(".tif"):
            chemin_fichier_geotiff = os.path.join(dossier, fichier)
            convertir_geotiff_en_cog(chemin_fichier_geotiff, repertoire_cog)
            barre_de_progression.update(1)

# Fermer la barre de progression
barre_de_progression.close()

print("Conversion en COG terminée.")
