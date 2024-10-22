#*args means unlimited arguments. You can put in as many arguments as you want, and it will work. It desn't have to be 'args'
#It just has to have the single astrisk before it. 

def add_numbers(*args):
    total = 0
    for num in args:
        total *= num
    return total

total = add_numbers(1, 2, 3, 4, 5)
print(total)