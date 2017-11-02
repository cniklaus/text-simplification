"""
2 Nov, 2017
UC Davis Computational Linguistics Lab

Program to parse datasets using CoreNLP server.

In order to maintain consistent line counts between aligned text files,
this program forces all parse output from a single source line
to a single output line, regardless of parse output.

Usage: python3 parse_coreNLP.py input_filename output_filename
"""

from pycorenlp import StanfordCoreNLP
import io, sys, re

if __name__ == "__main__":
  nlp = StanfordCoreNLP('http://localhost:9000') #load CoreNLP server
  outfile = io.open(sys.argv[2], mode='a+', encoding='utf-8') #open new file for output
  
  with io.open(sys.argv[1], encoding='utf-8') as textfile: #open source file to be parsed
    for line in textfile: #iterate through lines of source file and parse each one
      text = str(line) # convert line to a string
      # call CoreNLP on line of text - store resulting output as 'output_parse'
      output_parse = nlp.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,parse', 'outputFormat': 'xml'})
      if output_parse.encode('utf-8') == "": #if CoreNLP did not produce any output for the input text
        outfile.write('\n') #write a blank line to outfile to maintain source and output alignment
      else:
        strings = re.findall("<parse>[^<]*</parse>", str(output_parse.encode('utf-8'))) #extract the sentence parse from CoreNLP output
        concat_string = "" #variable to concatenate outputs in case of multiple sentences in a line
        for string in strings:  #process all parse trees identified by regex 
          string = string.lstrip('<parse>') #remove 'parse' tags from beginning and end
          string = string.rstrip('</parse>')
          string_array = re.split('\s+', string) #split on space to delete excess whitespace
          strip_array = []
          for word in string_array: #remove '\\n' tags from all words
            strip_array.append(word.rstrip('\\\\n'))
          for word in strip_array: #reconstitute trees.  If multiple trees created by CoreNLP, combine into single string
            concat_string += (word.encode('raw_unicode_escape').decode('utf-8') + ' ')
        outfile.write(concat_string + '\n') #write concatenated output trees to outfile
