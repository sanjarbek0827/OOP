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



class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, t_yil, pasport_raqami, username):
        super().__init__(ism, familiya, t_yil, pasport_raqami)

        self.username=username
    
    def get_info(self):
        return f"Foydalanuvchi: {self.username}, {super().get_info()} "
    


class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, t_yil, pasport_raqami, username, admin_haqida):
        super().__init__(ism, familiya, t_yil, pasport_raqami, username)

        self.admin_haqida=admin_haqida
        


    def get_info(self):
        return f'Admin: {self.username} ({self.admin_haqida}), {super().get_info()} '
    
    def ban_user(self, foydalanuvchi):
        return f'Foydalanuvchi {foydalanuvchi.username} ban qilindi!'
    