import random
class Kartya:
  def __init__(self):
    mylist = ["ut", "mezo", "varos"]
    self.bal = random.choices(mylist, weights = [1, 1, 1], k = 1)
    self.fent = random.choices(mylist, weights = [1, 1, 1], k = 1)
    self.jobb = random.choices(mylist, weights = [1, 1, 1], k = 1)
    self.lent = random.choices(mylist, weights = [1, 1, 1], k = 1)

  def forgat(self):
    tmp=self.bal
    self.bal=self.fent
    self.fent=self.jobb
    self.jobb=self.lent
    self.lent=tmp

#jatekos kartyaja:
kartyalist=[]
k1 = Kartya()
print(k1.bal, k1.fent,k1.jobb,k1.lent)
k1.forgat()
print(k1.bal, k1.fent,k1.jobb,k1.lent)
