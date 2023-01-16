class Hewan:
  def suara(self):
    pass

class Anjing(Hewan):
  def suara(self):
    print("Guk guk")

class Kucing(Hewan):
  def suara(self):
    print("Meong meong")

hewan1 = Anjing()
hewan2 = Kucing()

hewan1.suara()  # Mencetak "Guk guk"
hewan2.suara()  # Mencetak "Meong meong"
