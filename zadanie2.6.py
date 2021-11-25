import SzyfrCezara
tekst=input("Wprowadź tekst który chcesz zaszyfrować:")
klucz=int(input("Podaj klucz szyfrujący:"))
print("Zaszyforwany tekst wygląda tak:", SzyfrCezara.szyfruj(tekst,klucz))
tekst2=SzyfrCezara.szyfruj(tekst,klucz)
print("Odszyfrowant tekst wygląda tak:",SzyfrCezara.odszyfruj(tekst2,klucz))