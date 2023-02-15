# closures, first class function
# function returning function (closure) practice
# square
# cube

def to_power(x):
    def to_calc(n):
        return n**x
    return to_calc

