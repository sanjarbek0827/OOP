from info import Avto

avto1=Avto(make="GM",model="Malubu",rang="Qora",narh=40000,yil=2025)
avto2 = Avto("GM","Malibu","Qora",2020,40000)
avto3 = Avto("GM","Lacetti","Oq",2020,20000)
"""# bu birnci usuli  yani abyetni uzi orqali murojat qilsih
print(avto1.num_avto)
"""
#  ikkinchi usuli classni uzi bilan murojat qilsih
print(Avto.num_avto)

print(avto1)
print(avto2)
print(avto3)