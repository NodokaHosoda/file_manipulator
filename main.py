import sys
import os

def reverse(contents, fileoutput):
    with open(fileoutput, 'w') as f:
        reversed_contents = contents[::-1]
        f.write(reversed_contents)
    print('Reversed file is succesfully created as ' + fileoutput)

def copy(contents, fileoutput):
    with open(fileoutput, 'w') as f:
        f.write(contents)
    print('Copy file is succesfully created as ' + fileoutput)

def duplicate_contents(contents, fileinput, n):
    with open(fileinput, 'a') as f:
        for i in range(int(n)):
            f.write(contents)
    print(fileinput + 'contents are succesfully depulicated ' + n + ' times')

def replace_string(contents, fileinput, needle, newstring):
    with open(fileinput, 'w') as f: 
        replaced_contents = contents.replace(needle, newstring)
        f.write(replaced_contents)
    print(needle + ' are succesfully replaced by ' + newstring)


function = sys.argv[1]
fileinput = sys.argv[2]

if not(os.path.exists(fileinput)):
    print('Input file path does not exit. Type correct file path')
    sys.exit()

with open(fileinput) as f:
    contents = f.read()

if function == 'replace_string':
    if(len(sys.argv) != 5):
        print('Incorrect number of argument. Plase type function, fileinput needle and newstring')
        sys.exit()
    replace_string(contents, fileinput, sys.argv[3], sys.argv[4])

elif function == 'reverse':
    if(len(sys.argv) != 4):
        print('Incorrect number of argument. Plase type function, fileinput and fileoutput')
        sys.exit()
    reverse(contents, sys.argv[3])

elif function == 'copy':
    if(len(sys.argv) != 4):
        print('Incorrect number of argument. Plase type function, fileinput and fileoutput')
        sys.exit()
    copy(contents, sys.argv[3])

elif function == 'duplicate_contents':
    if(len(sys.argv) != 4):
        print('Incorrect number of argument. Plase type function, fileinput and duplicate number')
        sys.exit()
    duplicate_contents(contents, fileinput, sys.argv[3])

else:
    print(function + ' is not a available function. Try again!')
    sys.exit()
