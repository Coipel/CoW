
# android-filename-checker

# What it does?

Scans all files in all subdirectories under the specified directory to generate an report on which files are not consistent of "a-z", "A-Z", "0-9", "_-." or spaces.

# Why the program?

When transfering files to android devices via wire, certain symbols such as ":" in filenames will cause the transfer to hang indefinately. By scanning all filenames, the user can be informed of the potential need to correct filenames and where it is located. There are many characters, such as other language symbols, that can be used in filenames without issue, but mainly "a-z", "A-Z", "0-9", "_-." or spaces is practical for my use case.

