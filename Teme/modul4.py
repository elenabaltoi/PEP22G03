# #pb1
# def my_function(x):
#     y = 3 * x
#     return 3*x**2-4*y+4
# my_number=input("Introduceti x")
# n=0
# x=range(10,20)
# z=[]
# for i in x:
#     result=my_function(i)
#     z.append(result)
#
# for x in range(10,20):
#     if n<=10:
#         print(f'============= X={x} ============= \n Rezultatul functiei :', z[n])
#         n += 1


# #pb2

nr=input("Cate carti doriti sa adaugati in biblioteca? ")
nume= []
autor=[]
an= []
carte={}
for i in range(int(nr)):
    nume_carte= input("Numele cartii:")
    an_publicatie= input("Anul publicarii :")
    nume_autor=input("Numele autorului: ")
    nume.append(nume_carte)
    autor.append(nume_autor)
    an.append(an_publicatie)

for i in range(int(nr)):

    print(f"========Cartea {i+1}======== ")
    print(f"Numele cartii: {nume[i]}")
    print(f"Numele autorului: {autor[i]}")
    print(f"Anul publicarii: {an[i]}")

for i in range(len(nume)):
    carte['nume'] = nume[i]
    carte['autor'] = autor[i]
    carte['an'] = an[i]
    print("Cartile dvs sunt:", carte)


