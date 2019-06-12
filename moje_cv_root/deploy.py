import os
import requests
from distutils.dir_util import copy_tree
import os
from moje_cv.settings import LANGUAGES

default_language = "pl"

for code, language in LANGUAGES:
    site = requests.get(os.path.join("http://127.0.0.1:8000/", code)).text

    with open('../{}.html'.format(code), 'w', encoding="utf-8") as ff:
        print("Writting", code, "site")
        ff.write(site)

print("renaming", "../{}.html".format(default_language), "to ../index.html")
os.replace("../{}.html".format(default_language), "../index.html")

print("Copying assets...")
copy_tree("assets", "../static")


