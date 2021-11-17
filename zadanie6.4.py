
print("Podaj wartości kolorów R G B w systemie dziesiętnym")
r=int(input("R: "))
g=int(input("G: "))
b=int(input("B: "))
#zamiana na wartości
Rp=r/float(255)
Gp=g/float(255)
Bp=b/float(255)
Cmax = max(Rp, Gp, Bp)
Cmin = min(Rp, Gp, Bp)
delta = Cmax - Cmin
if delta == 0:
    h = 0
elif Cmax == Rp:
    h = 60 * (((Gp - Bp)/delta)%6)
elif Cmax == Gp:
    h = 60 * (((Bp - Rp)/delta)+2)
elif Cmax == Bp:
    h = 60 * (((Rp - Gp)/delta)+4)
if Cmax == 0:
        s = 0
else:
    s = (delta/Cmax)*100
v = Cmax*100
print("Wartości RGB po konwersji na HSV: ",h,"°,",s,"%,",v,"%")
