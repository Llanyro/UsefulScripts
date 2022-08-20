from pathlib import Path
from os import path, mkdir
import os
import subprocess
import sys

root_folder: str
file_list: list = []      # The list of .o files to be compiled
banned_folders: list = []
banned_extensions: list = [".cpp", ".cxx", ".cc"]
bin_path: str = "./bin"
object_list: list = []


def file_in_banned_folder(p: str) -> bool:
    return any([True for folder in banned_folders if p.__contains__(folder)])


def has_banned_extension(p: str) -> bool:
    return any([True for extension in banned_extensions if p.__contains__(extension)])


if sys.argv.__len__() > 1:
    root_folder = sys.argv[1]
    file_name: str = "a.out"
    if sys.argv.__len__() > 2:
        file_name = sys.argv[2]

    # Fiind all files *.c files
    for a_file in Path(root_folder).glob('**/*.c*'):
        # If file is not a cpp
        if not has_banned_extension(str(a_file)):
            # If the file is in banned folder
            if not file_in_banned_folder(str(a_file)):
                file_list.append(str(a_file))
    #print(file_list)
    # We create the bin path if not exit
    # Or remove it if exit
    if path.exists(bin_path):
        os.system(f"rm -rf {bin_path}")
    mkdir(bin_path)

    # Now, we create an object for each file
    for file in file_list:
        # We get the name without path and extension
        filename: str = str(file).rsplit("/", 1)[-1].split(".")[0]
        os.system(f"gcc -c -o {bin_path}/{filename}.o {file}")
        object_list.append(f"{bin_path}/{filename}.o")
        print(f"gcc -c -o {bin_path}/{filename}.o {file}")
    object_list.reverse()

    final_command: str = f"gcc -g -o {bin_path}/{file_name} {' '.join(object_list)}"
    print(final_command)
    os.system(final_command)
else:
    exit(1)
