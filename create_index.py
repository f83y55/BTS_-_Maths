import os

def file_load(filename:str) -> str:
    st = ""
    with open(filename, 'r', encoding='utf-8') as file:
        st = file.read()
    return st
    
def file_save(filename:str, st:str):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(st)
        #print(f"saved as {filename}")
 
if __name__ == "__main__" :
    MAINROOT = '.'
    BRIQUE = "brique_index.html"
    dc = {}
    for rep in [element for element in os.listdir(os.path.join(MAINROOT)) if os.path.isdir(os.path.join(MAINROOT, element))] :
        for name in [element for element in os.listdir(os.path.join(MAINROOT, rep)) if element.endswith(".html")] :
            if os.path.exists(os.path.join(MAINROOT, rep, f"{name[:-5]}.name")) :
                dc[name] = (file_load(os.path.join(MAINROOT, rep, f"{name[:-5]}.name")), rep)
            else :
                dc[name] = (name[:-5], rep)
    file_save("index.html", file_load(os.path.join(MAINROOT, BRIQUE)).replace('#####', '\n'.join([f'<li> <a href="{os.path.join(MAINROOT, y[1], x)[:-5]}.html"> {y[0]} </a> </li>' for x, y in dc.items()])))
            


