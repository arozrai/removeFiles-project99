import time
import os
import shutil

def main():

    path = input("Which folder will you want to apply this program on? ")
    days = int(input("Delete files over what days old: "))
    seconds = time.time() - (days * 24 * 60 * 60)

    print(seconds)

    pathExists = os.path.exists(path)

    deletedFoldersCount = 0
    deletedFilesCount = 0

    if(os.path.exists(path)):
        for root_folder,folders,files in os.walk(path):
            if (seconds >= getFile_folderAge(root_folder)):
                remove_folder(root_folder)
                deletedFoldersCount += 1
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder,folder)
                    if (seconds >= getFile_folderAge(folder_path)):
                        remove_folder(folder_path)
                        deletedFoldersCount += 1
                for file in files:
                    file_path = os.path.join(root_folder,file)
                    if (seconds >= getFile_folderAge(file_path)):
                        remove_file(file_path)
                        deletedFilesCount += 1
    else:
        print("Folder was not found")
    print("Amount of folders deleted: ",deletedFoldersCount,", Amount of files deleted: ",deletedFilesCount)

def getFile_folderAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

def remove_folder(path):
    if not shutil.rmtree(path):
        print(path+" is removed successfully")
    else:
        print("Unable to delete the path")

def remove_file(path):
    if not os.remove(path):
        print(path+" is removed successfully")
    else:
        print("Unable to delete the path")

main()

# folder = os.path.join()

# daysUnchanged = st_ctime(os.stat(path))



# if (daysUnchanged > seconds):
#     root=os.path.splitext(path)
#     if ():
#         os.remove(path)
#     elif ():
#         shutil.rmtree()
