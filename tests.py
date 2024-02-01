# ---------------------------------------------
# Nom du fichier: tests.py
# Auteur: Maxime Rabaud
# Description: fichier principal pour executer le programme 
# ---------------------------------------------

import itertools
import random as rd
from datetime import date
from typing import List

TEST_TYPES = ["Functionnal", "Reliability", "Performance", "Operability", "Security", "Compatibility", "Maintenabilty", "Transferability"]
TEST_RESULTS = ["Passed", "Failed", "Skipped", "Error", "Passed"]

class Test:
    """ 
    Classe qui definit un test avec ses attributs 
    """

    _id_obj = itertools.count(start=1)

  def __init__(self, test_type: str, exec_date: str, exec_duration: str, result: str):
    # Initialise une nouvelle instance d'un test
    

    self.id = next(Test._id_obj)
    self.name = f"Test_{self.id:04d}" # ex. Test_0001 
    self.test_type = test_type
    self.exec_date = exec_date
    self.exec_duration = exec_duration
    self.result = result

  def get_formatted_dictionnary(self):
      # Retourne un dictionnaire de type {key: value} pour chaque attributs 
      return vars(self)


def init_tests(nb: int):
  # Initialise <nb> tests et renvoie un tableau 
  tests = []

  for _ in range(nb):
      test_type = rd.choice(TEST_TYPES)
    exec_date = date.today()
    exec_duration = rd.randint(1, 300)
    result = rd.choice(TEST_RESULTS)

    test = Test(test_type, exec_date, exec_duration, result)
    tests.append(test)

  return tests
