def mean(l):
        m=0.0
        c=0
        for i in l:
                m=m+i
                c=c+1
        m=m/c
        return m
def median(l):
        m=0
        c=0
        for i in l:
                c=c+1
                a=c//2
        if a%2==0:
                m=l[a-1]
        else:
                m=l[a]
        return m
def per(i, l):
        count=0
        for num in l:
                if i<num:
                        count=count+1
        p=100*count/len(l)
        return p
def quartile(l):
        q=0
        c=0
        for i in l:
                c=c+1
        a=c//4
        if a%2==0:
                q=l[a-1]
        else:
                q=l[a]
        return q
fh=open("StudentExercise.csv")
lst=[]
next(fh)
for line in fh:
        word=line.split(',')[0]
        if word!='':
                i=float(word)
                lst.append(i)
                lst.sort()
mea=mean(lst)
med=median(lst)
percent=per(mea, lst)
qua=quartile(lst)
print("Mean is: ", mea)
print("Percent is: ", percent)
print("Median is: ", med)
print("1st Quartile is: ", qua)
