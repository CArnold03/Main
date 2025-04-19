word='brontosaurus'
d=dict()
for char in word:
    if char not in d:
        d[char]=1
    else:
        d[char]=d[char]+1
print(d)
print(d['s'])
for key in d:
    print(key, d[key])
lst=list(d.keys())
print(lst)
lst.sort()
print(lst)
