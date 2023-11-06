def offre(durée):
    if durée>120:
        price1=(durée-120)*0.5
    else:
        price1=100
    if durée>60:
        price2=(durée-60)*1
    else:
        price2=50
    if durée>30:
        price3=(durée-30)*1.5
    else:
        price3=20
    if durée>0:
        price4=durée*2
    tab=[200,price1,price2,price3,price4]
    return(tab)
for i in range(0,4):
    print("_____________________________________________________")
    print("                        MENU                         ")
    print("_____________________________________________________")
    print("1_Saisir le durée de communication\n2_Afficher la liste du cout mensulle par offre\n3_afficher l'offre la plue intéressante(moindre cout\n4_Quitter le programme)")
    print("")
    a=int(input("enter a number from the menu \n"))
    if a==1:
        dur=int(input("enter the number of the minutes consomed \n"))
        while dur=="":
            dur=int(input("enter the number of the minutes consomed \n"))
        b=dur
    if a==2:
        print(offre(dur))
    if a==3:
        print("l'offre la plue untéressante est:",min(offre(dur)))
    if a==4:
        break

