import random, io



list1 = random.sample(range(1, 167000), 4000)
list2 = list1[0:1999]
list3 = list1[2000:3999]


line_count = 1
filename = "normal.aligned"

f1 = io.open("/home/khgkim/torch/OpenNMT/data2/data3" + '/test.txt', mode='a+', encoding='utf-8')
f2 = io.open("/home/khgkim/torch/OpenNMT/data2/data3" + '/val.txt', mode='a+', encoding='utf-8')
f3 = io.open("/home/khgkim/torch/OpenNMT/data2/data3" + '/train.txt', mode='a+', encoding='utf-8')

with io.open("/home/khgkim/torch/OpenNMT/data2/data3" + '/' + filename, encoding='utf-8') as s:
  for line in s:
    stripped = line.split('\t')[2]
    if line_count in list2:
      f1.write(stripped + '\n')
    elif line_count in list3:
      f2.write(stripped + '\n')
    else:
      f3.write(stripped + '\n')
    line_count += 1
