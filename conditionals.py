is_male: bool = True
is_tall = True

if is_male and is_tall:
    print("I am a male and tall ")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but you are tall")
else:
    print("Your are neither male nor tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("Num1 is highest " + str(num1))
    elif num2 >= num1 and num2 >= num3:
        print("Num2 is highest " + str(num2))
    else:
        print("Num3 is highest " + str(num3))


max_num(1, 2, 3)


