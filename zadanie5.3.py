import re
password=input("Wprowadz hasło by sprawdzić jego bezpieczeństwo: ")

literaM=re.search(r"[a-z]",password) is None
literaD=re.search(r"[A-Z]",password) is None
cyfra=re.search(r"[0-9]",password) is None
znakSpecjalny=re.search(r"[$#@]",password) is None
if literaM==False and literaD==False and cyfra==False and znakSpecjalny==False and len(password)>=6 and len(password)<=16:
    print("Twoje hasło spełnia wymogi")
else:
    print("Hasło jest zbyt słabe")