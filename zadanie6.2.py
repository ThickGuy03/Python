listOfStudents=["Kasia","Basia","Marek","Darek"]
listOfStudents.append("Józek")
print(listOfStudents)
listOfStudents.extend(["Ania","Basia"])
print(listOfStudents)
listOfStudents2=sorted(listOfStudents)
print(listOfStudents2)
print(listOfStudents2[3])
print(listOfStudents2[:2])
print(listOfStudents2[-2:])
listOfStudents2.remove("Basia")
listOfStudents2.remove("Basia")
print(listOfStudents2)
print(len(listOfStudents2))
t=(listOfStudents2)
print (t)