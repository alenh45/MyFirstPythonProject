print("Hello,Welcome to my first game!")
name = input("What is your name? ")
print('Hi ' + name + ' ,nice to meet you!')
age = int(input('How old are you ? '))

health = 10

if age >= 18:
    print("You are old enough to play")

    wants_to_play = input("Do you want to play? (yes/no) ").lower()
    if wants_to_play == "yes":
        print("OK...Let's start")
        print("You start with ", health, "health")

        first_choise = input("Choose do you want to go left or right? (left/right) ? ").lower()
        if first_choise == "right":
            ans = input("Good...You follow the road and reached the lake do you swim or walk around (swim/walk)? ")
            if ans == "walk":
                print("You walked around the lake and reached the shore")
            elif ans == "swim":
                print("You managed to reach the shore but you were bit by a fish and lost five health ")
                health -= 5

                ans = input("You noticed a house and the river...which do you go to? (house/river) ? ")
                if ans == "house" :
                    print("You go to the house and owner is there.He doesn't like you so you loose five health ")
                    health -=5
                    if health <= 0:
                        print("You now have 0 health and you lost the game...haha")
                    else:
                        print("You survived...you win...boo!")
                else:
                    print("You fell in the river and lost...haha")

        else:
            print("You felt down and lost")

    else:
        print("Stupid...cya")
else:
    print("You are not old enough to play")
