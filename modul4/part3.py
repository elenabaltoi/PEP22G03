#exceptii

def create_fraction(number):
    try:
    # result=number/1
        if number >= 1:
            result=1/number
        else:
            result=0
            print("Number is small, can't use it")
    except:
        result="infinit"
        print("Can't use 0 devider")

        return result

print(create_fraction(3))
print(create_fraction(-1))
print('done')