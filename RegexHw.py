import re
f=open('RegexData.txt')
num=[]
add=0
for line in f:
    g=re.findall('[0-9]+', line)
    num=num+g
count=0
for nu in num:
    n=int(nu)
    add=add+n
    count+=1
print('counted: ', count)
print('added: ', add)
