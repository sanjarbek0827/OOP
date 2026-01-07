from info import Talaba,Shaxs,Manzil
from colorama import Fore,Back,Style

#  bu yerda  brinchi shaxs degan classni uzidan olin xususiyatlarni  uz ichiga olgan qismi
"""
talaba=Shaxs()
print(f"{talaba.get_info()} va siz {talaba.get_age()}  yoshdasiz ")
"""

# Bu qismim esa  Talaba classiga shaxs classdan olin xususiyatlari va bu  voris class xisoblanadu 
"""
talaba=Talaba()
print(Style.BRIGHT+Fore.GREEN+f"{talaba.get_info()} va siz {talaba.get_age()}  yoshdasiz {talaba.get_bosqich()}-bosqich talbasi"+Style.RESET_ALL
      )
"""
# Bu qismim esa  Manzil classiga Talaba classdan olin xususiyatlari va bu  voris class xisoblanadu 

talaba2=Manzil() 
print(Style.BRIGHT+Fore.YELLOW+f"{talaba2.get_info()} va siz {talaba2.get_age()}  yoshdasiz {talaba2.get_bosqich() }-bosqich talbasi\n Manzili {talaba2.get_manzil()}"+Style.RESET_ALL
      )
