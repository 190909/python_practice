a=input("enter the string: ")
m=a[len(a)//2]
print(m)
if m in "aeiou":
    print("It is a vowel")
else:
    print("not a vowel")
n=ord(m)
if(ord(m)%2 == 0):
   print(" the ASCII value is even")
else:
    print(" the ASCII value is odd")

#odd or even:
o=input("enter the string:  ")
op=(len(o))
if(op % 2 == 0):
    print("the len of the string is even")
else:
    print("the len of the string is odd")


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
    
              
