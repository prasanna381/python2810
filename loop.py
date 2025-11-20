#loop statements
count=1
while count <=5:
    print(count)
    count+=1

#while True:
#print("infinite loop")
#best use case to undeerstand while
password= "123"
user_input =""
while user_input != password:
      user_input= input("enter your password")
print('access granted')

#for loop statements
text = "python"
for i in text:
  print(i)
#we cannot use for iterable and non iterable

#num=10
#for i in num:
#print(i)

num=[10]
for i in num:
    print(i)

just_num = 10
print(dir(just_num))

list_num =[10]
print(dir(list_num))
for i in list_num:
    print(i)

for i in range(10):
    print("hi")

for i in range(3,10):
    print("hello")

for i in range(1,10,2):
    print(i)

i= 2 
while i<=20:
    print(i)
    i+=2


while i % 2 == 0:
    print(i)
    i+=1

#nested for loop
#math table

for i in range(1,6):
  for j in range(1,11):
    print(f"{i}*{j} = {i*j}")

#nested while loop
#math table
#break
for i in range(5):
    if i == 3:
        break 
    print(i)
print('=====')
#continue
for i in range(5):
    if i== 3:
      continue #skip loop when i=3
    print(i)

#pass
    if (5>9):
        pass

  
