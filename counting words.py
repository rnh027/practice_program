name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    words = line.split()
    if line.startswith("From") and len(words)==2:
        count[words[1]] = count.get(words[1],0)+1
mail = None
cnt = None
for m,c in count.items():
    if cnt is None or c>cnt:
        mail = m
        cnt = c
print(mail,str(cnt))
