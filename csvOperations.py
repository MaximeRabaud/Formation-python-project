import csv
from typing import List

from tests import *

def generate_csv(filename: str, fields: List[str], tests: List[Test]) -> None:
  with open(filename, 'w', newline='') as file: 
    writer = csv.DictWriter(file, fieldnames = fields)
    writer.writeheader()   

    writer.writerows(map(Test.get_formatted_dictionnary, tests))

    file.close()
