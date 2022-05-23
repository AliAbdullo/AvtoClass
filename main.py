class Avto:
  """Avto nomli class """
  def __init__(self,make, model, rang, korobka, narx):
    self.make=make
    self.model=model
    self.rang=rang
    self.korobka=korobka
    self.narx=narx
    self.km=0

  def get_make(self):
    """Avtoning kompaniyasini qaytaradi"""
    return self.make

  def get_model(self):
    """Avto modelini qaytaradi"""
    return self.model

  def get_rang(self):
    """Avtoning rangini qaytaradi"""
    return self.rang

  def get_karobka(self):
    """Avtoning karobkasini qaytaradi"""
    return self.korobka

  def update_km(self,yurgani):
    """Kilometr saqlaydi"""
    self.km+=yurgani

  def get_info(self):
    """Avto xaqida malumotlarni qaytaradi"""
    return f"{self.rang} {self.model} narxi: {self.narx}, korobkasi:{self.korobka}, kilometri:{self.km}"
    
    
#Avtosalon nomli class:
class Avtosalon:
  def __init__(self,nomi, manzili):
    self.nomi=nomi
    self.manzili=manzili
    self.avtomobillar=[]

  def get_nomi(self):
    """Avtosalon nomini qaytaradi"""
    return self.nomi

  def get_manzili(self):
    """Avtosalon manzilini qaytaradi"""
    return self.manzili

  def add_avtollar(self,avto):
    """Sotuvdagi avtollar qo'shish"""
    self.avtomobillar+=[avto]

  def get_salon_info(self):
    """Avtosalon xaqida malumotlar"""
    return f"{self.manzili}dagi {self.nomi}li avtosalonda {self.avtomobillar} bor!"



mashina1 = Avto("GM","Malubu", "Qora","avtomat",20000)
print(mashina1.get_info())