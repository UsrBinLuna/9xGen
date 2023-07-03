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

def is_divisible_by_7(): # This function checks if Z is divisible by 7, which is required for the mod7 algo.
    #print(z)
    z_calc = [int(x) for x in str(z)]
    #print("z_calc_: ", z_calc)
    #print("z_calc length: ", len(z_calc))
    if len(z_calc) != 6:
        return False
    z_calc_end_float = str((z_calc[0] + z_calc[1] + z_calc[2] + z_calc[3] + z_calc[4] + z_calc[5]) / 7)
    print("z_calc_end_float: ", z_calc_end_float)
    z_calc_end_split = z_calc_end_float.split('.')
    #print(z_calc_end_split)

    if len(z_calc_end_split[1]) != 1:
        return False
    elif int(z_calc_end_split[1]) != 0:
        return False
    else:
        z_calc_end = z_calc_end_split[0]
        print(z_calc_end_split, " has no decimal point!")
        return True


z = random.randint(000000, 999999)
while not is_divisible_by_7():
    z = random.randint(000000, 999999)

c = random.randint(00000, 99999)
while True:
    if len(str(c)) < 5:
        c = random.randint(00000, 99999)
    else:
        break


key = f"Valid OEM Key: {day}{year}-OEM-0{z}-{c}"


print("day: ", day, ", year: ", year, ", z: ", z, ", c: ", c )

print()
print(key)
