class Shaxs():
    def __init__(self,ism,familiya,t_yil,pasport_raqami):
        self.ism=ism
        self.familiya=familiya
        self.t_yil=t_yil
        self.pasport_raqami=pasport_raqami
    def get_info(self):
        info=f'{self.ism} {self.familiya}'
        info+=f', {self.t_yil} yilda tug\'ilgan, pasport raqami: {self.pasport_raqami}'
        return info
    def get_age(self,joriy_yil):
        return joriy_yil-self.t_yil
    

class Manzil():
    def __init__(self,kocha,uy,shahar,viloyat):
        self.kocha=kocha
        self.uy=uy
        self.shahar=shahar
        self.viloyat=viloyat
    def get_manzil(self):
        return f"{self.kocha} ko'chasi, {self.uy} - uy, {self.shahar} shahri, {self.viloyat} viloyati"
    
class Fan:
    def __init__(self, nomi, soat):
        self.nomi = nomi
        self.soat = soat

    def get_info(self):
        return f"{self.nomi} ({self.soat} soat)"







class Talaba(Shaxs):
    talaba_bosqichi = 0

    def __init__(self, ism, familiya, t_yil, pasport_raqami, id_raqami, manzil):
        super().__init__(ism, familiya, t_yil, pasport_raqami)

        self.id_raqami = id_raqami
        self.manzil = manzil
        self.fanlar = []   

        Talaba.talaba_bosqichi += 1
        self.bosqich = Talaba.talaba_bosqichi

    def get_bosqich(self):
        return self.bosqich

    def get_id(self):
        return self.id_raqami

    def get_info(self):
        info = super().get_info()
        info += f", id raqami: {self.id_raqami}, bosqichi: {self.bosqich}"
        return info

    def fanga_yozil(self, fan):
        if isinstance(fan, Fan):
            if fan not in self.fanlar:
                self.fanlar.append(fan)
            else:
                return "Siz bu fanga allaqachon yozilgansiz"
        else:
            return "Xatolik: Fan obyektini yuboring"

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            return f"{fan.nomi} fani o‘chirildi"
        else:
            return "Siz bu fanga yozilmagansiz"
