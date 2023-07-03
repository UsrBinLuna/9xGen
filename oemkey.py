import random

day = str(random.randint(1, 366)).zfill(3)

y = str(random.choice([95, 96, 97, 98, 99, 0, 1, 2]))
def getyear(): # The year string must be 2 digits long. This function checks and corrects it if its 1 long.
    #print(len(str(y)))
    
    if len(str(y)) == 1:
        year2 = "0" + y
        #print("y2: ", year2)
    else:
        year2 = y
    
    return year2

year = getyear()

def is_divisible_by_7(): # This function checks if mod7 is divisible by 7, which is required for the mod7 algo.
    #print(mod7)
    mod7_calc = [int(x) for x in str(mod7)]
    #print("mod7_calc_: ", mod7_calc)
    #print("mod7_calc length: ", len(mod7_calc))
    if len(mod7_calc) != 6:
        return False
    mod7_calc_end_float = str((mod7_calc[0] + mod7_calc[1] + mod7_calc[2] + mod7_calc[3] + mod7_calc[4] + mod7_calc[5]) / 7)
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


mod7 = random.randint(000000, 999999)
while not is_divisible_by_7():
    mod7 = random.randint(000000, 999999)

c = random.randint(00000, 99999)
while True:
    if len(str(c)) < 5:
        c = random.randint(00000, 99999)
    else:
        break


key = f"Valid OEM Key: {day}{year}-OEM-0{mod7}-{c}"


print("day: ", day, ", year: ", year, ", mod7: ", mod7, ", c: ", c )

print()
print(key)
