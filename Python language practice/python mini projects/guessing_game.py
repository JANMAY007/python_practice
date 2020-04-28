sec_num = int(input("enter a secret number: "))
guess_cnt = 0
guess_limit = 3
while(guess_cnt < guess_limit):
    guess = int(input("guess a nunber: "))
    guess_cnt+=1
    if guess == sec_num:
        print("you won this game!")
        break
    else:
        print("Try next time!")