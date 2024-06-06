class Dequeu:   
   def __init__(self):
      self.items = ["Motor Supra"]     
   def isempty(self):
      return self.items == 0

   def addRear(self, item):
      self.items.insert(0,item)
      
   def addFront(self, item):
      self.items.append(item)

   def removeFront(self):
    self.items.pop(0)
      
   def removeRear(self):
      self.items.pop()
      
   def size(self):
      return len(self.items)
      
   def tampilaknDequeu(self):
      if self.isempty():
         print("Parkiran sedang kosong")
      else:
         print("Tampilkan isi parkir: ",self.items)

  
#Membuat objek 
Parkir = Dequeu()
print("---- SIMULASI ANTRIAN PARKIR ----")

#Operasi Dequeu
Parkir.addRear("Motor 1")
Parkir.addRear("Motor 2")
Parkir.addFront("Motor 3")
Parkir.addFront("Motor 4")

Parkir.tampilaknDequeu()

Parkir.removeFront()#Menghapus dari depan
print("Menghapus isi parkir dari depan :", Parkir.size())

Parkir.removeRear()#Menghapus dari belakang
print("menghapus isi parkir dari belakang :", Parkir.size())