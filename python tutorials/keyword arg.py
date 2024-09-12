# keyword arguments = An argument preceded by an identifier
#                     helps with readablity
#                     order of arguments dosen't matter

# Exc 1

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# hello("Hello", "Mr.", "Tarang", "Shah")
# hello("Hello", "Tarang", "Shah", "Mr.")
# hello("Hello", title="Mr.", first="Tarang", last="Shah")
# hello("Hello", first="Tarang", last="Shah", title="Mr.")
# hello(first="Tarang", last="Shah", title="Mr.", "Hello")
# hello("Hello", last="Tarang", first="Shah", title="Mr.")

#############################################################################

# Exc 2

# for x in range(1, 11):
#     print(x, end =" ")

# print("1", "2", "3", "4", "5", sep = "-")

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=91, area=413001, first=9322, last=257)

# print(phone_num)