# # # -2=11111110
# # # 2=00000010
# # #  11111110
# #
# # my_test='hello python'
# # key='A'
# #
# # # encrypted_text=""
# # for letter in my_test:
# #      letter_code=ord(letter)
# #      encrypted_letter=chr(letter_code^ord(key))
# #      encrypted_text+=encrypted_letter
# # print(encrypted_text)
# #
# # dencrypted_text=""
# # for letter in encrypted_text:
# #     letter_code=ord(letter)
# #     encrypted_letter=chr(letter_code^ord(key))
# #     dencrypted_text+=encrypted_letter
# # print(dencrypted_text)
# #
# # #pb 6
# # #var1
# #
# # text = input("Introduceti un cuvant (fara majuscule): ")
# # contor = 0
# # for letter in text:
# #     if letter == text[0]:
# #         contor = contor + 1
# # print("r apare de:", contor, "ori.")
# #
# # #var2
# # text = input("Introduceti un cuvant (fara majuscule): ")
# # contor = 0
# # for letter in text:
# #     if letter == text[0]:
# #         contor = contor + 1
# # print("r apare de:", contor, "ori.")
#
# # #pb5
# #var1
# # my_list = ["Masa", 5, "Scaun", 4.5, [5,6,7], 8]
# # for i in my_list:
# #     print("Tipul obiectului", i, "este", type(i))
#
# # #var2
# # obiecte = ['Masa', 5, 'Scaun', 4.5, [5,6,7], 8]
# # for i in obiecte :
# #     print(f"Tipul obiectului {i} este:", type(i).__name__)
#
#
# #pb7
# lista=input("introduceti taskurile")
# lista_taskuri=lista.split(",")
# print(lista_taskuri)
# for task in lista_taskuri.copy():
#     lista_taskuri.count(task)
#     print(f"taskul: {task} se regaseste de  {lista_taskuri.count(task)}")
#     if lista_taskuri.count(task) >1:
#         lista_taskuri.remove(task)
# print(lista_taskuri)
