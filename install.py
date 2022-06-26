#insert logo here

#formating disk

from re import I
from subprocess import run, PIPE
import os
import time
import text_bash_executor
def physical_drives():
    command = ['lsblk -d -o name -n']
    output = run(command, shell=True, stdout=PIPE)

    output_string = output.stdout.decode('utf-8')
    output_string = output_string.strip()

    results = output_string.split('\n')
    return results

def partitions(disk):
    command = ['lsblk -o name -n -s -l']
    output = run(command, shell=True, stdout=PIPE)

    output_string = output.stdout.decode('utf-8').strip()

    results = []
    results.extend(output_string.split('\n'))
    results = [x for x in results if x != disk and disk in x]

    return results
blacklist = ["loop","sr"]
def filtered_disks(blacklist,disks = physical_drives()):
    filtered_drives = []
    for disk in disks:
        for keyword in blacklist:
            if not(keyword in disk):
                blacklisted = False
            else:
                blacklisted = True
                break
        if(not(blacklisted)):
            filtered_drives.append(disk)

    return filtered_drives

print(partitions("sda"))

def automactic_installation():
    print("𝓌𝑒𝓁𝒸𝑜𝓂𝑒 𝓉𝑜 𝒶𝓊𝓉𝑜𝓂𝒶𝓉𝒾𝒸 𝒾𝓃𝓈𝓉𝒶𝓁𝓁𝒶𝓉𝒾𝑜𝓃 𝓊𝓉𝒾𝓁𝒾𝓉𝓎")
    print("\n\n\n")
    os.system("lsblk -o NAME,SIZE,MODEL -I 8 -d")
    while(True):
        os.system("clear")
        print("enter your drive name, that you want the os installed in\n or press enter q to quit installer")
        
        os.system("lsblk -d -o NAME,SIZE,MODEL -I 8 -d")
        disks = physical_drives()
        user_selection = input("\n>").strip().replace("/dev/","").replace("dev/","")
        if(user_selection == "q" or user_selection == "'q'" or user_selection == "quit" ):
            break
            
        if(user_selection in physical_drives()):
            os.system("alias ${DISK}='/dev/"+user_selection+"'")
            break

        else:
            print("wrong disk name, please enter again")
            time.sleep(1)
            continue




def main():
    print("###logo###")
    time.sleep(1.5)
    os.system("clear")
    print("would you like the automatic mode, or advanced mode for installing")
    user_input= input(">").lower()
    if(user_input!= "advanced"):
        automactic_installation()

#     while(True):
#         os.system("clear")
#         print("enter your drive name to format\n enter 'q' to quit")
        
#         os.system("lsblk -d -o NAME,SIZE,MODEL -I 8 -d")
#         disks = physical_drives()
#         user_selection = input("\n>").strip().replace("/dev/","").replace("dev/","")
#         if(user_selection == "q" or user_selection == "'q'" or user_selection == "quit" ):
#             break
            
#         if(user_selection in physical_drives()):
#             os.system("sudo cfdisk /dev/"+user_selection)
#         else:
#             print("wrong disk name, please enter again")
#             time.sleep(1)
#             continue



# def advanced_mode(disk_names):
#     while(True):
#         os.system("clear")
#         print("welcome to formatting utility\n enter partition name")
#         os.system("lsblk -o NAME,SIZE,MODEL -I 8")
#         user_input = input(">")
#         partition_exists = False
#         for disk in disk_names:
#             for partition in partitions(disk):
#                 if(user_input == partition):
#                     partition_exists = True
                

#         if(not partition_exists):
#             print("##wrong partition name, please enter a correct name##")
#             time.sleep(1.2)
#             continue
#         print("what format would you like for the disk, ")


# main()
#selecting mount poin

#




