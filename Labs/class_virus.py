import os # We need to mess with files/folders and navigate, so we use this
import time # We want to wait between virus propagation attempts.
import string # For our random words.
import random # We want a random generator for the virus, so we get that here

N_FILES = 30
VIRUS_RATE = 0.2

VIRUS_TIME = 60

# If set, this uses a specific number of viruses instead of probability
N_VIRUS = 8
virus_count = 0 # Holds a count for virus generation
MAX_VIRUS = 50 # Don't let this code run away from us ><
failed_flag = False

# Virus is generated in a sub folder, so make that folder (only if it doesn't
# already exist.
if not os.path.exists("my_cool_stuff"):
    os.mkdir("my_cool_stuff")
os.chdir("my_cool_stuff")

folders = ["videos", "pictures", "magic",
           "documents", "documents/taxes", "documents/emails", "documents/secrets"]


def randomword(length):
    """
    A random word function from stack overflow (I was lazy).  It works by grabbing
    N random characters, where N is the given length, and joining them together into
    a string (pretty elegant).  Note, a MUCH better way is to use lorem lipsum, but
    this requires each student to install that python package for the code to run.

    **References**

        * http://stackoverflow.com/a/37675443
    """
    return ''.join(random.choice(string.lowercase) for i in range(length))


def get_random_file_contents(with_virus=False):
    """
    A function to generate a random file content, with the random occurance of having
    a VIRUS in the text.

    **Parameters**

        with_virus: *bool, optional*
            Whether to force the file to have a virus, or leave it up to chance.

    **Returns**

        contents: *str*
            A random text file content in string format.
    """
    # Grab the global variable
    global virus_count

    # Get the number of lines
    N_lines = random.randint(30, 250)

    # Determine if this will be a virus
    if N_VIRUS is None:
        put_virus = random.random() < VIRUS_RATE
    else:
        put_virus = virus_count < N_VIRUS
    if with_virus:
        put_virus = True
    if put_virus:
        virus_count += 1

    # If it is a virus, where does it go
    if put_virus:
        at_head = random.random() < 0.5
        virus_line = random.randint(0, 9)
        if not at_head:
            virus_line = N_lines - virus_line

    # Start generating the random contents line by line
    contents = []
    for i in range(N_lines):
        line = []
        add_virus = False
        N_words = random.randint(8, 15)

        # If we're adding the virus, at which word will it be
        if put_virus and i == virus_line:
            add_virus = True
            virus_pos = random.randint(0, N_words)

        # Add a word to the line
        for j in range(N_words):
            if add_virus and virus_pos == j:
                line.append("VIRUS")
            else:
                line.append(randomword(random.randint(4, 12)))

        # Store the final line
        line = ' '.join(line)
        contents.append(line)

    # Return the final contents
    return '\n'.join(contents)


def start_virus():
    """
    This is a function that will generate the initial folder for our virus, as well
    as all sub folders and files.
    """

    # Get current working directory (this folder)
    cwd = os.getcwd()
    
    
    # Now, let's generate our random file system.  My cool stuff will have folders
    # and files, named 
    
    # First we generate the folders
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)

    # Then we generate the files randomly.  We start off the N_FILES
    for i in range(N_FILES):
        # Choose a random folder
        folder = folders[random.randint(0, len(folders) - 1)]
        # Get a random name
        fname = "cool_" + randomword(random.randint(4, 8))
        # Get contents to give file
        contents = get_random_file_contents()
        # Generate file
        fptr = open("%s/%s" % (folder, fname), 'w')
        fptr.write(contents)
        fptr.close()


def can_propagate():
    """
    A function that checks if a virus can be propagated.  If so, a new file is generated here.

    **Returns**

        can_propagate: *bool*
            A boolean saying if virus propagation is valid.
    """

    # Grab our global
    global virus_count
    global failed_flag

    # First we go through every folder to make sure it is possible to propagate the virus.
    possible = []
    total_virus_flag = False
    for folder in folders:
        safe_flag = False
        virus_flag = False

        fptrs = [fptr for fptr in os.listdir(folder) if os.path.isfile("%s/%s" % (folder, fptr))]

        # Check if safe file exists
        safe_flag = "SAFE" in fptrs

        # Check if a virus is in the folder
        for fptr in fptrs:
            raw = open("%s/%s" % (folder, fptr), 'r').read()
            if "VIRUS" in raw:
                virus_flag = True
                break

        # If safe_flag and not virus_flag, then no propagation. Else, yes
        if safe_flag and not virus_flag:
            continue
        else:
            possible.append(folder)

        if virus_flag:
            total_virus_flag = True

    # In the case of total_virus_flag = False, we have removed all viruses!
    if not total_virus_flag:
        return False

    # In the case that too many have been made, kill the code.
    if virus_count > MAX_VIRUS:
        failed_flag = True
        return False

    if len(possible) > 0:
        # Randomly grab a folder to propagate to
        folder = random.choice(possible)
        # Get a random name
        fname = "cool_" + randomword(random.randint(4, 8))
        # Get contents to give file
        contents = get_random_file_contents(with_virus=True)
        # Generate file
        fptr = open("%s/%s" % (folder, fname), 'w')
        fptr.write(contents)
        fptr.close()
        return True
    else:
        return False


def virus_monitor():
    """
    This function will propagate the virus every VIRUS_TIME seconds. Virus propagation rules are as
    follows:
        1. A virus can propogate to a folder that both (a) does not have a SAFE file or (b)
           has a virus.
        2. A virus can NOT propagate to a folder that has (a) a file named SAFE and (b) no
           viruses within the folder
        3. Only one virus file will generate every N seconds (where N is the VIRUS_TIME)
        4. If a virus cannot propagate when N is reached, then the virus_monitor function ends.
    """

    while can_propagate():
        time.sleep(VIRUS_TIME)


def print_stats():
    fptr = open("GAME_OVER", 'w')
    if failed_flag:
        fptr.write("Unfortunately, the virus has overrun your system! Better luck next time.\n")
        fptr.write("(HINT) - Try using the grep command to more readily hunt down viruses.\n")
        fptr.write("(HINT) - Try using the touch command to more easily make SAFE files.\n")
    else:
        fptr.write("Congratulations! You have cleaned up your system.\n")
        fptr.write("    Did you use grep to make life easier on yourself?\n")
        fptr.write("    Did you use touch or vim when making the SAFE files?")
    fptr.close()

start_virus()
virus_monitor()
print_stats()