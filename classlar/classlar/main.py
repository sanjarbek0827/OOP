from shaxs import Talaba, Manzil,Fan,Shaxs
natija=Shaxs('Ali','Valiyev',2000,'AB1234567')
print(natija.get_info(), (f" va u {natija.get_age(2024)}  yoshda"))
# natija1=Talaba('Sara','Karimova',1999,'AC9876543','T123456')
# print(natija1.get_info(), (f" va u {natija1.get_age(2024)}  yoshda, bosqichi- {natija1.get_bosqich()}"))
# natija2=Talaba('Olim','Toshpulatov',2001,'AD7654321','T654321')
# print(natija2.get_info(), (f" va u {natija2.get_age(2024)}  yoshda, bosqichi- {natija2.get_bosqich()}"))
# natija1=Talaba('Lola','Husanova',2002,'AE3456789','T789012')
# print(natija1.get_info(), (f" va u {natija1.get_age(2024)}  yoshda, bosqichi- {natija1.get_bosqich()}"))
# natija=Talaba('Jasur','Bektemirov',2000,'AF2345678','T890123')
# print(natija.get_info(), (f" va u {natija.get_age(2024)}  yoshda, bosqichi- {natija.get_bosqich()}"))

# manzil1=Manzil("Bunyodkor",15,"Toshkent","Toshkent")
# talaba1=Talaba("Anvar","Saidov",2003,"AG4567890","T112233",manzil1)
# print(f'{talaba1.get_info()} va u {talaba1.get_age(2024)} yoshda, bosqichi- {talaba1.get_bosqich()}, manzili: {talaba1.manzil.get_manzil()}')
# manzil1=Manzil("Navoiy",20,"Samarqand","Samarqand")
# talaba1=Talaba("Dilshod","Jalilov",2002,"AH5678901","T223344",manzil1)
# print(f'{talaba1.get_info()} va u {talaba1.get_age(2024)} yoshda, bosqichi- {talaba1.get_bosqich()}, manzili: {talaba1.manzil.get_manzil()}')


# Fanlar
matematika = Fan("Matematika", 120)
fizika = Fan("Fizika", 90)

# Talaba
manzi=Manzil("Bunyodkor",15,"Toshkent","Toshkent")
t1 = Talaba("Ali", "Valiyev", 2000, "AB1234567", "ID001", manzi)

t1.fanga_yozil(matematika)
t1.fanga_yozil(fizika)

print([fan.get_info() for fan in t1.fanlar])

print(t1.remove_fan(matematika))
print(t1.remove_fan(matematika))


