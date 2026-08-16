'''
============================================================
FILE HANDLING IN PYTHON - COMPLETE NOTES
============================================================ '''

# WHAT IS FILE HANDLING?
# File handling in Python is the process of creating, opening,
# reading, writing, appending, and closing files to store data
# permanently.

# WHY FILE HANDLING IS USED?
# 1. Data is stored permanently
# 2. Data is not lost after program ends
# 3. Used to handle large amount of data
# 4. Useful in real-life applications (reports, logs, databases)

# TYPES OF FILES IN PYTHON
# 1. Text Files:
#    - Stores data in readable form
#    - Examples: .txt, .csv, .py
#
# 2. Binary Files:
#    - Stores data in binary (0 and 1) format
#    - Examples: .jpg, .png, .mp3, .pdf

# BASIC STEPS OF FILE HANDLING
# 1. Open the file
# 2. Perform operation (read/write/append)
# 3. Close the file

'''
------------------------------------------------------------
OPENING A FILE
------------------------------------------------------------ '''

# Syntax:
# file_object = open("filename", "mode")

# FILE MODES
# r   -> Read mode (file must exist)
# w   -> Write mode (creates new file, deletes old data)
# a   -> Append mode (adds data at end of file)
# x   -> Create mode (creates file, error if file exists)
# rb  -> Read binary file
# wb  -> Write binary file

'''
------------------------------------------------------------
READING A FILE
------------------------------------------------------------ '''

# read()
# - Reads the complete content of the file

# readline()
# - Reads only one line at a time

# readlines()
# - Reads all lines and returns a list

'''
------------------------------------------------------------
WRITING A FILE
------------------------------------------------------------ '''

# write()
# - Writes data into file
# - Old data will be erased if file is opened in 'w' mode

''' ------------------------------------------------------------
    APPENDING A FILE
    ------------------------------------------------------------ '''

# Append mode ('a') adds new data at the end of the file
# Existing data remains safe

''' ------------------------------------------------------------
    CLOSING A FILE
    ------------------------------------------------------------ '''

# close()
# - Saves the file
# - Frees system memory
# - Prevents data loss
# - Always close file after use

''' ------------------------------------------------------------
    WITH STATEMENT (BEST PRACTICE)
    ------------------------------------------------------------ '''

# Using 'with' statement:
# - No need to close file manually
# - File closes automatically
# - Safer and cleaner way

''' ------------------------------------------------------------
    FILE HANDLING ERRORS
    ------------------------------------------------------------ '''

# Common Errors:
# 1. FileNotFoundError
# 2. PermissionError
# 3. IOError

# These errors occur when:
# - File does not exist
# - Wrong mode is used
# - Permission is denied

''' ------------------------------------------------------------
    EXCEPTION HANDLING IN FILE HANDLING
    ------------------------------------------------------------ '''

# try-except-finally is used to handle file errors safely
# finally block always executes and is used to close file

''' ------------------------------------------------------------
    CHECKING FILE EXISTENCE
    ------------------------------------------------------------ '''

# os module is used to check whether a file exists or not

''' ------------------------------------------------------------
    IMPORTANT EXAM POINTS
    ------------------------------------------------------------ '''

# - File handling provides permanent storage
# - Always close a file after use
# - 'w' mode deletes old data
# - 'a' mode adds data safely
# - 'with' statement is recommended
# - Text files are human-readable
# - Binary files are machine-readable

