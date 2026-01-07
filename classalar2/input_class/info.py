class Shaxs:
    def __init__(self):
        self.ism=input("Ismingizni kirting-> ")
        self.familya=input("Familyangizni kirting-> ")
        self.t_yil=int(input("Tug'ilgan yilginzini kirting-> "))
        self.pasport=input("Passport seryasi raqamini kirting-> ")
    def get_info(self):
        "Sahxs haqida malumot beruvchi metod"
        info=f'Ismi familyasi {self.ism} {self.familya}'
        info+=f'  tugilgan yili {self.t_yil}  pasport sriyasi {self.pasport}'
        return info
    
    def get_age(self):
        self.j_yil=int(input("joriy yilni kirting->"))
        return self.j_yil-self.t_yil



class Talaba(Shaxs):
    talaba_bosqichi = 0   

    def __init__(self):
        super().__init__()
        self.id_raqam = input("ID raqamingizni kiriting -> ")

        Talaba.talaba_bosqichi += 1
        self.bosqich = Talaba.talaba_bosqichi

    def get_bosqich(self):
        return self.bosqich

    def get_id(self):
        return self.id_raqam
    

    def get_info(self):
        return f"{super().get_info() } uning id raqami {self.id_raqam}"
    


class Manzil(Talaba):
    def __init__(self):
        super().__init__()

        self.uy=int(input("Uy raqamini kirting-> "))
        self.kucha=input("Kuchani kirting-> ")
        self.tuman=input("Tumani kirting-> ")
        self.viloyat=input("Viloyatini kiritng-> ")
    
    def get_manzil(self):
        return f"{self.viloyat} viloyat {self.tuman} tuman {self.kucha } kucha {self.uy}-uy"
    
    def get_info(self):
        return super().get_info()

    
        

