# encoding: utf-8
import glob
import os
import re
from mutagen.easyid3 import EasyID3
# pip install mutagen

quiet = False

def fix_kr_tag(f, tag):
  try:
    title = f[tag]
    b = bytes()
    for c in title[0]:
      b += "%s" % chr(ord(c))
    converted = unicode(b,"cp949")

    if title[0] == converted:
      return False
    #print("%s ?= %s" % (title[0], converted))
    if not quiet:
      print(f"  {tag} = {converted}")
    f[tag]=converted
    return True
  except:
    pass
    return False

def fix_kr_encoding(path):
  needSave = False
  f = EasyID3(path)
  for tag in f.keys():
    if fix_kr_tag(f, tag):
      needSave = True

  if needSave: 
    if not quiet:
      print(f"updating {path}" )
    f.save()

def fix_dir(directory):
  directory = re.sub(r'\[', '[[]', directory)
  directory = re.sub(r'(?<!\[)\]', '[]]', directory)

  for path in glob.glob(directory+"/*.[Mm][Pp]3"):
    if not quiet:
      print(f"checking {path}")
    fix_kr_encoding(path)

def main():
  fix_dir(os.getcwd())

if __name__ == "__main__":
  main()

