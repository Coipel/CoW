import os
import argparse
import re


def find_invalid_characters(filename) -> list[str]:
    return re.findall("[^\\w\\d\\s\\-.,]",filename)


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
                                    description="Will generate report of filenames not consistent of 'a-z','A-Z','0-9','_-.'",
                                    epilog="Non-english characters and valid special characters not supported (false-positives)")

    parser.add_argument("target_directory")
    args = parser.parse_args()
    print("======== Invalid Filenames Search ========\n")
    path_walker(args.target_directory)
    print("======== Invalid Filenames Search Complete ========")

if __name__ == "__main__":
    main()




