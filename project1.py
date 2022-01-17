#Patrick M Lopata
#31036957
import os
import sys
import os.path
from shutil import copyfile
from datetime import datetime
from pathlib import Path
os.chdir(os.path.sep)
Direct=[]
FandD=[]
def sortfile(input: Path) -> str:
    file=[]
    index=0
    input = str(input)
    if(input[0:2] == "D " or input[0:2]== "R "):
        input = input[2:len(input)+1]
    input = Path(input)
    while index < len(os.listdir((input))):
        if os.path.isfile(os.path.join(input, os.listdir(input)[index])):
            file.append(os.path.join(input, os.listdir(input)[index]))
        index= index + 1
    index=0
    file.sort()
    FandD.extend(file)
    while index < len(file):
        print(file[index])
        index = index + 1


def sortdir(input: str)-> None:
    Direct=[]
    index= 0
    input= str(input)
    if(input[0:2] == "D " or input[0:2]== "R "):
        input = Path(input[2:len(input)+1])
    input = Path(input)
    sortfile(input)
    while index < len(os.listdir((input))):
        file_path = Path(os.path.join(input, os.listdir(input)[index]))
        #full path ^
        if os.path.isdir(file_path):
            Direct.append(file_path)
        index= index +1
    index2 = 0
    Direct.sort()
    while index2 < len(Direct):
        sortdir(Direct[index2])
        index2 = index2 +1
    
def section_1(ui: str) -> str:
    try:
        if ui[0]=="D":
           sortfile(ui)
        else:
            if ui[0]=="R":
                    sortdir(ui)
            else:
                print("ERROR")
                section_1(input())
               
    except :
        print("ERROR")
        section_1(input())

interesting_files=[]
def section_2(ui2:Path) -> str:
    index=0
    try:
        if(ui2=="A"):
            while index < len(FandD):
                interesting_files.append(FandD[index])
                print(FandD[index])
                index=index+1
        if(ui2[0:2]=="N "):
            while index < len(FandD):
                if(ui2[2:] == os.path.basename(FandD[index])):
                    print(FandD[index])
                    interesting_files.append(FandD[index])
                index = index + 1
        if(ui2[0:2]=="E "):
            while index < len(FandD):
                consid = FandD[index]
                if(ui2[2:]==consid[-len(ui2[2:]):]):
                    print(FandD[index])
                    interesting_files.append(FandD[index])
                index = index + 1
        if(ui2[0:2]=="T "):
            while index < len(FandD):
                consid = FandD[index]
                try:
                    with open(FandD[index]) as file:
                        if ui2[2:] in file.read():
                            print(FandD[index])
                            interesting_files.append(FandD[index])
                except :
                    continue
                index = index + 1
        if(ui2[0]=="<"):
            numbers = ui2[2:]
            number = int(numbers)
            while index < len(FandD):
                size = os.path.getsize(FandD[index])
                if(number > size):
                    print(FandD[index])
                    interesting_files.append(FandD[index])
                index = index + 1
        if(ui2[0]==">"):
            numbers = ui2[2:]
            number = int(numbers)
            while index < len(FandD):
                size = os.path.getsize(FandD[index])
                if(number < size):
                    print(FandD[index])
                    interesting_files.append(FandD[index])
                index = index + 1
        if(len(interesting_files) == 0):
            sys.exit()
    except:
        print("ERROR")
        section_2(input())

def section3(ui3:str) -> str:
    ui3 = str(ui3)
    index = 0
    try:
        if(ui3=="F"):
                while index < len(interesting_files):
                    length = len(interesting_files[index])-4
                    consid = interesting_files[index]
                    if(consid[length:]==".txt"):
                        with open(interesting_files[index]) as file:
                            print(file.readline().rstrip())
                    else:
                        print("NO TEXT")
                    index = index + 1
        else:
                if(ui3=="D"):
                    while index < len(interesting_files):
                        file_name= interesting_files[index] + ".dup"
                        with open(file_name, "r") as read:
                            with open(file_name,"w") as write:
                                read.write(write.read())
                        index =  index + 1
                else:
                    if(ui3=="T"):
                        while index < len(interesting_files):
                            os.utime(interesting_files[index])
                            index = index + 1
                    else:
                        print("ERROR")
                        inputB = Path(input())
                        section3(inputB)
    except:
        print("ERROR")
        section3(input())
if __name__ == '__main__':
    input1=input()
    section_1(input1)
    input2=input()
    section_2(input2)
    input3=input()
    section3(input3)
