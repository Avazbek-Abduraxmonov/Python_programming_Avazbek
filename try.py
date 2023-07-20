# try:
#     num = int(input("Butun son kiriting: "))
#     print("Siz shu yoshga kirdingiz: ", num)
# except ValueError:
#     print("Notog'ri kiritildi. Iltimos tog'ri butun son kiriting: ")
# finally:
#     print("Dasturimiz tugadi")


# my_list = [1,2,3,4,5]

# try:
#     index = int(input("index ni kiriting: "))
#     result = my_list[index]
#     print("Index dagi qiymat: ", result)
# except IndexError:
#     print("Index ni tog'ri kiriting")

# except ValueError:
#     print("Index uchun butun son kiriting")

try:
    number = int(input("Son kiriting: "))
    print("Siz shu yoshga kirdingiz: ",number)
except KeyboardInterrupt:
    print("Kirish bekor qilindi")
except ValueError:
    print("Notog'ri kiritdingiz. Iltimos tog'ri raqam kiriting")
finally:
    print("Dastur tugadi")

