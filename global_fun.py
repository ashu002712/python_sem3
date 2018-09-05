new_val=10
def square(value):
    """returns the square of a number"""
    global new_val
    new_val=new_val**value
    return new_val
print(square(5))
print(new_val)
 
