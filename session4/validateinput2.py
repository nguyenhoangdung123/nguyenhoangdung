while True:
txt = input("nhap mat khau? ")
print(txt)
if txt.isalpha:
    print("nhap lai mat khau")
elif len(txt)<=8:
    print("nhap lai mat khau")
else:
    print("nhap mat khau thanh cong")
    break