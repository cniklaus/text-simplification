# 01 Sept, 2017
# UC Davis Computational Linguisitics Lab
# Author: Sam Davidson

# Program to locate parsed sentences in 
# Stanford CoreNLP XML formated files and extract same.


import re
import io

tree = io.open('normal/train_normal_tree.txt', 'a+', encoding = 'utf-8')

for i in range(10):
  f = io.open('normal/train/train_normal' + str(i) + '.xml', encoding = 'utf-8')
  text = f.read()
  f.close()

  matches = re.findall("<parse>(.*)</parse>", text)

  for match in matches:
    tree.write(match + '\n')

tree.close()
