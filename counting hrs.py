name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = list()
for line in handle:
    if line.startswith("From") and ":" in line:
        i = line.find(':')
        count.append(int(line[i-2:i]))
tot = dict()
for h in count:
    tot[h] = tot.get(h,0)+1
for k,v in tot.items():
    print(k,v)
