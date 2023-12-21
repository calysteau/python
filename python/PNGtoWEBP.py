import argparse
from PIL import Image
import os
from tqdm import tqdm

# Créer un analyseur d'arguments
parser = argparse.ArgumentParser(description='Convertir des images PNG en images WebP en conservant la transparence.')

# Ajouter des arguments pour les répertoires d'entrée et de sortie
parser.add_argument('--repertoire_png', required=True, help='Répertoire contenant les images PNG à convertir.')
parser.add_argument('--repertoire_webp', required=True, help='Répertoire de sortie pour les images WebP converties.')

# Analyser les arguments de la ligne de commande
args = parser.parse_args()

# Répertoire contenant vos images PNG
repertoire_png = args.repertoire_png

# Répertoire de sortie pour les images WebP
repertoire_webp = args.repertoire_webp

# Créer le répertoire de sortie s'il n'existe pas
if not os.path.exists(repertoire_webp):
    os.makedirs(repertoire_webp)

# Fonction pour convertir une image PNG en WebP en conservant la transparence
def convertir_image_png_en_webp(chemin_fichier_png, repertoire_webp):
    # Ouvrir l'image PNG avec Pillow
    image = Image.open(chemin_fichier_png)

    # Construire le chemin de sortie pour l'image WebP en conservant la structure
    # des sous-répertoires et en modifiant l'extension en ".webp"
    chemin_relatif = os.path.relpath(chemin_fichier_png, repertoire_png)
    chemin_sans_extension, _ = os.path.splitext(chemin_relatif)
    chemin_fichier_webp = os.path.join(repertoire_webp, chemin_sans_extension + ".webp")

    # Créer les sous-répertoires s'ils n'existent pas
    os.makedirs(os.path.dirname(chemin_fichier_webp), exist_ok=True)

    # Convertir et sauvegarder l'image en WebP en conservant la transparence
    image.save(chemin_fichier_webp, "webp", quality=95, lossless=True)

# Compter le nombre total de fichiers PNG dans le répertoire source
total_fichiers_png = sum(1 for dossier, _, fichiers in os.walk(repertoire_png) for fichier in fichiers if fichier.endswith(".png"))

# Barre de progression
barre_de_progression = tqdm(total=total_fichiers_png, unit="image")

# Parcourir les fichiers PNG et les convertir en WebP en conservant la transparence
for dossier, _, fichiers in os.walk(repertoire_png):
    for fichier in fichiers:
        if fichier.endswith(".png"):
            chemin_fichier_png = os.path.join(dossier, fichier)
            convertir_image_png_en_webp(chemin_fichier_png, repertoire_webp)
            barre_de_progression.update(1)  # Mettre à jour la barre de progression

# Fermer la barre de progression
barre_de_progression.close()

print("Conversion terminée.")
