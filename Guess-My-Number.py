import getpass, os

while True:
    print("I'm thinking of a number! Try to guess the number I'm thinking of")
    #my_num = input('My number is: ')
    my_num = getpass.getpass(prompt='My number is: ', stream=None)
    os.system('cls')
    #print('\n'*10)

    print("The game is starting ...")
    #print("Type 'done' if you want to surrender")
    print("..."*20)

    # THE CLUES
    num = float(my_num)
    count = 0
    while(num > 0):
        count += 1
        num = num//10
    print("The clues:\n1) His/her number has/have", count, "digit(s) (before comma for decimal)")
    try:
        int(my_num)
        print("2) His/her number is integer")
    except:
        float(my_num)
        print("2) His/her number is decimal")
    print("..."*20)

    counter = 0
    while True:
        guess_num = input("Guess his/her number: ")

        if guess_num == 'done':
            print("Whaaat?! You can't guess his/her number?!\nOkay then, his/her number is: ", my_num)
            break

        try:
            fguess = float(guess_num)
        except:
            print('Please input number correctly')
            continue

        new_num = float(my_num)
        if fguess < new_num:
            print("That's too low!")
        elif fguess > new_num:
            print("That's too high!")
        else:
            print("Great!\nYou win!!!")
            break

        counter += 1
        if counter % 5 == 0:
            print('Come on!!! Maybe you can ask him/her for help :))\n'
                  'Or you want to surrender? Type "done" if you want to')
        else:
            continue
    status = input("Play again? Y/N: ")
    if status in ["N", "n"]:
        break