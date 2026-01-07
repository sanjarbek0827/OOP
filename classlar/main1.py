"""class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil



    def get_info(self,joriy_yil):
        return f"{self.ism} {self.familiya}, {joriy_yil-self.tyil}-yoshda"
    # def get_name(self):
    #     return f'talabaning ismi: {self.ism}'
    
    # def get_age(self, joriy_yil):
    #     return joriy_yil-self.tyil
    # def get_info(self):
    #     return f"{self.ism} {self.familiya}, {self.tyil}-yilda tug'ilgan"
talaba1 = Talaba("Ali", "Valiyev", 2000)
talaba2 = Talaba("Sara", "Karimova", 1999)
talaba3 = Talaba("Olim", "Toshpulatov", 2001)
print(talaba1.get_info(2024))
print(talaba2.get_info(2024))
print(talaba3.get_info(2024))
"""

# # AMALIYOT
# - Web sahifangiz uchun foydalanuvchi (`user`) klassini tuzing. Klassning xususiyatlari sifatida odatda 
# ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

# - Klassga bir nechta metodlar qo'shing, jumladan `get_info()` metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni
#  chiroyli qilib chiqarsin (masalan: `"Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com`).

# - Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.

"""

class User:
   
    def __init__(self):
        self.ism = input("Ismingizni kiriting: ")
        self.familiya = input("Familiyangizni kiriting: ")
        self.foydalanuvchi_ismi = input("Foydalanuvchi ismingizni kiriting: ")
        self.email = input("Email manzilingizni kiriting: ")

    def __str__(self):
        return f"'Foydalanuvchi: {self.foydalanuvchi_ismi}, ismi: {self.ism} {self.familiya}, email: {self.email}"
users=User()
print(users)

"""

# Foydalanuvchini lugat shaklida saqlash
"""
malumotlar={}
class User:

    def foydalanuchi_kirit(self):
        while True:
            self.id=len(malumotlar)+1
            self.ism = input("Ismingizni kiriting: ")
            self.familiya = input("Familiyangizni kiriting: ")
            self.foydalanuvchi_ismi = input("Foydalanuvchi ismingizni kiriting: ")
            self.email = input("Email manzilingizni kiriting: ")
            malumotlar[self.id] = self.__dict__
            

    
            javob = input("Yana foydalanuvchi qo'shasizmi? (ha/yo'q): ")
            if javob.lower() != 'ha':
                break
    
    def __init__(self):
        self.foydalanuchi_kirit()


users=User()
print(malumotlar)
  """
      
# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing.
# Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
"""
class Avto:
    def __init__(self,kilometr=0):
        self.kilometr=kilometr
        self.model = input("Avtomobil modelini kiriting: ")
        self.rang = input("Avtomobil rangini kiriting: ")
        self.korobka = input("Avtomobil korobkasini kiriting: ")
        self.narh = input("Avtomobil narhini kiriting: ")

    def update_km(self):
        yangi_km = int(input("Yangi kilometrni kiriting: "))
        self.kilometr += int(yangi_km)
        return self.kilometr
    
    def __str__(self):
        return f"Avtomobil modeli: {self.model}, rangi: {self.rang}, korobkasi: {self.korobka}, narhi: {self.narh}, yurgan kilometri: {self.kilometr}"
avto1=Avto()
avto1.update_km()
print(avto1)

"""



"""

avto=[]

class Avto:
    def __init__(self):
        self.model = input("Avtomobil modelini kiriting: ")
        self.rang = input("Avtomobil rangini kiriting: ")
        self.korobka = input("Avtomobil korobkasini kiriting: ")
        self.narh = input("Avtomobil narhini kiriting: ")
      
    
    def get_append(self):
        avto.append(self)
        return avto 
    
    def __repr__(self):
        return f'Avtombil modeli: {self.model}, rangi: {self.rang}, korobkasi: {self.korobka}, narhi: {self.narh}'
    
    def get_info(self):
         for x in avto:
            return x
while True:
         avto1=Avto()
         avto1.get_append()
         avto1.get_info()
         
         javob = input("Yana avtomobil qo'shasizmi? (ha/yo'q): ")
         if javob.lower() != 'ha':
              break

# print(f'{avto }')
karoka1=[]
for x in avto:
     if x.korobka =='avtomat':
            karoka1.append(x)
print(f'Avtomat korobkali avtomobillar: {karoka1}')

"""

# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing

"""

class Avtosalon:
    def __init__(self):
        self.salon_nomi = input("Avtosalon nomini kiriting: ")
        self.manzil = input("Avtosalon manzilini kiriting: ")
        self.sotuvdagi_avtomobillar = []

    def yangi_avto_qoshish(self):
        while True:
            model = input("Avtomobil modelini kiriting: ")
            rang = input("Avtomobil rangini kiriting: ")
            korobka = input("Avtomobil korobkasini kiriting: ")
            narh = input("Avtomobil narhini kiriting: ")
            avto = {
                'model': model,
                'rang': rang,
                'korobka': korobka,
                'narh': narh
            }
            self.sotuvdagi_avtomobillar.append(avto)
            javob = input("Yana avtomobil qo'shasizmi? (ha/yo'q): ")
            if javob.lower() != 'ha':
                break

    def __str__(self):
        return f"Avtosalon nomi: {self.salon_nomi}, manzili: {self.manzil}, sotuvdagi avtomobillar: {self.sotuvdagi_avtomobillar}"
avtosalon1 = Avtosalon()
avtosalon1.yangi_avto_qoshish()
print(avtosalon1)

"""
    


