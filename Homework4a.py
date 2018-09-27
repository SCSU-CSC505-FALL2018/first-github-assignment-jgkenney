from random import randint


select = (input("Please type an mathematical operator:\n"
                "x  -  +  /\n"))

r1 = randint(0, 10)
r2 = randint(0, 10)
z = r1*r2


if select == "x":
    answer=1
    user_answer=0
    while answer != user_answer:
        print("Multiplication. Please complete this example:")
        #print(r1, "x", r2)  # easier way is to use the modulus
        print("% s x % d" % (r1, r2))
        answer = int(r1*r2)
        user_answer = int(input("What do you think the answer is? "))
        if answer == user_answer:
            print("Very good!")
        else:
            print("Try again!")

if select == "-":
    answer = 1
    user_answer = 0
    while answer != user_answer:
        print("Subtraction. Please complete this example:")
        print("% s - % d" % (r1, r2))
        answer = int(r1-r2)
        user_answer = int(input("What do you think the answer is? "))
        if answer == user_answer:
            print("Very good!")
        else:
            print("Try again!")

if select == "+":
    answer = 1
    user_answer = 0
    while answer != user_answer:
        print("Addition. Please complete this example:")
        print("% s + % d" % (r1, r2))
        answer = int(r1+r2)
        user_answer = int(input("What do you think the answer is? "))
        if answer == user_answer:
            print("Very good!")
        else:
            print("Try again!")

if select == "/":
    answer = 1
    user_answer = 0
    while answer != user_answer:
        print("Division. Please complete this example:")
        print("% s / % d" % (z, r1))
        answer = int(z/r1)
        user_answer = int(input("What do you think the answer is? "))
        if answer == user_answer:
            print("Very good!")
        else:
            print("Try again!")
