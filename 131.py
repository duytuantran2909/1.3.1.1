a = 3 > 5       # a mang giá trị false vì 3 không lớn hơn 5
b = 4 != 4      # b mang giá trị false vì 4 bằng 4 nên biểu thức sai

print("a and b =", a and b)   # false vì a và b đều mang giá trị false
print("a or b =", a or b)     # false vì không có cái nào đúng
print("a ^ b =", a ^ b)       # false vì cả 2 đều giống nhau (a và b đều mang giá trị false)
print("not a =", not a)       # true vì phủ định của false là true
#ví dụ 
x = 99
y = 5
z = 99

ket_qua = (x == z) and (y != z) or (x < y)
# (x == z) và (y != z) mang giá trị True nên vế 1 mang giá trị True
# (x<y) mang giá trị false nhưng vế trước mang giá trị True nên biến ket_qua mang giá trị True

print("Kết quả:", ket_qua)
