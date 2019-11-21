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

def FindWordCount(lis, string):
    for i in lis:
       j = 0
       k = len(string) - 1
       num = 0
       while k < len(i):
           if i [j : k] == string:
               num += 1 
           j += 1
           k += 1
       PrintOutput(num)

