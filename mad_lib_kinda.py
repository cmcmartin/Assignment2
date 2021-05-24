"""
Assignment 3.
"""
import sys
from datetime import datetime


def main():
    """
    Enter your code below. Ensure your code is within the body of the main() function.
    i.e. it is tabbed-in at least once.
    """
    # This comment is within the body of the main() function.
    name = input("Please enter your name: ")
    sex = input("Enter your sex (M = Male, F = Female, N = Non-binary): ").upper()
    if sex == "M":
        long_sex = "male"
        pronoun = "He was"
        pronoun2 = "his"
    elif sex == "F":
        long_sex = "female"
        pronoun = "She was"
        pronoun2 = "her"
    elif sex == "N":
        long_sex = "non-binary"
        pronoun = "They were"
        pronoun2 = "their"
    else:
        print("Error: You must choose your sex by typing M, F, or N")
        sys.exit()
    try:
        dob = datetime.strptime(input("Enter date of birth, YYYY-MM-DD: "), "%Y-%m-%d")
    except ValueError:
        print("Error: Must use YYYY-MM-DD format (e.g. 2002-03-16)")
        sys.exit()
    birth_place = input("Enter city of birth: ")
    try:
        sin = int(input("Enter your SIN number: "))
    except ValueError:
        print("Error: SIN must be numeric only")
        sys.exit()

    age = int((datetime.today() - dob).days / 365.25)

    print(
        f"{name} is a {age} year old {long_sex}. {pronoun}"
        f" born in {birth_place} and {pronoun2} SIN # is {sin}"
    )

    # Creativity Points (I stole this sword art, online...in a creative way)
    # -----------------------//\\
    # ---------------------// ¤ \\
    # ---------------------\\ ¤ //
    # ----------------------\\//
    # ---------------------(___)
    # ---------------------(___)
    # ---------------------(___)
    # ---------------------(___)_________
    # ------------\_____/\__/----\__/\_____/
    # ------------\ _°_[------------]_ _° /
    # ----------------\_°_¤ ---- ¤_°_/
    # --------------------\ __°__ /
    # ---------------------|\_°_/|
    # ---------------------[|\_/|]
    # ---------------------[|[¤]|]
    # ---------------------[|;¤;|]
    # ---------------------[;;¤;;]
    # --------------------;;;;¤]|]\
    # -------------------;;;;;¤]|]-\
    # ------------------;;;;;[¤]|]--\
    # -----------------;;;;;|[¤]|]---\
    # ----------------;;;;;[|[¤]|]|---|
    # ---------------;;;;;[|[¤]|]|---|
    # ----------------;;;;[|[¤]|/---/
    # -----------------;;;[|[¤]/---/
    # ------------------;;[|[¤/---/
    # -------------------;[|[/---/
    # --------------------[|/---/
    # ---------------------/---/
    # --------------------/---/|]
    # -------------------/---/]|];
    # ------------------/---/¤]|];;
    # -----------------|---|[¤]|];;;
    # -----------------|---|[¤]|];;;
    # ------------------\--|[¤]|];;
    # -------------------\-|[¤]|];
    # ---------------------\|[¤]|]
    # ----------------------\\¤//
    # -----------------------\|/
    # ------------------------V


# This comment is NOT within the body of the main() function.

# Do not edit below
if __name__ == "__main__":
    main()
