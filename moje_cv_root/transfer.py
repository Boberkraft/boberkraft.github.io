import os
import requests
from distutils.dir_util import copy_tree


site = requests.get("http://127.0.0.1:8000/").text

with open('../index.html', 'w', encoding="utf-8") as ff:
    ff.write(site)

copy_tree("assets", "../static")


