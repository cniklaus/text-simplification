import io

dest1 = io.open('sscorpus_norm.txt', mode='a+', encoding='UTF-8')
dest2 = io.open('sscorpus_simp.txt', mode='a+', encoding='UTF-8')

with io.open('sscorpus', encoding = "UTF-8") as f:
  for line in f:
    sent_list = line.split('\t')
    dest1.write(sent_list[0] + '\n')
    dest2.write(sent_list[1] + '\n')
	

