while True:
txt = input("nhap mat khau? ")
print(txt)
if txt.isalpha():
    print("nhap lai mat khau")
else:
    print("nhap mat khau thanh cong")
    break