
# android-filename-checker

# What it does?

Scans all files in all subdirectories under the specified directory to generate an report on which files are not consistent of "a-z", "A-Z", "0-9", "_-." or spaces.

# Why the program?

When transfering files to android devices via wire, certain symbols such as ":" in filenames will cause the transfer to hang indefinately. By scanning all filenames, the user can be informed of the potential need to correct filenames and where it is located. There are many characters, such as other language symbols, that can be used in filenames without issue, but mainly "a-z", "A-Z", "0-9", "_-." or spaces is practical for my use case.

# Usage

python3 -m main <target_directory>

# Example

## Command

python3 -m main ./dummy_directory_tree

## Output

======== Invalid Filenames Search ========

./dummy_directory_tree/directory_3/invalid\*filename.txt
Invalid Characters: ['*'] 

./dummy_directory_tree/directory_3/subdirectory/invalid&filename.txt
Invalid Characters: ['&'] 

./dummy_directory_tree/directory_4/invalid\filename.txt
Invalid Characters: ['\\\\'] 

./dummy_directory_tree/directory_2/invalid^filename.txt
Invalid Characters: ['^'] 

./dummy_directory_tree/directory_2/invalid\$filename.txt
Invalid Characters: ['$'] 

./dummy_directory_tree/directory_1/invalid:filename.txt
Invalid Characters: [':'] 

======== Invalid Filenames Search Complete ========


