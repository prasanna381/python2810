
#''or"" or """ using in strings
data_1 = "hello"
data_2 =  'hello'
data_3 = """hello"""
data_4 = '''hello'''

print(data_1)
print(data_2)
print(data_3)
print(data_4)

# multi line strings--> """
python_desc = """Python is a high-level, general-purpose programming language.
              Its design philosophy emphasizes code 
              readability with the use of significant indentation"""

question = "how are you?"
#using a single quote inside single quotes not valid
#if you want add single quote inside ,used in double quotes
#answer   = i'm fine

answer = "i'm fine"
print(answer)

answer = 'im " good"'
print(answer)
# if you need to use both ''' and """
answer =""" i'm fine and "good" """
print(answer)

answer ='''i'm fine and "good" '''
print(answer)

#accessing
text = "python"

#python using indexing and accessing individual characters
print(text[0])
print(text[-1])
print(text[3])

#invalid range
#print(text[10]) # string index out of range
#text ='python'
#using for loop
text ='python' 
for i in text:
    print(i)

text ='python' 
print(text[1])
print(text[2])
print(text[4])

text = "python is very easy to learn"
print(text)
print(text[1])
print(text[3])
print('===')
for i in text:
   print(i)
print('===')
#slicig
text = "python"
print(text[0:3])#pyt
print(text[2:5])#tho
print(text[1:])#ython
print(text[:1])#p
print(text[:])
print("===")
#if step is not defined, by default step 1
print(text[0:4:1])
print(text[0:4:2])

text = 'python is very easy to learn'
print(text[0:16:4])

#for negative indexing default step 1
text ="python"
print(text[-3:-1])#ho
print(text[-4:-1:1])#
print(text[-4:-1:-1])
#print(text[1:4:0])#ValueError: slice step cannot be zero

#typical use case of backward step
text = 'python'
print(text[::-1])

#ohty
print(text[-2:-5:1])
print(text[-2]+text[-3]+text[-5])

#string immutability
text ="python"
new_text ='j' + text[1:]
print(new_text)

#concat & Repeat
#concat --> join multiple strings
str ='hi' 
print(str*5)
#string operataions and string methods
print(dir(str))

mobile_number = input("Enter your number:")
valid_number = mobile_number.isdigit()
print(valid_number)

pan_number = input("enter your pan number:")
valid_pan_number = pan_number.isalnum()
fomart_valid_number = pan_number.upper()
print(fomart_valid_number)




