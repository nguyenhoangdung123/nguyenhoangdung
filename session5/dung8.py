while True:
    email = input("nhap email:")
    taikhoan = input ("Nhap tai khoan:")
    matkhau = input ("nhap mat khau:")
    matkhau2 = input ("nhap lai mat khau:")
    if matkhau2 == matkhau:
        print("Nhap tai khoan thanh cong !")
        break 
    else:
        print("Nhap mat khau sai, vui long nhap lai tu dau")