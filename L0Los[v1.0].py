# todo:
# get commands sorted, get better store for arrays to save lines

# ---------------------
# ARRAYS
# ---------------------
ipconf = ["ipconfig"]
filehuntphrase = ["filelist"]
exitphrases = ["exit"]
helpphrases = ["help"]
testfuncphrase = ["test"]

# -------------
# IMPORTS
# -------------
from ctypes.util import test
import socket, time, os, glob

# -------------
# TEST FUNCTION
# -------------

# FILENAME    Finds a specific file and prints its path

def testFunct():
    print("FILENAME command, work on it")
    commandFunction()

# -------------


def helpFunction():
    print("""
    EXIT    Stops OS
    FILELIST    Finds and prints the path of all files under a specific extension.
    IPCONFIG    Prints IP information
    TEST    [ADMIN PRIV. REQUIRED] Runs the Test Function
    """)
    commandFunction()

def fileHunt():
    ext = input("Enter file extension (e.g. slnx): ").lower().strip()
    
    print("Please wait, may take a minute.")
    
    rootDir = "C:\\"
    
    found = False


    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if file.lower().endswith(f".{ext}"):
                fullPath = os.path.join(root, file)
                print(f"{fullPath}\n")
                found = True
    
    print("Search complete!")

    if not found:
        print("No files found.")

    commandFunction()

def commandFunction():
    print("Please type your command below:")
    command = input("").lower()
    if command in ipconf:
        ipFind()
    elif command in exitphrases:
        exitTool()
    elif command in filehuntphrase:
        fileHunt()
    elif command in helpphrases:
        helpFunction()
    elif command in testfuncphrase:
        if admin == True:
            testFunct()
        else:
            print("RESTRICTED ACCESS - ADMIN PRIV. REQUIRED.")
            commandFunction()
    
    else:
        print("Unknown Command, for a list of commands, use 'HELP'")
        commandFunction()


def exitTool():
    print("Are you sure you want to exit? [Y/N]")
    decideExit = input("")
    if decideExit.lower() == "y":
        exit()
    elif decideExit.lower() == "n":
        print("EXIT ABORTED")
        commandFunction()
    else:
        print("Unnatural input")
        exitTool()

def ipFind():
    hostName = socket.gethostname()
    IPgrab = socket.gethostbyname(hostName)
    
    print(f"Your IP is {IPgrab}\nYour Computer Name is {hostName}\n")

    ipconfig = os.system('ipconfig')
    print("FULL IPCONFIG PAGE OF OS:\n")
    print(ipconfig)

    commandFunction()


    
def nameAdminChecker():    
    print("NAME SELECT")
    
    
    securityKey = "1337"
    admin = False
    adNames = ["OUROBOROS", "Abel+Cain"]
    print("Please input your LWos Username:")
    name = input("")

    if name == "":
        name = "User"
        print("No name selected, name is 'User'")

    if name in adNames:
        print("ADMIN USERNAME DETECTED: ENTER SECURITY KEY")
        keySel = input("")
        if keySel == securityKey:
            print(f"Welcome back {name}")
            admin = True
            return admin
        else:
            print("INCORRECT SECURITY KEY: LOCKED")
            return admin
    
    print(f"Welcome back {name}")


def main():
    print("""
      _     ___  _              
     | |   / _ \| |    ___  ___ 
     | |  | | | | |   / _ \/ __|
     | |__| |_| | |__| (_) \__ |
     |_____\___/|_____\___/|___/
     Welcome to L0Los Operating System [V1.0]
     Please input your command
    """)

    commandFunction()

    

admin = nameAdminChecker()

main()
