#task1:

#positive or negative
n=int(input("enter the value you have to check: "))
if(n<=0):
    print(" th number you have entered is NEGATIVE")
elif(n>=0):
    print("the number you have entered is POSITIVE")
    
    
#task2:
#even or odd:
m=int(input("enter the value you have to check:  "))
if(m%2 == 0):
    print("the number is EVEN")
elif(m%2!= 0):
    print("the number is ODD")

    
#task3:
#palindrome or not
p=input("enter the string:  ")
rev= p[::-1]
if(p == rev):
    print("{} is a palindrome".format(p))
else:
    print("{} is not a palindrome".format(p))
    
    
#taskk4: (middle letter vowel)
a=input("enter the string: ")
m=a[len(a)//2]
print(m)
if m in "aeiou":
    print("It is a vowel")
else:
    print("not a vowel")
    
    
#task5:(middle ascii value odd or even)    
n=ord(m)
if(ord(m)%2 == 0):
   print(" the ASCII value is even")
else:
    print(" the ASCII value is odd")

    
 #task6:   
#length of the string odd or even:
o=input("enter the string:  ")
op=(len(o))
if(op % 2 == 0):
    print("the len of the string is even")
else:
    print("the len of the string is odd")

#task7:
#marks
mark=int(input("enter the marks: "))
if(0 <= mark and mark <= 100):
    print("the mark is valid")
    if mark >=90 and mark >=100:
        print("A grade")
    elif mark >=80 and mark >=89:
        print("B grade")
    elif mark >=70 and mark >=79:
        print("C grade")
    elif mark >=60 and mark>=69:
        print("D grade")
    elif mark>=50 and mark >=59:
        print("E grade")
        
      
    elif mark > 0 and mark < 50:
        print("Fail mark")
    
else:
    print("the mark is invalid")
    
    
#task8         
#hackerrank create a function
def is_leap(year):
    leap = False
    if year%400==0:
        leap = True;
    elif year%4 == 0 and year%100 !=0:
        leap = True;
    return leap
year = int(input("enter the year"))
print(is_leap(year))


#task9
#hackerrank if else problem
n=int(input("enter the number:  "))
if(n%2!=0):
    print("weird")
else:
    if(n>2 and n<5):
        print("Not weird")
    elif(n>6 and n<20):
        print("Weird")
    elif(n>20):
        print("Not Weird")


#task11:
#whether the number is armstrong number or not
num=int(input("enter the number to be checked: "))
l=len(str(num))
sum=0
temp=num;
while (temp>0):
    digit=temp%10
    sum+= digit **3
    temp = temp //10

if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
             
#task12:
#whether the length is odd or even
li=[123, 124, 125,130,131]
i=len(li)
if(len(li)%2 ==0):
    print (" the lenght is even")
else:
    print(" the length is odd")



#range function tasks
for i in range(0,75,5):
        print(i)
print("--------------------")
for k in range(0,72,8):
        print(k)
print("--------------------")
for j in range(75,0,-5):
     print(j)
print("--------------------")
for a in range(96,72,-8):
        print(a)




