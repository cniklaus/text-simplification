"""
  Created on August 22, 2017

  Replace all digits with '9'
"""

import os, logging, sys, datetime, time
import glob, io, re
#import nltk

#from nltk.corpus import PlaintextCorpusReader

start_time = time.time()

timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

print timestamp

logging.basicConfig(
  format = '%(asctime)s : %(levelname)s : %(message)s',
  level = logging.INFO
)

directory = '/home/sam/OpenNMT/data_nonums/'
paths = os.listdir(directory)

#reader = PlaintextCorpusReader(directory, '.*_unk.txt')

for path in paths:
  for files in os.listdir(directory + path + '/'):
    print [fp for fp in os.listdir(directory + path + '/') if 'unk.txt' in fp]
    with io.open(directory + path + '/' + files, encoding='utf-8') as f:
      for line in f:
        contents = line

        # find all digit occurrences
        for digits in re.findall('((?<=\W)|^)(\d+s*(?!(\-*[a-zA-Z]\-*\s*))(?=\W))', contents):
          temp = re.sub('\d', '9', digits[1]) # placeholder for matching groups
          contents = re.sub(digits[1], temp, contents, count=1) # replace digits with '9'
          del temp
        contents = contents.encode('utf-8')

        # save changes to outfile
        with open(directory + path + '/' + files + '_processed', 'a+') as outfile:
          outfile.write(contents)
          del contents

# print execution time
print("--- Execution time: %s minutes ---" % ((time.time() - start_time)/60))

