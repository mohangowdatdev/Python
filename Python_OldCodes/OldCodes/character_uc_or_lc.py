ch=input("Enter the Character: ")[0]
if ch>='a' and ch<='z':
    print("Lower case")
else:
    if ch >= 'A' and ch <= 'Z':
        print("Upper case")
    else:
        if ch>='0' and ch<='9':
            print("Number")
        else:
            print("Its a special character")
