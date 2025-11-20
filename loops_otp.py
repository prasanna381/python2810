import random
otp = random.randint(1000,9999)
print(otp) 

attempts = 3
while attempts:
    user_otp = int(input("enter otp: "))
    if len(str(user_otp !=4)):
        print("otp must be 4 digit only")

    if user_otp == otp:
        print("Correct OTP -success")
        break
    attempts-=1
else:
    print("Maximum attempts done,try after 24hours")