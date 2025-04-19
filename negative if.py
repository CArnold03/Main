hrs = input("Enter Hours:")
rte=input("Enter Rate:")
r=float(rte)
h=float(hrs)
if h>0.0:
    if r>0.0:
        o=1.5
        d=21
        if h>40 and h<50:
            print(40*r+((h-40)*(r*o)))
        elif h<=40:
            print(h*r)
        else:
            print(h*d)
    else:
        print("positives, please")
else:
    print("positives, please")
