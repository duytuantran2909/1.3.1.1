def kiemtra_nuocsoi(nhiet_do):
    if nhiet_do < 50:
        return "Nước lạnh"
    elif nhiet_do < 100:
        return "Nước chưa sôi"
    else:
        return "Nước đã sôi"
print(kiemtra_nuocsoi(30))   # in ra :nước lạnh
print(kiemtra_nuocsoi(70))   # in ra: nước chưa sôi
print(kiemtra_nuocsoi(100))  # in ra: nước đã sôi
print(kiemtra_nuocsoi(-10))  # in ra:nước lạnh vì -10 < 50 nên điều kiện đầu đúng hàm sẽ bỏ qua các điều kiện tiếp theo và nhận giá trị "nước lạnh"