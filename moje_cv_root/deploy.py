import os
import requests
from distutils.dir_util import copy_tree
import os
from moje_cv.settings import LANGUAGES, LANGUAGE_CODE

landing_page_language = LANGUAGE_CODE

# ---

for code, language in LANGUAGES:
    site = requests.get(os.path.join("http://127.0.0.1:8000/", code)).text

    with open('../{}.html'.format(code), 'w', encoding="utf-8") as ff:
        print("Writting", code, "site")
        ff.write(site)

print("renaming", "../{}.html".format(landing_page_language), "to ../index.html")
os.replace("../{}.html".format(landing_page_language), "../index.html")
# ---

print("Copying assets...")
copy_tree("assets", "../static")

# ---

print("Renaming CV's...")
for code, language in LANGUAGES:
	cv_main_name = "../static/CV {} Andrzej Bisewski n.pdf".format(code)
	new_name = "../CV-{}-Andrzej-Bisewski.pdf".format(code)
	os.replace(cv_main_name, new_name)
