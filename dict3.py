counts = dict()
names = ['aa' , 'bb' , 'cc' , 'AA' , 'CC' , 'DD']
for namess in names:
    if namess not in counts:
        counts[namess] = 1
    else:
        counts[namess] = counts[namess] + 1
print(counts)
