#! /usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals
import os
import sys
import cv
import argparse
import termcolor
import ast
import copy


class ImageToGcode():
    def __init__(self,img,  verbose=False):
        self.img = cv.LoadImageM(img)
        self.output = ""
        self.outFile = os.path.splitext(os.path.abspath(img))[0] + ".gco"
        self.spread = 3.175
        self.nozzles = 12
        self.increment = spread/nozzles
        self.printArea = [200, 200]
        self.feedrate = 1000
        self.red = (0.0, 0.0, 255.0, 0.0)
        self.green = (0.0, 255.0, 0.0, 0.0)
        self.blue = (255.0, 0.0, 0.0, 0.0)
        self.black = (0.0, 0.0, 0.0, 0.0)
        self.offsets = black
        self.debug_to_terminal()
        self.make_gcode()

    def make_gcode(self):
        self.output = "M106"  # Start Fan
        nozzleFirings = [0 for x in range(0, self.img.cols)]
        nozzleFirings = [copy.copy(nozzleFirings) for x in range(0, 4)]
        scan = range(0, self.img.rows)
        scan.reverse()
        for y in scan:
            for x in range(0, self.img.cols):
                color = cv.Get2D(self.img, y, x)
                if color == self.red:
                    nozzleFirings[0][x] += 1 << y % self.nozzles
                elif color == self.green:
                    nozzleFirings[1][x] += 1 << y % self.nozzles
                elif color == self.blue:
                    nozzleFirings[2][x] += 1 << y % self.nozzles
                elif color == self.black:
                    nozzleFirings[3][x] += 1 << y % self.nozzles
                else:
                    pass
            if y % 12 == 0 and y > 0:
                for headNumber, headVals in enumerate(nozzleFirings):
                    for column, firingVal in enumerate(headVals):
                        if firingVal:
                            currentOffset = self.offsets[headNumber]
                            self.output += "G1X"+str(self.increment*column-currentOffset[0])+"Y"+str(y/12*self.spread-currentOffset[1])+"F"+str(self.feedrate)+"\n"
                            self.output += "M400\n"
                            self.output += "M700 P"+str(headNumber)+" S"+str(firingVal)+"\n"
                print(str(nozzleFirings))
                nozzleFirings = [0 for x in range(0, self.img.cols)]
                nozzleFirings = [copy.copy(nozzleFirings) for x in range(0, 4)]
        f = open(self.outFile, 'w')
        f.write(self.output)
        f.close()
        print(self.output)

    def debug_to_terminal(self):
        print("Rows: "+str(self.img.rows))
        print("Cols: "+str(self.img.cols))
        print("Spread: "+str(self.spread)+"mm")
        print("Nozzles: "+str(self.nozzles))
        print("Print Area: "+str(self.printArea)+"mm")
        rowStr = ""
        for y in range(0, self.img.rows):
            rowStr = ""
            for x in range(0, self.img.cols):
                color = cv.Get2D(self.img, y, x)
                if color == self.red:
                    rowStr += termcolor.colored(" ", 'white', 'on_red')
                elif color == self.green:
                    rowStr += termcolor.colored(" ", 'white', 'on_green')
                elif color == self.blue:
                    rowStr += termcolor.colored(" ", 'white', 'on_blue')
                elif color == self.black:
                    rowStr += " "
                else:
                    rowStr += termcolor.colored(" ", 'white', 'on_white')
            print(rowStr)

    imageProcessor = ImageToGcode(img)
