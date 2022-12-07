import random


def main():
    max_number = 100
    rnd_number = random.randint(1, max_number)
    print(rnd_number)
    number_of_attempts = 5
    attempt = 0

    starting_screen(number_of_attempts, max_number)

    while attempt < number_of_attempts:
        if number_of_attempts == attempt:
            print()
            print("You loose! You're out of attempts.")
            break

        guess = input("What is your guess? ")
        try:
            guess = int(guess)
        except ValueError:
            print("That is not a number!!!")
            print()
            continue

        if guess not in range(1, max_number):
            print(f"That is not a valid guess. Type a number from 1 to {max_number}...")
            print()
            continue
        else:
            attempt += 1
            if rnd_number == guess and attempt == 1:
                print(f"Congratulations! It was {rnd_number}! It took you 1 attempt!")
                print('')
                break
            elif rnd_number == guess and attempt > 1:
                print(f"Congratulations! It was {rnd_number}! It took you {attempt} attempts!")
                print('')
                break
            elif rnd_number < guess:
                print("Sorry, that's too HIGH...")
            else:
                print("Sorry, that's too LOW...")

        print(f'Attempts remaining: {number_of_attempts - attempt}')
        print('')

    print("Thank you for playing!")


def starting_screen(number_of_attempts, max_number):
    """ Generate an introduction.

    Args:
        number_of_attempts: A number of tries to guess the number.
        max_number: Maximum value of randomized number.

    Returns:
        A print statement: starting screen, introduction & rules.
    """

    print("-----------------------------------------")
    print("     Welcome to the Guessing Game!")
    print("-----------------------------------------")

    print(f"You have {number_of_attempts} tries to guess a randomly generated number, "
          f"within the range of 0 and {max_number}!")
    print()


if __name__ == '__main__':
    main()
