#!/usr/bin/python

import sys
from PIL import Image

def pixel8(inputfile,outputfile):
    factor = 8
    img = Image.open(inputfile)
    width, height = img.size
    out = Image.new('RGB', (width*factor, height*factor), color=0)
    for y in range(height):
        for x in range(width):
            color = img.getpixel((x, y))
            for a in range(factor):
                for b in range(factor):
                    out.putpixel((x*factor+a, y*factor+b), color)
    out.save(outputfile)

def main():
    if len(sys.argv) == 1:
        print("Example: ./pixel8.py in.png out.png")
    try:
        inputfile = sys.argv[1]
        outputfile = sys.argv[2]

    except getopt.error as err:
        print (str(err))
    try:
        pixel8(inputfile,outputfile)
    except:
        print("Something went wrong! Try -h to see help")

if __name__ == "__main__":
   main()
