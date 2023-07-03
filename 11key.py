import random

cdkey = str(random.randint(1, 999)).zfill(3)
cdkey_third = list(cdkey)[2]
print("3rd digit:", cdkey_third)


if int(cdkey_third) + 1 >= 10: # for 11key cdkey or sitenr, the last digit is the 3rd + 1 or 2. There are no exceptions
    cdkey_last = 0
    print("Last digit: ", cdkey_last)
else:
    cdkey_last = int(cdkey_third) + 1
    print("Last digit: ", cdkey_last)

cdkey = str(cdkey) + str(cdkey_last)

# mod7 generation as usual
def is_divisible_by_7(): # This function checks if mod7 is divisible by 7, which is required for the mod7 algo. The last digit also can't be >= 8.
    #print(mod7)
    mod7_calc = [int(x) for x in str(mod7)]
    #print("mod7_calc_: ", mod7_calc)
    #print("mod7_calc length: ", len(mod7_calc))
    if len(mod7_calc) != 7:
        return False
    elif mod7_calc[6] >= 8:
        return False
    
    mod7_calc_end_float = str((mod7_calc[0] + mod7_calc[1] + mod7_calc[2] + mod7_calc[3] + mod7_calc[4] + mod7_calc[5] + mod7_calc[6]) / 7)
    print("mod7_calc_end_float: ", mod7_calc_end_float)
    mod7_calc_end_split = mod7_calc_end_float.split('.')
    #print(mod7_calc_end_split)

    if len(mod7_calc_end_split[1]) != 1:
        return False
    elif int(mod7_calc_end_split[1]) != 0:
        return False
    else:
        mod7_calc_end = mod7_calc_end_split[0]
        print(mod7_calc_end_split, " has no decimal point!")
        return True


mod7 = random.randint(0000000, 9999999)
while not is_divisible_by_7():
    mod7 = random.randint(0000000, 9999999)
    
print("Valid CDkey: ", cdkey)
print("Valid mod7: ", mod7)

print()
key = f"Valid 11key: {cdkey}-{mod7}"
print(key)