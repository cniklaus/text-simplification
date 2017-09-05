"""
preprocess_parse.py
UC Davis Computational Linguistics Lab
Written 05 Sept. 2017 by Sam Davidson
Input: Standford CoreNLP format parsed sentences - 1 per line
Output: Parsed sentences with part of speech tags duplicated on
	both opening and closing parentheses.
"""
from pythonds.basic.stack import Stack
import io

#output file to be created - update as needed
out = io.open("simple/val_simple_tree.processed.txt", mode='a+', encoding='utf-8')

#open source file - update as needed
with io.open('simple/val_simple_tree.txt', encoding='utf-8') as parse:
  for line in parse: #one parse tree per line
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
    out.write(resultString)

