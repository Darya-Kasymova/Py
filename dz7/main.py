from contextlib import ExitStack
from CSV_creating import creating
from writing_file import writing_scv
from writing_file import writing_txt


path = 'spravochnik.csv'
valid = ExitStack(path)
if not valid:
    creating()

writing_scv()
writing_txt()