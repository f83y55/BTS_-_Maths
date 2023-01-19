import os, json

def file_load(filename:str) -> str:
    st = ""
    with open(filename, 'r', encoding='utf-8') as file:
        st = file.read()
    return st
    
def file_save(filename:str, st:str):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(st)
        #print(f"saved as {filename}")

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


if __name__ == "__main__" :
    MAINROOT:str = '.'
    BRIQUE:str = "brique_index.html"
    NAV:str = os.path.join("nav", "nav.html")
    dc:dict = {}
    ls:list = [element for element in os.listdir(os.path.join(MAINROOT)) if os.path.isdir(os.path.join(MAINROOT, element))]
    ls.sort()
    for rep in ls :
        for name in [element for element in os.listdir(os.path.join(MAINROOT, rep)) if element.endswith(".html")] :
            if os.path.exists(os.path.join(MAINROOT, rep, f"{name[:-5]}.json")) :
                dc[name] = (json_load(os.path.join(MAINROOT, rep, f"{name[:-5]}.json"))["name"], rep)
            html = file_load(os.path.join(MAINROOT, BRIQUE))
            html.replace('#####list#####', '\n'.join([f'<li> <a href="{os.path.join(MAINROOT, y[1], x)[:-5]}.html"> {y[0]} </a> </li>' for x, y in dc.items()]))
            nav = file_load(os.path.join(MAINROOT, NAV))
            nav.replace("@import \"../style/nav.css", "@import \"./style/nav.css")
            html.replace('#####nav#####', nav)
            file_save("index.html", html)
            


