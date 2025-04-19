fh='mbox-short.txt'
h=open(fh)
count=dict()
for line in h:
        if line[0:5]==('From '):
            c=line.split(' ')
            time=c[2]
            count[time]=count.get(time,0)+1
print(count)
