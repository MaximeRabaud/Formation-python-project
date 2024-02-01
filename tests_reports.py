# ---------------------------------------------
# Nom du fichier: test-reports.py
# Auteur: Maxime Rabaud
# Description: fichier principal pour executer le programme 
# ---------------------------------------------

import csv
import argparse
from csvOperations import *
from tests import *

# parser pour gerer les options a partir du CLI
parser = argparse.ArgumentParser(prog="Generate Test-report csv", 
                                 description="Genere un rapport de tests dans le format csv")
parser.add_argument('-f', dest='filename', default='rapport_test.csv', help="Nom du fichier de sortie",type=str)
parser.add_argument('-n', dest='nombre_tests', default='5', help="le nombre de tests qui seront générés",type=int)

args = parser.parse_args()

# champs definis pour les tests (cf. Test.py)
FIELDS = ["id", "name", "test_type", "exec_date", "exec_duration", "result"]

# Execution du programme
tests = init_tests(args.nombre_tests)
generate_csv(args.filename, FIELDS, tests)
