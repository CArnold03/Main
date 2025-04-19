nums=[3,5,4,7,1,2]
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        nums[i], nums[i+1]= nums[i+1], nums[i]
print (nums)
num=[3,5,4,7,1,2]
i=0
a=0
while i<len(num)-1:
    while a<len(num)-1:
        if num[a]>num[a+1]:
            num[a], num[a+1]=num[a+1], num[a]
        a+=1
    a=0
    i+=1
print (num)
