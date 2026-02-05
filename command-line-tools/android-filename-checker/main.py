# Written in Python 3.12.3 virtual environment

import os
import argparse
import re

# Whitelist approach
# Introduced variables to minimize regex for readability/maintainability
letters_and_digits = "\\w" # Includes regular letters of English and other languages as well as digits
whitespaces = "\\s"
special_regex = "\\-\\[\\]"
specials = ".,'&()—;–!=・‘^«»$"

# The ^ symbol in the beginning inverts the logic of everything to the right; aka the whitelist
blacklist = "[^" + letters_and_digits + whitespaces + special_regex + specials + "]"


def find_invalid_characters(filename) -> list[str]:
    return re.findall(blacklist, filename)


def path_walker(target_directory):
    for root, _, files in os.walk(target_directory):
        for file in files:
            path = os.path.join(root,file)

            invalid_characters = find_invalid_characters(file)
            if bool(invalid_characters):
                print(path)
                print("Invalid Characters:", invalid_characters, "\n")
  

def main():
    parser = argparse.ArgumentParser(prog="android-filename-checker",
                                    description="Will generate report of filenames not consistent with Android")

    parser.add_argument("target_directory")
    args = parser.parse_args()
    print("======== Invalid Filenames Search ========\n")
    path_walker(args.target_directory)
    print("======== Invalid Filenames Search Complete ========")

if __name__ == "__main__":
    main()




