txt=input()
extraWord="Python"
print(len(txt))
newWord=txt[0:3]+ extraWord + txt[10:len(txt-1)+6]
print (newWord)