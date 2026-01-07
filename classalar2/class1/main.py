from colorama import Fore,Back
#  bu yerda  brinchi shaxs degan classni uzidan olin xususiyatlarni  uz ichiga olgan qismi
"""from shaxs import Shaxs
talaba=Shaxs("Hasan","Valiyev",  2001, "AC33234","MZ59815")
print(f"{talaba.get_info()} va u {talaba.get_age(2026)} yoshda")
"""


# Bu qismim esa  Talbaga classi shaxs clasdan olin xususiyatlari va bu  voris class xisoblanadu 

from shaxs import  Talaba,Manzil
manzil_talaba=Manzil(12,'Olmazor',"Bog'bon","Samarqand")
talaba=Talaba("Hasan","Valiyev",  2001, "AC33234","MZ59815",manzil_talaba)
print(f"{talaba.get_info()} va u {talaba.get_age(2026)} yoshda hamda u {talaba.get_bosqich()}-bosqich talbasi")


manzil1=Manzil("Bunyodkor",15,"Toshkent","Toshkent")
talaba=Talaba('Olim','Toshpulatov',2004,'AD7654321','T654321',manzil1)
print(f"{talaba.get_info()} va u {talaba.get_age(2026)} yoshda hamda u {talaba.get_bosqich()}-bosqich talbasi")


