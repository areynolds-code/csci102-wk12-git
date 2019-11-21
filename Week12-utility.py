#Austin Reynolds
# CSCI 102 – Section C
#Week 12

def PrintOutput(thing):
    print ("OUTPUT", thing)

def LoadFile (name):
    fi = open(name, "r")
    lines = []
    for i in fi:
        lines.append(i)
    return i

def UpdateString(string, rep, i):
    PrintOutput(string[0 : i] + rep + string[i + 1 : (len(string) - 1)])
