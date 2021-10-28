a=list(input("Wprowadź litere alfabetu: ").lower())
samogloski=['a','e','i','o','u','y','ą','ę','ó']
print(type(samogloski))
print(type(a))
print(a[0])

if a[0]==samogloski[0:]:
    print("Podana litera jest samogłoską")
      
else:
    print("Podana litera jest spółgłoską")
        