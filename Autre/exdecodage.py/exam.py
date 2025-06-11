from utils import unzip_with_7z
import string
from itertools import product

zip_file_path = 'congrats.7z'  # keep as is
dest_path = '.'  # keep as is

# Boucle brute-force pour trouver les 2 lettres manquantes
for letters in product(string.ascii_lowercase, repeat=2):
    find_me = ''.join(letters)
    secret_password = find_me + 'bcmpda'
    
    if unzip_with_7z(zip_file_path, dest_path, secret_password):
        print(f"✅ Mot de passe trouvé : {secret_password}")
        break
    else:
        print(f"❌ Mauvais mot de passe : {secret_password}")
