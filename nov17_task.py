#create an empty list
a=list()
print(type(a))
b=[]
print(type(b))

#concatenate with [5,6,7,8]
c=[5,6,7,8]
print(b+c)
print(type(c))

#adding elements to the list
d= c+[8,9,1,5,6,7,8,1]
print(d)

#the frequency of the 8
print(d.count(8))

#finding the min,max and sum
print(sum(d))
print(min(d))
print(max(d))

#finding the mean of the list
print(sum(d)/2)

print(len(d))
median=len(d) //2
print(d[median])

mean=sum(d)/len(d)
print(mean)

d.sort()
print(d)
median=len(d)//2
print(d[median])
