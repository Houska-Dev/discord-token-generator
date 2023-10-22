import random

chars = "qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM-_0147258369"

for i in range(5000) :
    first = ''.join((random.choice(chars) for i in range(24)))
    second = ''.join((random.choice(chars) for i in range(6)))
    third = ''.join((random.choice(chars) for i in range(27)))

    result = first + "." + second + "." + third

    output = open("tokens.txt", "a")
    output.write(result + "\n")
