while True:
txt = input("nhap ten cua ban? ")
print(txt)
if txt.isalpha():
    print("nhap ten thanh cong ")
    break
else:
    print("nhap ten khong thanh cong")