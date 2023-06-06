#this converts the files in a directory from the format: The <artist> - <track>.<ext> to <artist>, The - <track>.<ext>
#example: The Beatles - Hey Jude.mp3 --> Beatles, The - Hey Jude.mp3
#it isn't perfect, but it works for my purposes
#I used chatgpt for the regex, because I'm lazy.
#should work on windows and linux, i tested it on windows
#i made the directory hardcoded to make sure you know what you're doing, failure could result in corrupted file names on files you didn't want to rename
#
#test first with --test, then run with --run
#
#technobug 2023, no licence, do whatever you want with it, i don't care
#
#

import os #for file handling
import re #for regex
import sys #for command line arguments

# Directory containing the files
directory = "d:\\PortableApps\\Files\\Music\\outfiles"

# Regex pattern to match files beginning with "the "
pattern = r"^(the )(.+?) - (.+)$"

def rename_file(runtype):

    #check directory exists
    if not os.path.isdir(directory):
        print("\n\nThe specified directory does not exist.")
        print("directory: "+directory+"\n\n")
        info()
        sys.exit(1)

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Check if the filename matches the pattern
        match = re.match(pattern, filename, re.IGNORECASE)
        if match:
            # Extract the artist name and track title
            artist = match.group(2)
            track = match.group(3)
            
            # Move "the" to the end of the artist name
            new_artist = f"{artist.capitalize()}, The"
            
            # Create the new filename
            new_filename = f"{new_artist} - {track.capitalize()}"
            
            # Print the new filename
            if runtype == "test":
                print("simulated: "+filename+" --> "+new_filename)
            if runtype == "run":
                print("attempting: "+filename+" --> "+new_filename)
                # Rename the file
                try:
                    os.rename(
                        os.path.join(directory, filename),
                        os.path.join(directory, new_filename)
                    )
                except OSError as e:
                    print(f"An error occurred while renaming the file: {e}")


def info():
    print("This script renames files in a directory.")
    print("Usage: python renamer.py --run")
    print("to see what it would do use: python renamer.py --test\n\n")
    print("YOU MUST CHECK THE DIRECTORY VARIABLE IN THE SCRIPT BEFORE RUNNING IT!\n")
    print("currently: "+directory+"\n")
    print("The script will rename all files in the directory that match the pattern:")
    print(" the <artist> - <track>.<ext> --> <artist>, The - <track>.<ext>\n")
    print("failure to understand this isn't my problem.")


# Check if the script is called with exactly one command line parameter
if (len(sys.argv) == 2):
    match(sys.argv[1]):
        case "--run": rename_file("run")
        case "--test": rename_file("test")
        case _:
            info()
            sys.exit(1)
else:
    info()
    sys.exit(1)

print("Script has finished normally.")