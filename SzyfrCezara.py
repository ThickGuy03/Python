def szyfruj(x,klucz):
    zaszyfrowany=""
    for i in range(len(x)):
        if ord(x[i])>122-klucz:
            zaszyfrowany+= chr(ord(x[i])+klucz-26)
        elif ord(x[i])>96-klucz and ord(x[i])<122-klucz:
            zaszyfrowany+= chr(ord(x[i])+klucz)
        elif 31<ord(x[i])<65 or 90<ord(x[i])<97:
            zaszyfrowany+=x[i]
        elif ord(x[i])<97-klucz and klucz<0:
            zaszyfrowany+=chr(ord(x[i])+26+klucz)
        elif ord(x[i])<65-klucz and klucz<0:
            zaszyfrowany+=chr(ord(x[i])+26+klucz)
        elif ord(x[i])>90-klucz:
            zaszyfrowany+= chr(ord(x[i])+klucz-26)
        elif ord(x[i])>64 and ord(x[i])<122-klucz:
            zaszyfrowany+= chr(ord(x[i])+klucz)
    return zaszyfrowany
def odszyfruj(tekst2,klucz):
    odszyfrowany=""
    for i in range(len(tekst2)):
        if ord(tekst2[i])>122-klucz:
            odszyfrowany+= chr(ord(tekst2[i])-klucz+26)
        elif ord(tekst2[i])>96+klucz and ord(tekst2[i])<122+klucz:
            odszyfrowany+= chr(ord(tekst2[i])-klucz)
        elif 31<ord(tekst2[i])<65 or 90<ord(tekst2[i])<97:
            odszyfrowany+=tekst2[i]
        elif ord(tekst2[i])<122+klucz and klucz<0:
            odszyfrowany+=chr(ord(tekst2[i])-26-klucz)
        elif ord(tekst2[i])<65+klucz and klucz<0:
            odszyfrowany+=chr(ord(tekst2[i])-26-klucz)
        elif ord(tekst2[i])>90+klucz:
            odszyfrowany+= chr(ord(tekst2[i])+klucz-24)
        elif ord(tekst2[i])>65 and ord(tekst2[i])<122+klucz:
            odszyfrowany+= chr(ord(tekst2[i])-klucz)
    return odszyfrowany