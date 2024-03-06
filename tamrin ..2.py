hesab = 0
while 1:
    darkhast = input("darkhast:")
    if darkhast == "khroj":
        break
    elif darkhast == "variz":
        n = int(input("meghdar:"))
        hesab += n
    elif darkhast == "bardasht":
        n = int(input("meghdar")) 
        hesab -= n
    elif darkhast == "mojodi":
        print("mojodi",hesab)
           
