#Program that lets us choose number from 1 to n(we specify it) and lets us make a guess and check whether our guess is right or wrong
import random as ran
while True:
  try:
    #Step1: Asking user for input and checking whether the input is positive integer
    while True:
        usr_lvl = int(input("Level: "))
        if usr_lvl > 0:
            break

    #STEP2: Randomly generate a number between 1 and n, by using random module
    guess = ran.randint(1,usr_lvl)
    # print(guess)


    while True:
      try:
      #STEP3: Prompt the user to guess the integer and also check whether guess is positive or not
          usr_guess = int(input("Guess: "))
        #STEP4 b: If gues is larger than the interger, then print("Too large!") and reprompt
          if usr_guess < 0:
             continue
          elif usr_guess > guess:
              print("Too large!")
              continue
        #STEP4 a:If guess is smaller than the integer, then print("Too small!") and reprompt
          elif usr_guess < guess:
              print("Too small!")
              continue
          else:
              print("Just right!")
          break
      except:
         continue
      else:
         break
  except:
      continue

  else:
      break