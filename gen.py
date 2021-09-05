import random

chars = "ODc5NDYyMDk2MjMwODE3ODMzYS0kPgLClIkA5-WqafNWVXe4ib7xX07Ks"

for i in range(5000) :
    first = ''.join((random.choice(chars) for i in range(24)))
    second = ''.join((random.choice(chars) for i in range(6)))
    third = ''.join((random.choice(chars) for i in range(27)))

    result = first + "." + second + "." + third

    output = open("tokens.txt", "a")
    output.write(result + "\n")