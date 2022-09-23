import random

point = 0

while True:
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    true = a + b
    wrong = random.randint(0, 200)
    c = random.choice([true,wrong])

    print(f'{a} + {b} = {c}')
    ans = int(input("1 for True, 0 for False: "))

    if (a + b) == c:
        if ans == 1:
            point += 1
            print("Great!\n")
        else:
            print("\n== GAME OVER ==")
            print(f'Your total point is: {point}')
            break
    else:
        if ans == 0:
            point += 1
            print("Great!\n")
        else:
            print("\n== GAME OVER ==")
            print(f'Your total point is: {point}')
            break