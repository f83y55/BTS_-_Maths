import unidecode, os, json

def file_load(filename:str, dc:dict) -> str:
    st = ""
    with open(filename, 'r', encoding='utf-8') as file:
        st = file.read()
    return st.format(**dc)

def file_save(filename:str, st:str):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(st)

def json_load(filename:str) -> str:
    data = {}
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def json_save(filename:str, data:dict):
    if not data :
        data = {}
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

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
    data = {"name":folder_name, "web_name":web_name}
    confirmation = input(f"Name : {folder_name}\n Webname : {web_name}\nConfirmation (*:yes/n:no)")
    if confirmation.upper() == "N" :
        pass
    else :
        try :
            os.makedirs(os.path.join(MAINROOT, web_name), exist_ok=True)
            os.makedirs(os.path.join(MAINROOT, web_name, "assets"), exist_ok=True)
            if not os.path.exists(os.path.join(MAINROOT, web_name, f"{web_name}.html")) :
                file_save(os.path.join(MAINROOT, web_name, f"{web_name}.html"), file_load(os.path.join(MAINROOT, BRIQUE), data))
            json_save(os.path.join(MAINROOT, web_name, f"{web_name}.json"), data)
        except Exception as e:
            print(e)


