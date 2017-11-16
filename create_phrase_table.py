#UC Davis Computational Linguistics Lab
#16 November, 2017

#Create an OpenNMT Phrase Table from tokenized source data.

#Usage: create_phrase_table.py input_file.txt output_file.txt

import io, sys

tokens = []

outfile = io.open(sys.argv[2], mode='a+', encoding='utf-8')

with io.open(sys.argv[1], encoding='utf-8') as infile:
  for line in infile:
    line_toks = line.split()
    for tok in line_toks:
      if tok not in tokens:
        tokens.append(tok)

for tok in tokens:
  outstring = tok + "|||" + tok
  outfile.write(outstring + '\n')
