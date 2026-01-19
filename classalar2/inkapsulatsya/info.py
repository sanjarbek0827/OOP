"""from uuid import uuid4
class Avto:
    
    def __init__(self,make,model,rang,yil,narh,km=0):
       
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
    
    def get_km(self):
        return self.__km
    

    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        
        if km>=0:
            self.__km+=km
        
        else:
            return "Moshinani km kamytirib bulmaydi "
        
    def add_narh(self,narh):
        if narh>self.narh:
            self.narh=narh
            return "Bu narhdan yuqori narx tugri kelmaydi"
        else:
            return "Bu nardagi Avtombile turi mavjud emas"

    

    def __str__(self):
        return (f'Moshinanning zavodi {self.make} moddeli {self.model} rangi {self.rang} yili {self.yil}  narhi {self.narh} ga teng'
    
        f'\n Moshinanig Id raqami {self.__id} va yurgan masofasi {self.__km}')
"""




from uuid import uuid4
class Avto:
    num_avto=0
    def __init__(self,make,model,rang,yil,narh,km=0):
       
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.num_avto+=1
        
    
    def get_km(self):
        return self.__km
    

    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        
        if km>=0:
            self.__km+=km
        
        else:
            return "Moshinani km kamytirib bulmaydi "
        
    def add_narh(self,narh):
        if narh>self.narh:
            self.narh=narh
            return "Bu narhdan yuqori narx tugri kelmaydi"
        else:
            return "Bu nardagi Avtombile turi mavjud emas"

    

    def __str__(self):
        return (f'Moshinanning zavodi {self.make} moddeli {self.model} rangi {self.rang} yili {self.yil}  narhi {self.narh} ga teng'
    
        f'\n Moshinanig Id raqami {self.__id} va yurgan masofasi {self.__km}')
