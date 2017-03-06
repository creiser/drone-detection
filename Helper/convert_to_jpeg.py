from __future__ import print_function
import os, sys
from PIL import Image

for infile in os.listdir('.'):
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
            os.remove(infile)
        except IOError:
            print("cannot convert", infile)