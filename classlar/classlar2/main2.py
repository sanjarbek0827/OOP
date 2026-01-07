from info import Admin, Foydalanuvchi

# foydalanuvchi1=Admin("Ali","Valiyev",1985,"AB1234567","A001")
# print(f'{foydalanuvchi1.get_info()} va u {foydalanuvchi1.ban_user(foydalanuvchi1)}')
f1 = Foydalanuvchi("Olim", "Toshpulatov", 2001, "AD7654321", "olim001")

admin = Admin("Ali", "Valiyev", 1985, "AB1234567", "A001", "SuperAdmin")
print(f1.get_info())
print(admin.ban_user(f1))
