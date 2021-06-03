passwordFile = open("pass.txt")
secretPassword = passwordFile.read()
for p in range(3):
    typePassword = input("Enter password:\n")
    if typePassword == secretPassword:
        print("Access granted:")
        break
    else:
        print("Access Denied!")
else:
    print("No more attemps")

