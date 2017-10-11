# 1 Sept, 2017
# UC Davis Computational Linguisitics Lab

# Program to locate parsed sentences in 
# Stanford CoreNLP XML formated files and extract same.

# Usage:  clean_parse.py input_file_base output_file_name num_files

import re
import io
import sys

tree = io.open(sys.argv[2], 'a+', encoding = 'utf-8')

for i in range(int(sys.argv[3])):
  if int(sys.argv[3]) > 1:
    f = io.open(sys.argv[1] + str(i) + '.xml', encoding = 'utf-8')
  else:
    f = io.open(sys.argv[1] + '.xml', encoding = 'utf-8')
  text = f.read()
  f.close()

  matches = re.findall("<parse>(.*)</parse>", text)

  for match in matches:
    tree.write(match + '\n')

tree.close()

