#Arguments
def cube(number):
    return number*number*number
def divby3(number):
    if number%3==0:
        return cube(number)
    else:
        return False
print(divby3(9))
print(divby3(4))