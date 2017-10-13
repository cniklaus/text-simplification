"""
October 11, 2017

UC Davis Computational Linguistics Lab

Script to duplicate tags in CoreNLP-formatted files
that have been stripped of XML tags

Usage: python preprocess_parse.py infile_name outfile_name
"""

from pythonds.basic.stack import Stack
import io, sys

outfile = io.open(sys.argv[2], mode='a+', encoding='utf-8')

with io.open(sys.argv[1], encoding='utf-8') as parse:
  for line in parse:
    stack = Stack()
    resultString = ""
    tokens = line.split()
    for token in tokens:
      if '(' in token:
        stack.push(token)
        resultString += (token + ' ')
      elif ')' in token:
        for i in range(len(token)-1):
          if token[i] == ')':
            match = stack.pop()
            resultString += (' ' + token[i] + match[1:])
          else:
            resultString += token[i]
        if ')' in token[len(token)-1]:
          match = stack.pop()
          resultString += (' ' + token[len(token)-1] + match[1:] + ' ')
        else:
          resultString += token[len(token)-1]
      else:
        resultString += (token + ' ')
    resultString += '\n'
    outfile.write(resultString)

