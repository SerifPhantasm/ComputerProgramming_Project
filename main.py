import time
import json
import os
import sys
from FileExtensionList import file_extensions 
# add custom message from here to json file and into files.
# add sys.argv 1-3 for filename, num of files, file extension, make input for cus-msg

Line_ = ("---------------------------------------------------------")
FileName = "null"
NumOfFiles = 0
FileExtension = ""
DirectoryName = ""
Folder_ = "Created Files"
jsFile = "settings.json"

CustomMessage = f"This is the {NumOfFiles} file."



if not os.path.exists(Folder_):
    os.mkdir(Folder_)
    print(f"Folder, ({Folder_}) has been Created")
else:
    print(f"The Folder, ({Folder_}) already Exists.")


def FileName_Valid():
    while True:
        FileName = input("What Would you want the file name to be? ")
        if len(FileName) >= 20:
            print(" Error: File Name is too long. ")
        else:
            print(FileName)
            break
    return FileName

def NumOfFiles_Valid():
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
    str(NumOfFiles)
    
    return NumOfFiles
    
def FileExtension_Valid():
    while True:
        try:
            FileExtension = input("Name the file extension you would like the files to be. (eg .txt, .docx etc) ").lower()
            print(FileExtension)

            if FileExtension not in file_extensions:
                print("Invalid File Extension.")
            else:
                print(f"{FileExtension} is a valid file extension.")
                break
            
        except:
            print("ERROR: Something went wrong. Please try again.")

    if FileExtension[0] != ".":
        FileExtension = "." + FileExtension

    return FileExtension

def CustomMessage_Valid():
    while True:
        try:
            CustomMessage = input("What custom message would you like to add to each file? ")
            print(CustomMessage)
            break
        except:
            print("ERROR: Something went wrong. Please try again.")
    return CustomMessage

def Info_ToJson(FileName, NumOfFiles, FileExtension, CustomMessage):
    Json_1 = {
        "FileName": FileName,
        "NumOfFiles": NumOfFiles,
        "FileExtension": FileExtension,
 #       "CustomMessage": CustomMessage 
 #          complete at uni
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

    return Json_1

print(" ")

def Creating_Files():
    Confirmation_ = input(f"Do you want to create {NumOfFiles} of these files? Type 'y' or 'n' ").lower()
    if Confirmation_ == "n":
        print("Exiting Program...")
        time.sleep(0.5)
        exit()
    else:
        for i in range(NumOfFiles):
            full_path = os.path.join(Folder_, f"{FileName}_{i+1}{FileExtension}")
            count = i + 1
            count_str = ("File Number." + str(count))
            try:
                with open(full_path, "w") as f:
                    f.write(CustomMessage + "\n" + count_str)
                print(f"Created file: {full_path}")
            except Exception as e:
                print(f"Failed to create file {full_path}: {e}")
    return

def Default_Setup():
    print("-")
    FileName = FileName_Valid()
    NumOfFiles = NumOfFiles_Valid()
    FileExtension = FileExtension_Valid()
    
    return FileName, NumOfFiles, FileExtension

# add custom message 


FileName, NumOfFiles, FileExtension = Default_Setup()
Json_1 = Info_ToJson(FileName, NumOfFiles, FileExtension)

Creating_Files()


