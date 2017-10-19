"""
October 13, 2017

UC Davis Computational Linguistics Lab

This script splits an input file into 10 separate files
so that it may be parsed by CoreNLP

Usage: python partition_file.py infile dump_path
"""

import io
import sys

f = io.open(sys.argv[1], encoding='utf8')

dump_path = sys.argv[2]

# TODO get line count of any input file
line_count = sum(1 for line in f)


per_file = line_count/10

index = 1

d0 = io.open(dump_path + '0', mode="a+", encoding='utf8')
d1 = io.open(dump_path + '1', mode="a+", encoding='utf8')
d2 = io.open(dump_path + '2', mode="a+", encoding='utf8')
d3 = io.open(dump_path + '3', mode="a+", encoding='utf8')
d4 = io.open(dump_path + '4', mode="a+", encoding='utf8')
d5 = io.open(dump_path + '5', mode="a+", encoding='utf8')
d6 = io.open(dump_path + '6', mode="a+", encoding='utf8')
d7 = io.open(dump_path + '7', mode="a+", encoding='utf8')
d8 = io.open(dump_path + '8', mode="a+", encoding='utf8')
d9 = io.open(dump_path + '9', mode="a+", encoding='utf8')

f = io.open(sys.argv[1], encoding='utf8')

for line in f:
  if index < per_file:
    d0.write(line)
  elif index < 2*per_file:
    d1.write(line)
  elif index < 3*per_file:
    d2.write(line)
  elif index < 4*per_file:
    d3.write(line)
  elif index < 5*per_file:
    d4.write(line)
  elif index < 6*per_file:
    d5.write(line)
  elif index < 7*per_file:
    d6.write(line)
  elif index < 8*per_file:
    d7.write(line)
  elif index < 9*per_file:
    d8.write(line)
  else:
    d9.write(line)
  index += 1
