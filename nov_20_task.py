#task2:

a={"python":[1994,"interpreter","scripting","development",3], "java":[1992,"compiler","scripts","frontend/backend",10],"c":[1980,"core","scripting","Both",20]}
print(a["python"][4])

print(a["python"][0])

l=(a["java"][3])
print(l[9:])

print(a["c"][1])


#task3:

#positive or negative
n=int(input("enter the value you have to check: "))
if(n<=0):
    print(" th number you have entered is NEGATIVE")
elif(n>=0):
    print("the number you have entered is POSITIVE")

#even or odd:
m=int(input("enter the value you have to check:  "))
if(m%2 == 0):
    print("the number is EVEN")
elif(m%2!= 0):
    print("the number is ODD")

#palindrome or not
p=input("enter the string:  ")
rev= p[::-1]
if(p == rev):
    print("{} is a palindrome".format(p))
else:
    print("{} is not a palindrome".format(p))


#task4
#remove duplicates from a and converting to list again
l=[1,2,3,4,5,1,1,1,2,3,4,5,1]
l=[1,2,3,4,5,1,1,1,2,3,4,5,1]
print(set(l))
print(list(set(l)))


