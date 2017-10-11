"""
October 11, 2017

UC Davis Computational Linguistics Lab

Script to remove POS tags from words in preprocessed CoreNLP files,
leaving phrase-level tags intact

"""

import io, re

output = io.open('simple/pos_removed/test_simple_tree.txt', mode = 'a+', encoding = 'utf-8')

with io.open('simple/test_simple_tree.processed.txt', encoding='utf-8') as source:
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

    
