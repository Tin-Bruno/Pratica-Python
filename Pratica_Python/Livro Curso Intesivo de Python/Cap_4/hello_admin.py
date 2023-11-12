AcountGrupe = ["bruno", "carlos", "daniel", "adimin", "lucas",]
if AcountGrupe:
    for acount in AcountGrupe:
        if acount == "adimin":
            print("olá adimin, would like a report?")
        else:
            print("Olá " + acount + ", thanks for to make login again.")
else:
    print("We need find a more users.")
