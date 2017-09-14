from pythonds.basic.stack import Stack
import io

out = io.open("simple/val_simple_tree.processed.txt", mode='a+', encoding='utf-8')

with io.open('simple/val_simple_tree.txt', encoding='utf-8') as parse:
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
    out.write(resultString)

