libName = "SearchLib"

def libImport():

    status = "{0} is loaded\n".format(libName)

    return print(status)

def searchInfo():
    print("""
    search module enabled

    By Date...............D
    By Name...............N
    By project............P
    By Rep................R
    """)

def searchStart():
    sParam = input("parameter of search or exit to quit :  ")
    paramCheck(sParam)

def paramCheck(sParam):
        if sParam == "D":
            print("search by date")
        elif sParam == "N":
            print("search by Name")
        elif sParam == "P":
            print("search by project")
        elif sParam == "R":
            print("search by Rep")
        elif sParam == "exit":
            print("Exited")
