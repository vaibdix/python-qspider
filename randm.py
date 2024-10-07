from random import *

def OTP():
    otp=" "
    for i in range(6):
        otp+=str(randint(0,9))
    print(otp)
OTP()

def OTP_Combi():
    otp=" "
    for i in range(2):
        otp+=str(randint(0,9))
    for j in range(2):
        otp+=chr(randint(65,90))
    for k in range(2):
        otp+=chr(randint(97,122))
    print(otp)
OTP_Combi()