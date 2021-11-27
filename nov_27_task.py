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

