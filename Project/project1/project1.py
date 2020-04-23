# create saperete folders after searching for extension and move the files.

import os, shutil

# Extensions to be searched
dict_extensions = {
    'Audios_extension' : ('.mp3', '.m4a', '.wav', '.flac'),
    'Videos_extension' : ('.mp4', '.mkv', '.MKV', '.mpeg'),
    'Documents_extension' : ('.docx', '.pdf', '.txt', '.csv'),
    'Images': ('.jpg', '.png', '..jpeg', '.img')
}

# function takes 2 input as directorypath and extension to be searched and append into list datastructure
def file_finder(folder_path, file_extension):
    lists = []
    for file in os.listdir(folder_path):
        for item in file_extension:
            if file.endswith(item):
                lists.append(file)
        
    return lists


# folderpath = os.getcwd() #directory to be searches for extensions
folderpath = (r"D:\Personal")

for file_name, file_extension in dict_extensions.items():  
    folder_name = file_name.split('_')[0]
    folder_path = os.path.join(folderpath, folder_name)
    # os.mkdir(folder_path)
    for item in file_finder(folderpath, file_extension ):  #function call file_finder in loop
        item_path = os.path.join(folderpath, item)
        if os.path.exists(folder_path):   #check if folder already exists
            item_new_path = os.path.join(folder_path,item)
            try:
                shutil.move(item_path, item_new_path)
            except Exception as e:
                print(e)
        else:
            try:
                os.mkdir(folder_path)    #create a folder
                item_new_path = os.path.join(folder_path, item)
                shutil.move(item_path, item_new_path)   #move files in ceated folder
            except Exception as e:
                print(e)
