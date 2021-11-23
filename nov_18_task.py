#creating the tuples
a=(1,4,5,6,7,8)
b=(5,6,7,8,9)

#finding the common elements
p=a and b
print(p)

#concanatenate both tuples
c=a+b
print("the concatenated tuple is: ",c)

#to remove the duplicate values
d=tuple(set(c))
print("the tuple without duplication is: ",d)

#to find the index value of 9
print(d.index(9))

#multiply above elements 3 times
mul= 3*d
print(mul)



#SETS
#creating the sets
set1={7,8,9,1,2,3,4,5,0}
set2={4,5,6,0}
print(set2.issubset(a))

#common_elements
com=set1.intersection(set2)
print(com)

#remove 8
set1.remove(8)
print(set1)
#set2.remove(8)
print(set2)

#discard 10
set1.discard(0)
print(set1)
set2.discard(0)
print(set2)


#DICTIONARY
dict={1:["english","maths","science"], 2:[10,20,30], 3:["bio-botany","bio-zoology","Algebra"]}
print(dict)
print(dict.keys())
print(tuple(dict.keys()))

#get the values
a=dict.get('3')
print(a)
b=dict.get("algebra")
print(b)
c=dict.get("histroy")
print(c)





Li1 = [2,3,4,5,6,7,"python",10]

#on
print(Li1[6])
print(Li1[:2])
print(Li1[6][:2])

Li1 = [2,3,4,5,6,7,"python",10, [10,12,23,24,25]]
print(Li1[8])
print(Li1[8][4])
