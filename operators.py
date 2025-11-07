#operators
#arthematic operators
 
num1= 5
num2= 6
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1%num2)
print(num1//num2)
print(num1/num2)


#compound assignment operator
num=10
#num= num+5
num += 5
print(num)
num*=2
print(num)

#comparison /relational operators
num1=2
num2=3
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)
print(num1==num2)

#logical opertors
a=1
b=2
c=3
d=4
 
result_and= a>b and b<c
print(result_and)
result_or=a<b or b>d
print(result_or)
result_not=b>d
print(result_not)

#membership operator
text='python is eazy'
is_z_present="z" in text
print(is_z_present)

list=[1,23,4]
is_5_present=5 in list
print(is_5_present)

is_z_not_present='z' not in text
print(is_z_not_present)

#identity operators
num1=10
num2=10
print(id(num1))
print(id(num2))
print(num1 is num2)

list_nums1=[10,20]
list_nums2=[10,20]
print(id(list_nums1))
print(id(list_nums2))
print(list_nums1 is list_nums2)
print(list_nums1 is not list_nums2)

#bitwise operator
a= 5
b= 3
resultand =a&b
print(resultand)

resultor=a/b
print(resultor)

resultxor=a^b
print(resultxor)

resultnot=~b
print(resultnot)

a=3
print(3<<2)
print(3<<1)
print(3<<3)

a=3
print(3>>2)
print(3>>1)
print(3>>3)




