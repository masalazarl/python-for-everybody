#Assingnment 6.5

text = "X-DSPAM-Confidence:    0.8475"
at_text = text.find("0")
num = float(text[at_text:])
print(num)
 
#Assingnment 7.1

#fname = input("Enter file name: ")
#fh = open(fname)
fh = open("words.txt") #file name
for line in fh:
    fhand = fh.read()
    print(str(fhand.strip()).upper())

#Assingnment 7.2

#fname = input("Enter file name: ")
#fh = open(fname)
fh = open("mbox-short.txt") #file name
count = 0
n = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1 
        text = line.find("0")
        num = float(line[text:])
        n = n + num
avg = n/count
print("Average spam confidence:", avg)

#Assingnment 8.4

#fname = input("Enter file name: ")
#fh = open(fname)
fh = open("romeo.txt") #file name
lst = list()
for line in fh:
    t = line.rstrip()
    new_lst = t.split()
    for word in new_lst: 
        if word not in lst:
            final_lst = lst.append(word)
print(sorted(lst))

#Assingnment 8.5 

#fname = input("Enter file name: ")
#fh = open(fname)
fh = open("mbox-short.txt") #file name
count = 0
for line in fh:
    t = line.rstrip()
    lst = t.split()
    if len(lst) < 3 or not line.startswith("From"):
        continue
    count = count + 1
    print(lst[1])
    
print("There were", count, "lines in the file with From as the first word")

#Assingnment 9.4 

#fname = input("Enter file name: ")
#fh = open(fname)
fh = open("mbox-short.txt") #file name
counts = dict()
final_lst = []
biggerword = None
biggercount = None
for line in fh:
    t = line.rstrip()
    lst = t.split()
    if len(lst) < 3 or not line.startswith("From"):
        continue
    final_lst.append(lst[1])

for word in final_lst:
    counts[word] = counts.get(word, 0) + 1

for word,count in counts.items(): 
    if biggercount is None or count > biggercount: 
        biggerword = word
        biggercount = count

print(biggerword, biggercount)

#Assingnment 10.2

#fname = input("Enter file name: ")
#fh = open(fname)
fh = open("mbox-short.txt") #file name
counts = dict()
final_lst = []
for line in fh:
    t = line.rstrip()
    lst = t.split()
    if len(lst) > 3 and line.startswith("From"):
        hr = lst[5].split(':')
        counts[hr[0]] = counts.get(hr[0], 0) + 1

for k,v in counts.items():
    final_lst.append((k,v))

final_lst.sort()

for k,v in final_lst:
    print(k,v)


