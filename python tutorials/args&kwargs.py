# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#           * unpacking operator 
#           1. positional 2. default 3. keyword 4. ARBITRARY


# def add(*args):
#     print(type(args))

# add(1, 2, 3)
################################################################################

# def add(*args):
#     total = 0
#    for arg in args:
#         total += arg
#     return total    

# print(add(1, 2, 3, 4))

#################################################################################

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Tarang", "Dhiraj", "Shah")

#################################################################################

# *kwargs

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_address(street="123 Fake st.",
#               apt="100", 
#               city="Detroit", 
#               state="MI", 
#               zip=54321)

##################################################################################
# Exc 1

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()

#     if "apt" in kwargs:   
#         print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     elif "pobox" in kwargs:
#         print(f"{kwargs.get('street')}")
#         print(f"{kwargs.get('pobox')}")
#     else:
#          print(f"{kwargs.get('street')}")   
#     print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")
  

# shipping_label("Dr.", "Tarang", "Shah", "III", 
#                street="123 Fake St.",
#                pobox="PO box #1001",  
#                city="Detroit", 
#                state="MI", 
#                zip="54321")
