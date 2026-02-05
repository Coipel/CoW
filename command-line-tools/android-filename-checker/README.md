
# android-filename-checker

# What it does?

Scans all files in all subdirectories under the specified directory to generate an report on which filenames will hang an Android wired file transfer.

# Why the program?

When transfering files to android devices via wire, certain symbols such as ":" in filenames will cause the transfer to hang indefinately. By scanning all filenames, the user can be informed of the potential need to correct filenames and where it is located.

# Usage

python3 -m main <target_directory>

# Example

## Command

python3 -m main ./dummy_directory_tree

### Tip

Use bash output redirection to flow output into a text file if working with a large amount of files with invalid characters where the entire output can't be held in a terminal.

python3 -m main ./dummy_directory_tree > log.txt

## Output

======== Invalid Filenames Search ========

./dummy_directory_tree/directory_3/invalid\*filename.txt\
Invalid Characters: ['*'] 

./dummy_directory_tree/directory_4/invalid\filename.txt\
Invalid Characters: ['\\\\'] 

./dummy_directory_tree/directory_1/invalid:filename.txt\
Invalid Characters: [':'] 

======== Invalid Filenames Search Complete ========

# Post Scan

Note, the following was done using default Ubuntu "Files" (Nautilus)

Utilize computer file explorer filename search on the root of the directories (target_directory) locate and group files invalid characters in one place; ctrl-A all offending filenames; select name change while group selecting to mass rename files to replace invalid character with a valid one. Repeat procedure for all offending files. Rerun scan as needed to see what remains until all filenames are valid. Start with the most common invalid symbol so rescan reports become easier to read.

Recommendation: replace ":" with "," and "?" with "\_" (underscore).


