email=input("emailni kiriting: ")
a=not email.startswith("@") and email.endswith(".com")
print(a)