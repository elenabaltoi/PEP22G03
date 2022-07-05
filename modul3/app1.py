# # ex 1
# cnp = input("Introduceti primele 7 cifre din cnp")
# anul_nasterii = int(cnp[1:3])
# print(anul_nasterii)
# anul_curent = 2022
# if int(cnp[0]) > 2:
#     anul_nasterii += 2000
# else:
#     anul_nasterii += 1900
# print(anul_nasterii)
#
# if anul_curent == anul_nasterii > 18:
#     print(anul_curent == anul_nasterii > 18)
#     print("Sunteti major")
# else:
#     print("Sunteti minor")
#
# # == e comparatie
# print(2000 - True)
# print(True - 2000)
# print(True > 2000)
# print(dir(True))
#
#
# #ex2 cu nr pare
# #var1
# numar = int(input("Introduceti un numar: "))
# i = 0
# while i < numar:
#     if ( i % 2) == 0:
#         print(i)
#     i += 1
#
# #var2
#
# number = int(input("Type a number: "))
# start = 0
# if start+2 <= number:
#     start+=2
#     print(start)
# if start+2 <= number:
#     start+=2
#     print(start)
# if start+2 <= number:
#     start+=2
#     print(start)
# if start+2 <= number:
#     start+=2
#     print(start)
#
# #ex2 cu loop
# #nu curpinde si pe 6
# number = int(input("Type a number: "))
# counter=0
# while counter<number:
#     if not counter%2:
#         print(counter)
#     counter+=1
# #cuprinde si pe 6
# number = int(input("Type a number: "))
# counter=0
# while counter<=number:
#     if not counter%2:
#         print(counter)
#     counter+=1
#
# #ex3
# #var1
#
# optiuni = input('Cappucino......4 lei\nExpreso......3.5lei\nCe optiune alegeti?:[1,2]:')
# bani = int(input("Introduceti bancnota [5,10]:"))
# var1= '1'
# var2= '2'
# ban = 5
# ban1 = 10
# pret1 =4
# pret2 = 3.5
# if optiuni == var1 and bani == (ban or ban1) :
#     print("Vei primi restul de:",bani- pret1 )
# elif optiuni== var2 and bani == (ban or ban1):
#     print("Vei primi restul de:",bani- pret2 )
# # elif optiuni != (var1 and var2):
# #     print("Alegere gresita!")
# else:
#     print('Alegere gresita!')
#
# #var2
# print("1. Cappuccino     ... 4 lei","2. Espresso       ... 3.5 lei",sep="\n")
# Cappucino = 4
# Espresso = 3.5
# optiune = 0
# while not optiune:
#     optiune = int(input("Ce optiune alegeti? [1,2]: "))
#     if optiune == 1:
#         print("Ati ales optiunea 1")
#     elif optiune == 2:
#         print("Ati ales optiunea 2")
#     else:
#         print("Alegere gresita")
#         optiune = 0
#
# while True:
#     bani = int(input("Introduceti o banconta [5,10]: "))
#     if bani == 5:
#         print("Ati introdus 5 lei")
#         break
#     elif bani == 10:
#         print("Ati introdus 10 lei")
#         break
#     else:
#         print("Se permit doar bancnote de 5 sau 10 lei")
#         continue
#
# if optiune == 1:
#     print(f"Veti primi restul de {bani-Cappucino} lei","Produsul se livreaza...",sep="\n")
# elif optiune == 2:
#     print(f"Veti primi restul de {bani- Espresso} lei", "Produsul se livreaza...", sep="\n")
# else:
#     print("Alegere gresita")
#
#
# #pb4
# while input("Introduceti parola") != "7788":
#     print("Parola gresita. Mai incercati.")
#     counter += 1
#     if counter == 3:
#         break
# else:
#     print("Acces permis.")
#
