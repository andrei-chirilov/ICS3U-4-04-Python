#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program does the guessing game with loops

import random


def main():

    rnd_number = random.randint(1, 10)

    while True:
        try:
            number = int(input("Guess a number between 1-10: "))
        except Exception:
            print("Not a valid integer")
            break
        if number == rnd_number:
            print("You got it!")
            break
        else:
            print("You got it wrong.")


if __name__ == "__main__":
    main()
