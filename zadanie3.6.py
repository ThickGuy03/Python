def look_and_say(s):
    wynik=[]
    i=0
    while i<len(s):
        liczba=1
        while i+1<len(s) and s[i]==s[i+1]:
            i+=1
            liczba+=1
        wynik.append(str(liczba)+s[i])
        i+=1
    return ''.join(wynik)
s="1"
n=10
for i in range(n):
    s=look_and_say(s)
    print(s)