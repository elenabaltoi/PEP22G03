# #functii
#
# def putere_doi(x):
#     print(x**x)
#     #return None #implicit
#
# def putere_n(x,n):
#     print(x**n)
#
# putere_doi(3)
# putere_n(4,5)
#
# print(putere_n(3,3))

# def putere_n(x,n):
#     return x**n
# result=putere_n(4,5)
# print(result)
# print(putere_doi(3))

# #argumente
# def putere_n(x,n):
#     print("variabilele sunt:", x,n)
#     return x**n
#
# putere_n(3,4)
# #print("variabilele sunt: ', x,n) - local scope only
#
# def putere_n(n,x):
#     print("variabilele sunt:", x,n)
#     return x**n
#
# putere_n(3,4)
#
# #argumente de tip cheie
# def putere_n(n,x, add=100):
#     print('Valoare argument cheie', add)
#     print("variabilele sunt:", x,n)
#     return x**n + add
#
# putere_n(3,4, add=201)
# putere_n(3,4,200)
#
# def putere_n(n,x, add=100, sub=0):
#     print('Valoare argument cheie', add)
#     print('Valoare argument cheie', sub)
#     print("variabilele sunt:", x,n)
#     return x**n + add
#
# putere_n(3,4, add=201)
# putere_n(3,4,200)
# putere_n # (3,4,add=200, 150)
# #print(" #variabilele sunt: ', x,n) - local scope only
#

#variabilele

# add=200
# sub=100
# div=3
# def putere_n(n,x, add=100, sub=0):
#      print('Valoare argument cheie', add)
#      print('Valoare argument cheie', sub)
#      print("variabilele sunt:", x,n)
#      return (x**n + add + sub) / div
# print(putere_n(3,3))
# print(putere_n(3,3, 25, -25))

# #variabile globale
# add=200
# sub=100
# div=3
# def putere_n(n,x, add=100, sub=0):
#     global div
#     print('Valoare argument cheie', add)
#     print('Valoare argument cheie', sub)
#     print("variabilele sunt:", x,n)
#     div=5
#     return (x**n + add + sub) / div
# print(putere_n(3,3, 25, -25))
# print("div result: ", div)


#nested functions
#  #global
# arg1=2
# def level1(arg1):
#     print("inainte de modificare", arg1)
#     def level2(arg2):
#         global arg1
#         arg1=10
#         print(arg2 + arg1)
#     level2(3)
#     print("dupa modificare", arg1)
#
# level1(1)
# print("variabila globala", arg1)


#nonlocal
# arg1=2
# def level1(arg1):
#     print("inainte de modificare", arg1)
#     def level2(arg2):
#         nonlocal arg1
#         arg1=10
#         print(arg2 + arg1)
#     level2(3)
#     print("dupa modificare", arg1)
#
# level1(1)
# print("variabila globala", arg1)

#call method
def test ():
    print(("Dummy"))

test()  #cand punem cele doua paranteze dupa def functiei i se face call
test.__call__.__call__()

test.abcd=3
print(dir(test))

