from categories import*
import pathlib


folder_path=input("Enter folder path to organize: ")

#validate folder path
if(folder_path==""):
    print("Please enter a valid folder path.")
    folder_path=input("Enter folder path to organize: ")
folder=pathlib.Path(folder_path)

#check if folder exists

if(folder.is_dir()):
    print("Folder exists.")
else:
    print("this folder does not exist.")
    print("Please enter a valid folder path.")
    folder_path=input("Enter folder path to organize: ")
    folder=pathlib.Path(folder_path)

#get all files in the folder
folder_contents=folder.iterdir()
statistics = {category: 0 for category in file_types}
statistics["Others"] = 0
if(not any(folder_contents)):
    print("The folder is empty.")
    exit()
for item in folder_contents:
    if(item.is_dir()):
        continue
    if(item.is_file()):
        file_extension=item.suffix.lower()
        moved=False
        for category, extensions in file_types.items():
            if file_extension in extensions:
                category_folder=folder/category
                category_folder.mkdir(exist_ok=True)
                item.rename(category_folder/item.name)
                statistics[category] += 1
                moved=True
                break
        if not moved:
            statistics["Others"] += 1
            others_folder=folder/"Others"
            others_folder.mkdir(exist_ok=True)
            item.rename(others_folder/item.name)
print("Files have been organized successfully.")

print("\nFile Type Statistics:")
for category, count in statistics.items():
    print(f"{category}: {count} files")
print("Total files organized:", sum(statistics.values()))
