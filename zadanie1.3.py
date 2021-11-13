a=input("Wprowadź litere alfabetu: ").lower()
samogloski=['a','e','i','o','u','y','ą','ę','ó']


if a in samogloski:
    print("Litera "+a+" należy samogłosek")
      
else:
    print("Litera "+a+" należy spółgłosek")