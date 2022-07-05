#pb3 cu dictionare

# def check_logs():
#     acces = {}
#     for i in range(1, 4):
#         acces[input(f"User PC.{i}")] = input(f"User password.{i}")
#     for user,parola in acces.items():
#         print(f"{user} --> {parola}")
#
# check_logs()

#pb4
#
# angajat1 = {'nume': 'Ana-Maria Popescu','departament': 'IT','ID': 3409,'Salar': 4560,}
# angajat2 = {'nume': 'Marian Muntean','departament': 'IT','ID': 2235,'Salar': 4556,}
# angajat3 = {'nume': 'Maria Manea','departament': 'HR','ID': 1908,'Salar': 6755,}
# angajat4 = {'nume': 'Oana Popa','departament': 'HR','ID': 1977,'Salar': 5400,}
# angajat5 = {'nume': 'David Codru','departament': 'Management','ID': 1988,'Salar': 12900,}
# lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]
#
# #a
# for angajat in lista_dict:
#     if angajat['Salar'] > 5000:
#         print(f"{angajat['nume']} -> {angajat['departament']}{angajat['ID']}")
#
# #b
# list = []
# for angajat in lista_dict:
#     if angajat['departament'] != "Management":
#         list.append(angajat['nume'])
# print(list)

#c
# counter=0
# suma_sal=0
# for angajat in lista_dict:
#     if angajat['departament'] == "HR":
#         counter+=1
#         suma_sal+=angajat['Salar']
#
# media=suma_sal/counter
# print(media)

#pb2/lab2

def suma(lista: list):
    pass
def medie(lista: list):
    pass
def putere(lista: list):
    pass
meniu = {
"1": medie,
"2": suma,
"3": putere
}

numbers = []
data = input("Introduceti numere. Cand sunteti gata, introduceti x:\n")
while data != 'x':
    numbers.append(float(data))
    data = input("number:")
print(numbers)

mesaj=input("""Meniu
1. Media numerelor
2. Suma numerelor
3. Puterea numerelor din lista de numere
4. Iesire
Introduceti optiunea dvs:""")
my_function=meniu[mesaj]
rezultat=my_function(numbers)
print(rezultat)


