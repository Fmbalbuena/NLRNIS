# read file of first agrument
import sys, os
try:
 data = open(sys.argv[1]).read()
except:
 print("ERR")
 exit()
dct = {"@": data, "E": "0"}
iteration = 0
RESET = False
define = False
printf = False
replace = False
inp = False
join = False
Revert = False
getascii = False
getfirstchar = False
removeallexceptcertainchar = False
readfile = False
comment = False
multilinecomment = False
takeagrument = False
definebutvar = False
getfilesandfolders = False
################################################################################
variable = ""
variable2 = ""
variable3 = ""
variable4 = ""
variable5 = ""
variable6 = ""
string = ""
escape = False
isready = False
isset = False
isgo = False
def erroring(errtype, errreason, tb):
    print(end=errreason, file=sys.stderr)
sys.excepthook = erroring
def dctremoveallexceptcertain(string, variable):
    # removes all except certain characters
    # string = string to be modified
    # variable = characters to be kept
    # returns modified string
    global newstring
    newstring = ""
    for i in string:
        if i in variable:
            newstring += i
    return newstring
while True:
    # Note you should use try and except to catch errors, not if x in y:
    for i in data:
        if printf:
            # print the variable of dct variable
            if i in dct:
                print(dct[i], end = "")
                printf = False
            else:
                raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                break
        elif define:
            if isready:
                if escape:
                    # check if i is quote or backslash add to string else add backslash and i
                    if i == "\"" or i == "\\":
                        string += i
                        escape = False
                    else:
                        string += "\\" + i
                        escape = False
                elif i == "\"":
                    dct[variable] = string
                    string = ""
                    isready = False
                    define = False
                    # check if the variable is "@" change the data
                    if variable == "@":
                        RESET = True
                        break
                elif i == "\\":
                    escape = True
                    continue
                else:
                    string += i
            else:
                variable = i
                isready = True
        elif replace:
            # get 3 variables
            if isgo:
                try:
                  dct[variable] = dct[variable2].replace(variable3, i)
                except:
                  raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                  break
                replace = isset = isready = isgo = False
                # check if the variable is "@" change the data
                if variable == "@":
                    RESET = True
                    break
            elif isset:
                variable3 = i
                isgo = True
            elif isready:
                variable2 = i
                isset = True
            else:
                variable = i
                isready = True
        elif inp:
            try:
                dct[i] = input()
                dct["E"] = "0"
            except EOFError:
                dct["E"] = "1"
            inp = False
            if i == "@":
                RESET = True
                break
        elif join:
            if isset:
                try:
                    dct[variable] = dct[variable2] + dct[i]
                except:
                    raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                    break
                join = isset = isready = isgo = False
                # check if the variable is "@" change the data
                if variable == "@":
                    RESET = True
                    break
            elif isready:
                variable2 = i
                isset = True
            else:
                variable = i
                isready = True
        elif Revert:
            # this is equivalent to pseudocode var = var2.reverse()
            if isready:
                try:
                    dct[variable] = dct[i][::-1]
                except:
                    raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                    break
                isready = False
                Revert = False
                if variable == "@":
                    RESET = True
                    break
            else:
                variable = i
                isready = True
        elif getfirstchar:
            # gets the first character of the variable
            if isready:
                try:
                    dct[variable] = dct[i][0]
                except:
                    raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                isready = False
                getfirstchar = False
                if variable == "@":
                    RESET = True
                    break
            else:
                variable = i
                isready = True
        elif getascii:
            # gets ascii value of the variable
            if isready:
                try:
                    dct[variable]
                    dct[i]
                    try:
                     dct[variable] = ord(dct[i])
                    except:
                     raise Exception("ERROR IN FILE", sys.argv[1], "INVALID NUMBER IN ITERATION", iteration)
                except:
                    raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                getascii = False
                isready = False
                if variable == "@":
                    RESET = True
                    break
            else:
                variable = i
                isready = True
        elif removeallexceptcertainchar:
            # removes all except certain character
            if isready:
                try:
                    dct[variable] = dctremoveallexceptcertain(dct[variable], dct[i])
                except:
                    raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                isready = False
                removeallexceptcertainchar = False
                if variable == "@":
                    RESET = True
                    break
            else:
                variable = i
                isready = True
        elif readfile:
            if isready:
                try:
                    dct[i]
                except:
                    raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                try:
                    dct[variable] = open(dct[i], "r").read()
                    dct["E"] = "0"
                except:
                    dct["E"] = "1"
                isready = False
                readfile = False
                if variable == "@":
                    RESET = True
                    break
            else:
                variable = i
                isready = True
        elif comment:
            # ignore until a newline is found
            if i == "\n":
                comment = False
        elif multilinecomment:
            if i == "}":
                multilinecomment = False
        elif takeagrument:
            # checks if the variable is defined and the variable is a number
            if isready:
                try:
                    dct[i]
                    try:
                        int(dct[i])
                        try:
                         dct[variable] = int(dct[i]) + 2
                         dct["E"] = "0"
                        except:
                         dct["E"] = "1"
                    except:
                        raise Exception("ERROR IN FILE", sys.argv[1], "INVALID NUMBER", iteration)
                except:
                    raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                isready = False
                takeagrument = False
                if variable == "@":
                    RESET = True
            else:
                variable = i
                isready = True
        elif definebutvar:
             # like > but it defines the variable
            if isready:
                try:
                    dct[variable] = dct[i]
                except:
                    raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                isready = False
                definebutvar = False
                if variable == "@":
                    RESET = True
                    break
            else:
                variable = i
                isready = True
        elif getfilesandfolders:
            # gets all files and folders in a variable if folder not found the variable "E" is equal to "1" else "0"
            if isready:
                # check if variable is defined
                try:
                    dct[i]
                except:
                    raise Exception("ERROR IN FILE", sys.argv[1], "VARIABLE NOT FOUND IN ITERATION", iteration)
                try:
                 files = os.listdir(dct[i])
                 dct[variable] = files
                 dct["E"] = "0"
                except:
                    dct["E"] = "1"
                isready = False
                getfilesandfolders = False
                if variable == "@":
                    RESET = True
                    break
            else:
                variable = i
                isready = True
        elif i == "@": #############################################################################################################
            RESET = True
            break
        elif i == "H":
            break
        elif i == ">":
            define = True
        elif i == "*":
            printf = True
        elif i == "$":
            replace = True
        elif i == "&":
            inp = True
        elif i == "+":
            join = True
        elif i == "/":
            revert = True
        elif i == "?":
            getfirstchar = True
        elif i == ".":
            getascii = True
        elif i == "!":
            removeallexceptcertainchar = True
        elif i == ";":
            readfile = True
        elif i == ":":
            comment = True
        elif i == "{":
            multilinecomment = True
        elif i == "|":
            takeagrument = True
        elif i == "=":
            definebutvar = True
        elif i == "%":
            getfilesandfolders = True
        # its not necessary to raise error invalid command
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        iteration += 1
    # check if string still contains something put it in dct
    if string != "":
        dct[variable] = string
        string = ""
        define = False
        isready = False
        isset = False
        isgo = False
        printf = False
        replace = False
        inp = False
        join, revert = False, False
        getfirstchar = False
        getascii = False
        removeallexceptcertainchar = False
        readfile = False
        comment = False
        multilinecomment = False
        takeagrument = False
        definebutvar = False
        getfilesandfolders = False
        # check if dct is "@" change the data
        if variable == "@":
            RESET = True
    if RESET:
        RESET = False
        data = dct["@"]
        iteration = 0
        continue
    break
try:
    print(dct["#"], end = "")
except:
    pass
