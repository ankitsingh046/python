import os
import shutil

# current directory
# print(os.getcwd())


# change directory
# os.chdir(r"D:\New folder")


# create folder
# if os.path.exists(r"D:\New folder\os_pyhton"):
#     print('Already exists')
# else:
#     os.mkdir(r"D:\New folder\os_pyhton")


# create folder in folder in one step
# if os.path.exists('os_modules2'):
#     print('Already exists')
# else:
#     os.makedirs('os_modules2/module1')



# create file
# open(r"D:\New folder\os_pyhton\os_module.py", 'a').close()
# open(r'os_modules2/os.txt', 'a').close()


# list directory
# print(os.listdir())
# print(os.listdir(r"D:\New folder"))


# path of listdir()
# for item in os.listdir(r"D:\New folder"):
    # path = os.path.join(os.getcwd(), item)
    # print(path)


# os.walk
# file_iter = os.walk(r"D:\MANORANJAN")
# for path, folder, file in file_iter:
#     print(f'current path: {path},\n\nfolder: {folder},\n\nfile: {file}')
#     print()


# del with shutil
# shutil.rmtree('singh')


# copy & move folder with shutil
# shutil.copytree('new','New folder/new')
# shutil.move('new', 'New folder/new2')


# copy & move file with shutil
# shutil.copy('os.txt', 'new/os.txt')
# shutil.move('os.txt', 'New folder/os.txt')