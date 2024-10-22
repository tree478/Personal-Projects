#A kwarg is the same thing as an arg, but where an ar returns a tuple, a kwarg makes a dictionary

def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print("Your age is", kwargs.get("age"))

person(name="Soumya", age="16", grade=10, smart=True)#The function took all of this and packaged it into a dictionary


def order_pizza(name, address, **toppings):
    print(f"Order is for {name}")
    print(f"Ship it to {address}")
    price = 18.00
    for key, value in toppings.items():
        price += 2.00
    print(f"The price is {price}")
    return price

order_pizza("Soumya", "5 Westport Dr", cheese=True, peppers=True, pineapples=True, mushrooms=False)
