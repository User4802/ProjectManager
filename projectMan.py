import searchLib

list = []
version = "0.1.A"

def exit():
    print("exited the program")

def infoDisplay():
    print("\nProject Manager v{0}\n".format(version))
    searchLib.libImport()
    input("Press any key to return.....<")
    prompt()

def search():
    searchLib.searchInfo()
    searchLib.searchStart()
    prompt()

def nav(userP):
    if userP == "info":
        infoDisplay()
    elif userP == "search":
        search()
    elif userP == "exit":
        exit()


def prompt():
    mainInput = input("Listening for command.....<")
    nav(mainInput)

prompt()
