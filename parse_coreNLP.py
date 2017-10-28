from pycorenlp import StanfordCoreNLP
import io, sys, re

if __name__ == "__main__":
  nlp = StanfordCoreNLP('http://localhost:9000') #load CoreNLP server
  outfile = io.open(sys.argv[2], mode='a+', encoding='utf-8') #open new file for output
  
  with io.open(sys.argv[1], encoding='utf-8') as textfile: #open source file to be parsed
    for line in textfile: #iterate through lines of source file and parse each one
      text = str(line) # convert line to a string
      print(text.encode('utf-8'))
      dummy = input('Press <ENTER> to continue')
      output_parse = "" # set initial value of parsed output
      # call CoreNLP on line of text - store resulting output as 'output_parse'
      output_parse = nlp.annotate(text, properties={'annotators': 'tokenize,ssplit,pos,parse', 'outputFormat': 'xml'}).decode('utf-8','ignore')
      print("BEGIN OUT " + output_parse + "END OUT")
      if output_parse == "": #if CoreNLP did not produce any output for the input text
        outfile.write('\n') #write a blank line to outfile to maintain source and output alignment
      else:
        strings = re.findall("<parse>(.*)</parse>", str(output_parse)) #extract the sentence parse from CoreNLP output
        print(strings)
        concat_string = "" #variable to concatenate outputs in case of multiple sentences in a line
        if len(strings) > 1: #if more than one sentence in a line
          for string in strings: 
            concat_string += (string + ' ') #concatenate the output sentences
          outfile.write(concat_string + '\n') #write concatenated output sentences to outfile
        else:
          outfile.write(strings[0] + '\n') #if only one sentence - write its parse to outfile

