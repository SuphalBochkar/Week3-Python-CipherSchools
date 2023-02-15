# closures, first class function
# function returning function (closure) practice
# square
# cube

def to_power(x):
    def to_calc(n):
        return n**x
    return to_calc

#& Square
square = to_power(2)
print(square(4))

#& Cube
cube = to_power(3)
print(cube(2)) 
