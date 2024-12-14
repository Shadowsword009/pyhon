password = input()
special_char = ["@","!","&","^","%","#"]
val = True
if len(password) < 8:
    val = False
if len(password) > 20:
    val = False
if not any(char in special_char for char in password):
    val = False
if not any(char.isupper() for char in password):
    val = False
if not any(char.islower() for char in password):
    val = False
if not any(char.isdigit() for char in password):
    val = False
if val == True:
    print("password is accepted")
else:
    print("password not accepted")






