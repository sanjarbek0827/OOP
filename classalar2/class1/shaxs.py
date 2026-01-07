class Shaxs:
    def __init__(self,ism ,familya,t_yil,pasport):
        self.ism=ism
        self.familya=familya
        self.t_yil=t_yil
        self.pasport=pasport
    def get_info(self):
        """Shaxs haqida malumot beruvchi metod  """
        info=f"Ismi familyasi {self.ism} {self.familya} "
        info+=f" tug'ilgan yili {self.t_yil}-yil , pasport seriyasi {self.pasport}"
        return info
    
    def get_age(self,j_yil):
        self.j_yil=j_yil
        return f"{j_yil-self.t_yil}"
    

class Manzil:
    def __init__(self,uy,kucha, tuman, viloyat):
        self.uy=uy 
        self.kucha=kucha
        self.tuman=tuman
        self.viloyat=viloyat
    
    def get_manzil(self):
        manzil=f"{self.viloyat} viloyati {self.tuman} tumani  {self.kucha} ko'chasi {self.uy}-uyda yashaydi"
        return manzil

    
        
    
class Talaba(Shaxs):
    "Talbaning  klassi"
    talaba_bosqichi = 0
    def __init__(self, ism, familya, t_yil, pasport, id_raqam,manzil):
        " Sahxsdan olingan voris xususiyatlar "
        super().__init__(ism, familya, t_yil, pasport)
        self.id_raqam=id_raqam
        self.bosqich=1
        self.manzil=manzil
        Talaba.talaba_bosqichi += 1
        self.bosqich = Talaba.talaba_bosqichi
    
    def get_raqam(self):
        return self.id_raqam
    
    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info=super().get_info()
        info+=f", id raqami: {self.id_raqam} yashash mazili {self.manzil.get_manzil()}"
        return info


