import os
import shutil
import argparse
import re
from pathlib import Path

#EXTENSIONS
EXTENSIONS = {
"images" : ('.jpeg', '.png', '.jpg', '.svg', '.webp', '.JPG', '.PNG'),
"videos" : ('.avi', '.mp4', '.mov', '.mkv','.MP4'),
"docs" : ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.html'),
"music" : ('.mp3', '.ogg', '.wav', '.amr'),
"apps" : ('.exe', '.dmg', '.pkg'),
"archs" : ('.zip', '.gz', '.tar') }

#EXTENSIONS WHICH WERE SORTED
extension_set = set()

#SORTED FILES
files_dict = {
    "images":[],
    "videos":[],
    "docs":[],
    "music":[],
    "apps":[],
    "archives":[],
    "another":[],
}

#CONSOLE ARGS
parser = argparse.ArgumentParser(description = "sort files by type")
parser.add_argument("folder_path")
args = parser.parse_args()
path = args.folder_path

#DIRS
dirs = ["images", "videos", "docs", "music", "archives", "apps", "bin", "another"]

#TRANSLITION
TRANS = {}
for c, l in zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ", ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

#NORMALIZING TEXT
def normalize(line):
    separate=line.rsplit(".", 1)
    line = separate[0]
    line = line.translate(TRANS)
    line = re.sub(r"[^a-zA-Z0-9]", "_", line)
    try:
        return str(line+"."+separate[1])
    except IndexError:
        return(line)

#CUTTING TEXT TO 20 SYMBOLS
def cut(ins):
    if len(ins)>20:
        ins=ins[:17] +"..."
    return ins

#MOVING EMPTY FOLDERS TO BIN
def move_empty_folders(path):
    with os.scandir(path) as files:
        for file in files:
            if file.name not in set(dirs):
                if os.path.isdir(file.path):
                    if file.name not in set(dirs):
                        target_dir = os.path.join(path, "bin")
                        os.makedirs(target_dir, exist_ok = True)
                        shutil.move(file.path, os.path.join(target_dir, file.name))

    
#NORMALIZING FILE'S NAMES
def rename_all(path):
        with os.scandir(path) as files:
                for file in files:
                    if os.path.isdir(file):
                        rename_all(file.path)
                    else:
                        os.rename(file.path, os.path.dirname(file.path) + "/" + normalize(file.name))

#SORTING
def sort(path, path_ = path):
    with os.scandir(path_) as files:
        for file in files:
            extension_set.add((Path(file.path).suffix))
            for list, dir in zip(EXTENSIONS.values(), dirs):
                if file.name.endswith(list):
                    try:
                        files_dict[dir].append(file.name)
                        target_dir = os.path.join(path, dir)
                        os.makedirs(target_dir, exist_ok=True)
                        shutil.move(file.path, os.path.join(target_dir, file.name))
                    except FileNotFoundError:
                        continue
                #FINDING AND UNARCHIVATING ZIPS
                elif file.name.endswith(EXTENSIONS["archs"]):
                    files_dict["archives"].append(file.name)
                    target_dir = os.path.join(path, "archives"+ "/" + normalize((file.name).rsplit(".",1)[0]))
                    os.makedirs(target_dir, exist_ok = True)
                    try:
                        shutil.unpack_archive(file.path, target_dir)
                    except shutil.ReadError:
                        ...
                elif os.path.isdir(file.path) and file.name not in dirs:
                    sort(path, path_ + "/" + file.name)
                    
    #COLLECTING ALL UNKNOWN EXTENSION FILES
    with os.scandir(path_) as files:
        for file in files:
            try:
                if os.path.isfile(file.path):
                    files_dict["another"].append(file.name)
                    target_dir = os.path.join(path, "another")
                    os.makedirs(target_dir, exist_ok=True)
                    shutil.move(file.path, os.path.join(target_dir, file.name))
            except FileNotFoundError:
                continue

#ENTRY POINT
if __name__ == "__main__":

    sort(path)
    rename_all(path)
    move_empty_folders(path)
    
    #PRINTING SORTED FILES
    if extension_set != {""}:
        for i, _ in files_dict.items():   
            if _:
                print("|{:^25}|".format(""))
                print("|{:^25}|".format(i))
                for i in _:
                    print("|{:^25}|".format(cut(i)))
                print("|{:^25}|".format("-----------"))
        print("|{:^25}|".format(""))
        
        all_extensions = set()
        for extensions_tuple in EXTENSIONS.values():
            all_extensions.update(extensions_tuple)

        unknown_ext = extension_set - all_extensions
        print(f"unknown by script extensions: {unknown_ext}")
        print(f"previously known by script extensions: {extension_set - unknown_ext}")
    else:
        print("No sort was performed")
    