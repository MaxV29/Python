transl = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
f = []
with open("my_file4.txt", "r") as f_obj:
    for i in f_obj:
        i = i.split(" ", 1)
        f.append(transl[i[0]] + "  " + i[1])
    print(f)

with open("my_file4.txt", "w") as f_obj_2:
    f_obj_2.writelines(f)