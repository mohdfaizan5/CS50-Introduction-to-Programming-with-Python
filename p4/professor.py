#Progarm that gives user some addition problems to solve

#STEP3: If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total
    #Note: If the user has still not answered correctly after three tries, the program should output the correct answer.

#STEP4: The program should ultimately output the user’s score, a number out of 10.

import sys, random

def main():
    level = get_level()
    print(f"Score: {generate_integer(level)}")


def get_level():
    #STEP1:Prompts the user for a level, \(n\). If the user does not input 1, 2, or 3, the program should prompt again.
    #get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3

     while True:
        try:
            level = int(input("Level: "))
            if not 0 < level < 4:
                raise ValueError
            return level
        except:
            pass

def generate_integer(level):
    #generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3
    #STEP2: Random generate ten problems with the lvl usr choosed. wherein each of X and Y is a non-negative integer with \(n\) digits
    turns = 11
    score = 10
    while True:
        temp_lives = 3
        if level == 1:
            a = (random.randint(0,9))
            b = (random.randint(0,9))

        elif level == 2:
            a = (random.randint(10,99))
            b = (random.randint(10,99))

        elif level == 3:
            a = (random.randint(100,999))
            b = (random.randint(100,999))

        while True:
            turns -= 1
            if turns == 0:
                # print(score)
                return score
            try:
                user_ans = int(input(f"{a} + {b} = "))

            except EOFError:
                sys.exit()
            except:
                print("EEE")
                temp_lives -= 1
                continue
            else:
                if user_ans == a+b:
                    break
                else:
                    print("EEE")
                temp_lives -= 1

                if temp_lives == 0:
                    score -= 1
                    print(f"{a} + {b} = {a+b}")

    # return score


if __name__ == "__main__":
    main()
