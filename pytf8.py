
def affiche(first:int=0, last:int=1000, sep:str=" ") :
    for k in range(first, last+1) :
        print(str(k).encode("utf-8").decode('utf-8'), end=sep)
