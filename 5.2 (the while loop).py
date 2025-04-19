largest = None
smallest = None
while True:
    try:
        num = input("Enter a number, when done type 'done': ")
        if num == 'done':
            break
        n=int(num)
    except:
        print('Invalid input')
    if largest==None:
        largest=n
    if smallest==None:
        smallest=n
    if largest<n:
        largest=n
    if smallest>n:
        smallest=n
print("Maximum is", largest)
print("Minimum is", smallest)
