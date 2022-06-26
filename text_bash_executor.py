import os

def executor(file_name):
    with open(file_name) as f:
        commands = f.readlines()
        def clean(command):
            return command.strip()
        commands = list(map(clean,commands))
        for command in commands:
            os.system(command)
executor("std.txt")