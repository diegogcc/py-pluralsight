from random import randrange

def main_no_exceptions():
    number = randrange(100)
    while True:
        guess = int(input("? "))
        if guess == number:
            print("You win!")
            break

def main_all_exeptions():
    '''
    Not specifying the exception type causes this program to 
    omite even a KeyboardInterrupt.

    Catching all exceptions is a very bad idea.
    '''
    number = randrange(100)
    while True:
        try:
            guess = int(input("? "))
        except:
            continue
        if guess == number:
            print("You win!")
            break

def main():
    '''

    '''
    number = randrange(100)
    while True:
        try:
            guess = int(input("? "))
        except ValueError:
            continue 
        if guess == number:
            print("You win!")
            break

if __name__ == "__main__":
    main()