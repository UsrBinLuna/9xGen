import random


invalid_nrs = [333, 444, 555, 666, 777, 888, 999]

# Check if Site N° is valid. It cannot be 333, 444, 555, 666, 777, 888 or 999.
def valid_sitenr():
    for x in invalid_nrs:
        if sitenr in invalid_nrs:
            return False
        else:
            return True

sitenr = str(random.randint(0, 998)).zfill(3)
while not valid_sitenr():
    sitenr = str(random.randint(0, 998)).zfill(3)



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
    
print("Valid Site N°: ", sitenr)
print("Valid mod7: ", mod7)

print()
key = f"Valid 10key: {sitenr}-{mod7}"
print(key)