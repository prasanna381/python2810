value = 10
if value>0:
    print(f"the number is {value} positive")

    num= 30
    if num>=10 and num<=20:
        print(f"given num{num} is in range")
    
    value=-12
    if value>0:
        print(f"the number is {value}  positive")
    else:
        print(f"the number is {value} negative")

#input-->for taking inputs
    email=input(f"enter your email:")
    print(f"welcome{email}")
    age = int(input(f"enter your Age:"))
# checkvote eligibility
    if  age <= 18:
        print(f"you can vote")
    else:
        print(f"you cannot vote ")

#type coversion
a=1
b=3.2
c=a+b
print(type(c)) 


d=2.4
e= int(d)
print(type(e))
print(e) 

#type casting
x=100
y=float(x)
print(type(y))
print(y)

#checking your vote using ternary operator
#value_if_true if condition else_value_if
age = int(input(f"enter your Age:"))
status= "you can vote" if age>=18 else "you cannot vote"
print(status)

avg_score = int(input("Enter your avg_score"))
if avg_score>=90:
    print("a grade")
elif avg_score>=75:
    print("b grade")
elif avg_score>=65:
    print("c grade")
elif avg_score>=55:
    print("d grade")
elif avg_score>=45:
    print("e grade")
else:
    print("fail")

#match _case(3x++)
choice= int(input("enter your choice"))
match choice:
    case 1:
        print("one" )
    case 2:
     print ("two")
    case 3:
        print("three")
    case 4:
        print("four")
    case _:
        print("invalid")

#nested conditions
age=20
has_id = True
if age >=21:
    if has_id:
        print("you are allowed to enter")
    else:
        print("you need id to enter")
    #else:
        #print("you are young to enter")