import os
import subprocess
import shutil
from termcolor import colored

curdir = os.getcwd()
def ls():
    k = 1
    for files in os.listdir(os.curdir):
        if os.path.isfile(files):
            print (colored(files, "cyan"), end = ' ')
        else:
            print (colored(files, "yellow"), end = ' ')
        k = 0
    if k == 0:
        print()

def pwd():
    print (colored(os.getcwd(), "cyan"))

def cd(path):
    try:
        if path != "cd":
            path.split(' ', 1)
            os.chdir(path.split(' ', 1)[1])
        else:
            os.chdir(curdir)
    except Exception:
        print (colored("Directory doesn't exist!", "red"))

def mkdir(newdir):
    exists = 0
    newdir.split(' ', 1)
    for x in os.listdir(os.curdir):
        if x == newdir.split(' ', 1)[1]:
            exists = 1
            break
    if exists == 0:
        os.mkdir(newdir.split(' ', 1)[1])
    else:
        print(colored("Such file allready exists!", "red"))

def cp(arguments):
    original = arguments.split()[1]
    target = arguments.split()[2]
    try:
        shutil.copyfile(original, target)
    except Exception:
        if os.path.isdir(original) or os.path.isdir(target):
            print (colored("Can't copy Directory or To Directory!", "red"))
        else:
            print (colored("No such file!", "red"))

def mv(arguments):
    path = arguments.split()[1]
    moveto = arguments.split()[2]
    try:
        path = os.path.abspath(path)
        shutil.move(path, moveto)
    except Exception:
        print (colored("No such file or directory!", "red"))

def rm(path):
    arg = path.split(' ', 1)[1]
    if os.path.isfile(arg) or os.path.isdir(arg):
        print ("Are you sure you want to delete ", arg, " ? [y/n]")
        s = input()
        if s == 'y':
            if os.path.isfile(arg):
                os.remove(path.split(' ', 1)[1])
            if os.path.isdir(arg):
                shutil.rmtree(arg)
        else:
            return
    else: 
        print (colored("No such file or directory!", "red"))

def rmdir(argument):
    path = argument.split(' ', 1)[1]
    if os.path.isdir(path):
        if len(os.listdir(path)) == 0:
            shutil.rmtree(path)
        else:
            print (colored("The directory is not empty!", "red"))
    else:
        print (colored("Not a directory!", "red"))

def run(command):
    inp = ' '.join(command.split()[1:])
    process = subprocess.Popen(inp.split(), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = process.communicate()
    print (stdout.decode(), end = '')
    print (stderr.decode(), end = '')
    print()
    
while True:
    cin = input()
    if cin == "exit":
        break
    if cin == "ls":
        ls()
    elif cin == "pwd":
        pwd()
    elif cin.startswith('cd'):
        cd (cin)
    elif cin.startswith('mkdir'):
        if cin == "mkdir":
            print (colored("This command needs an argument!", "red"))
            print("Try ", colored("mkdir dir_name", "yellow"))
        else:
            mkdir(cin)
    elif cin.startswith('cp'):
        if cin == "cp":
            print (colored("This command needs arguments!", "red"))
            print("Try ", colored("cp arg_1 arg_2", "yellow"))
        else:
            cp(cin)
    elif cin.startswith('mv'):
        if cin == "mv":
            print (colored("This command needs arguments!", "red"))
            print("Try ", colored("mv arg_1 arg_2", "yellow"))
        else:
            mv(cin)
    elif cin.startswith('rmdir'):
        if cin == "rmdir":
            print (colored("This command needs an argument!", "red"))
            print ("Try ", colored("rmdir directory_name", "yellow"))
        else:
            rmdir(cin)
    elif cin.startswith('rm'):
        if cin == "rm":
            print (colored("This command needs an argument!", "red"))
            print ("Try ", colored("rm file_or_directory", "yellow"))
        else:
            rm(cin)
    elif cin.startswith('run'):
        run(cin)
    else:
        print(colored("Command not found!", "green"))

