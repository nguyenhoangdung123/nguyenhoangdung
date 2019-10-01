email = input("Nhap email: ")
if ("@" or ".") not in email:
    while True:
        print("email dang sai !!!!!")
        returnEmail = input("Nhap lai email")
        if ("@" or ".") in email:
            print("Tao tai khoan")
            break

if ("@" or ".") in email:
    print("Tao thanh cong")