#task1:
#separating odd and even lists
a=[2,3,4,6,7,8,9,10,11]
oddlist=[]
evenlist=[]
for i in a:
    if(i% 2 == 0):
        evenlist.append(i)
    else:
        oddlist.append(i)
   
print(evenlist)
print("the number of even elements is :",len(evenlist))
print(oddlist)
print("the number of odd elements is:",len(oddlist))


  
 #task2:
#separating the positive and negative elements
b=[-2,-3,4,5,6,8,9,0,0,1,2,3,5,-5,-6]
positive=[]
negative=[]
zero=[]
for i in b:
    if(i>0):
        positive.append(i)
    elif(i<0):
        negative.append(i)
    elif(i==0):
        zero.append(i)
print(positive)
print("the no. of positive elements is:",len(positive))
print(negative)
print("the no. of negative elements is:",len(negative))
print(zero)
print("the no. of zero is:",len(zero))
        

  
#task3:
#palindrome or not
c=["mom", "dad", "king", "python", "malayalam", "123321", "123"]
yes=[]
no=[]
for i in c:
    if i == i[::-1]:
        yes.append(i)
    else:
        no.append(i)
print(yes)
print("no.of palindromes:",len(yes))
print(no)
print("no.of non palindromes:",len(no))
        

 
#task5:

#task7:
#fibbonacci series:
n=int(input("enter the no.of output: "))
a=0
b=1
if(n==1):
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a = b
        b = c
        print(c)
        
        
#task7:
#fibbonacci series
n=int(input("enter the no.of elements:"))
seq=[0,1]
for i in range(2,n):
    nex=seq[-1]+seq[-2]
    seq.append(nex)
print(seq)



#task8:
#multiples of 10 from 12 to 100
a=12
while(a<=100):
    if(a%10==0):
        print(a)
    a=a+1
    
#multiples of 8 from from 120 to 20
b=120
while(b>=20):
    if(b%8 == 0):
        print(b)
    b= b-1
    
#multiples of 5 from 9 to 40
c=5
while(c<=40):
    if(c%5==0):
        print(c)
    c=c+1

#multiples of 8 from 300 to 200
d=300
while(d>=200):
    if(d%8==0):
        print(d)
    d=d-1


 #task11:
#dynamic list and positive negative
x=[]
positive=[]
negative=[]
zero=[]
n=int(input("enter the length of the list:"))
for i in range(1,n+1):
    k=int(input("value:"))
    x.append(k)
print(x)


for j in x:
    if(j>0):
        positive.append(j)
    elif(j<0):
        negative.append(j)
    elif(j==0):
        zero.append(j)
print(positive)
print("no. of positive elements is:",len(positive))
print(negative)
print("no. of negative elements is:",len(negative))
print(zero)
print("no. of zero is:",len(zero))
  

    
#task12:
n=int(input("enter the number: "))
m=int(input("enter the second number: "))
for i in range(n,m+1):
    if(i%3==0 and i%5==0):
        print(i,"fizzbuzz")
    elif(i%3==0):
        print(i,"fizz")
    elif(1%5==0):
        print(1,"buzz")

        
#task14:
#sum of digits
n=int(input("enter the number :"))
total=0
while(n>0):
    digit=n%10
    total=total+digit
    n=n//10
print("the sum of digits is: ",total)



#task15:
#multiples of the number
n=int(input("enter the number :"))
total=1
while(n>0):
    digit=n%10
    total=total*digit
    n=n//10
print("the sum of digits is: ",total)



#task16:
#factors of a number
n=int(input("enter the number: "))
factors=[]
print("the factors of",n,"are" )
for i in range(1,n+1):
    if(n%i ==0):
        factors.append(i)
print(factors)


#task17
#anagram
a=input("enter the first string: ")
b=input("enter the second string: ")
if(sorted(a)==sorted(b)):
    print("the strings are anagram")
else:
    print("it is not an anagram")
    
    
#task18:
#prime number or not
a=int(input("enter the number:"))
if a>1:
    for i in range(2,int(a/2)+1):
        if(a%i==0):
            print(a,"is not a prime")
            break
    else:
        print(a,"is a prime number")
else:
    print(a,"is a prime")

    
    
   


