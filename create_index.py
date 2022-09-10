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
    dc = {}
    for rep in [element for element in os.listdir(os.path.join(MAINROOT)) if os.path.isdir(os.path.join(MAINROOT, element))] :
        for html in [element for element in os.listdir(os.path.join(MAINROOT, rep)) if element.endswith(".html")] :
            dc[html[:-4]] = os.path.join(MAINROOT, rep, html)
    file_save("index.html", file_load("brique.html").replace('#####', '\n'.join([f'<li> <a href="{y}"> {x} </a> </li>' for x, y in dc.items()])))
            


