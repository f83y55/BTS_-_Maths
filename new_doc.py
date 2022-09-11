import unidecode, os

def file_load(filename:str) -> str:
    st = ""
    with open(filename, 'r', encoding='utf-8') as file:
        st = file.read()
    return st

def file_save(filename:str, st:str):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(st)

def valid_filename(st:str) -> str :
    name = unidecode.unidecode(st)
    name = "".join(x for x in name if x.isalnum() or x in "._- ()[]")[:255]
    for x in r"\/ " :
        name = name.replace(x, '_')
    return name



MAINROOT = "."
BRIQUE = "brique.html"

if __name__ == "__main__":
    folder_name = input("New folder name :\n")
    web_name = valid_filename(folder_name)
    confirmation = input(f"Name : {folder_name}\n Webname : {web_name}\nConfirmation (*:yes/n:no)")
    if confirmation.upper() == "N" :
        pass
    else :
        try :
            os.makedirs(os.path.join(MAINROOT, web_name), exist_ok=True)
            os.makedirs(os.path.join(MAINROOT, web_name, "assets"), exist_ok=True)
            if not os.path.exists(os.path.join(MAINROOT, web_name, f"{web_name}.html")) :
                file_save(os.path.join(MAINROOT, web_name, f"{web_name}.html"), file_load(os.path.join(MAINROOT, BRIQUE)))
            file_save(os.path.join(MAINROOT, web_name, f"{web_name}.name"), f"{folder_name}")
        except Exception as e:
            print(e)


