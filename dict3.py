counts = dict()
names = ['aa' , 'bb' , 'cc' , 'aa' , 'cc' , 'dd']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
