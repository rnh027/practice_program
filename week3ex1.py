import re

file = open("original_data.txt")
total = 0
for line in file:
    #extract number from each line and converted into list of integer
    number = list(map(int,re.findall('[0-9]+',line)))
    #store sum value of each line and add to total
    total += sum(number)
print(total)
