"""
October 11, 2017

UC Davis Computational Linguistics Lab

Script to remove POS tags from words in preprocessed CoreNLP files,
leaving phrase-level tags intact

Usage: python remove_pos_tags.py infile_name outfile_name
"""

import io, re, sys

output = io.open(sys.argv[2], mode='a+', encoding='utf-8')

with io.open(sys.argv[1], encoding='utf-8') as source:
  for line in source:
    result = ''
    toks = line.split()

    for i in range(len(toks)-1):
      if '(' not in toks[i] and ')' not in toks[i] and toks[i] != '':
        toks[i-1] = ''
        toks[i+1] = ''
    for i in range(len(toks)):
      if toks[i] != '':
        result += toks[i] + ' '
    output.write(result + '\n')

