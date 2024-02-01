# ---------------------------------------------
# Nom du fichier: csvOperations.py
# Auteur: Maxime Rabaud
# Description: fichier principal pour executer le programme 
# ---------------------------------------------

import csv
from typing import List
from tests import *

def generate_csv(filename: str, fields: List[str], tests: List[Test]) -> None:
  # Genere un fichier csv avec un le nom <filename> pour les <fields> specifier en entrer
  with open(filename, 'w', newline='') as file: 
    writer = csv.DictWriter(file, fieldnames = fields)
    writer.writeheader()   

    writer.writerows(map(Test.get_formatted_dictionnary, tests))

    file.close()
