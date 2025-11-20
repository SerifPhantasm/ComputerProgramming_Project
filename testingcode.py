import time
import json
import os
import sys

Line_ = ("---------------------------------------------------------")
FileName = "null"
NumOfFiles = 0
FileExtension = ""
DirectoryName = ""
FVar = "Folder_FF"
jsFile = "settings.json"
SysTwo = sys.argv[1:]

print("--")
print("--")



if not os.path.exists(FVar):
    os.mkdir(FVar)
    print(f"Folder, ({FVar}) has been Created")
else:
    print(f"The Folder, ({FVar}) already Exists.")


while True:
    FileName = input("What Would you want the file name to be? ")
    if len(FileName) >= 20:
        print(" Error: File Name is too long. ")
    else:
        print(FileName)
        break
else:
    print("")

while True:
    try:
        NumOfFiles = int(input("How many files would you like to create? "))
        if NumOfFiles >= 10000:
            print(" You're printing TOO MANY files. ")
        else:
            print(NumOfFiles)
            break
    except(ValueError):
        print(" ERROR: Wrong Value ")
    except(OverflowError):
        print(" ERROR: Overflow ")
    except:
        print(" ERROR, try again. ")
else:
    print("")
str(NumOfFiles)

while True:
    try:
        FileExtension = input("Name the file extension you would like the files to be. (eg .txt, .docx etc) ")
        if isinstance(FileExtension, int):
            print("You can't add numbers into the extension. ")
        else:
            print(FileExtension)
            break
    except:
        print("ERROR")
else:
    print("")

if FileExtension[0] != ".":
    FileExtension = "." + FileExtension

Json_1 = {
    "FileName": FileName,
    "NumOfFiles": NumOfFiles,
    "FileExtension": FileExtension
}
Json_str = json.dumps(Json_1)
try:
    with open(jsFile, "r") as file:
        _js_file_ = json.load(file)
except:
    print("settings.json not found.")
    print("Unable to Continue.")
    quit()

try:
    _js_file_["FileName"] = FileName
    _js_file_["NumOfFiles"] = NumOfFiles
    _js_file_["FileExtension"] = FileExtension
except:
    print("Something went Wrong.")
    quit()

try:
    with open(jsFile, "w") as file:
        json.dump(_js_file_, file)
except:
    print("Something went Wrong.")
    quit()


print(Line_)
print(Json_1)
print(Line_)



print(" ")
input(f"Do you want to create {NumOfFiles} of these files? Press Enter if YES. ")
for i in range(NumOfFiles):
    full_path = os.path.join(FVar, f"{FileName}_{i+1}{FileExtension}")
    try:
        with open(full_path, "w") as f:
            f.write(f"This is the {NumOfFiles} file.")
        print(f"Created file: {full_path}")
    except Exception as e:
        print(f"Failed to create file {full_path}: {e}")

print("end ")

