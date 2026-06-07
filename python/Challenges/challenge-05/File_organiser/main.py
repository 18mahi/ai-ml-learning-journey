from categories import*
import os


folder_path=input("Enter folder path to organize: ")
try:
    if(folder_path==""):
        print("Please enter a valid path.")
        path=input("Enter folder path to organize: ")

except Exception as e:
    print("An error occurred: ", e)
    exit()

if os.path.exists(folder_path):
    #we do not use here os.listdir() because checks specifically if it is a folder or not,
    #and if it is a folder, it will ignore it and move to the next file in the folder, 
    # but os.listdir() will list all the files and folders in the directory, and we will have to check if it is a file or not,
    # which is an extra step and can be time-consuming if there are many files and folders in the directory. 
