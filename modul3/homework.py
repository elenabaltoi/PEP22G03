my_list = ["abc", 123, "1", 1]
for obiect in my_list:
    print("Tipul obiectului", obiect, "este", type(obiect))
for obiect in my_list.copy():
    my_list.count(obiect)
    print(f"Obiectul: {obiect} se regaseste de  {my_list.count(obiect)}")

