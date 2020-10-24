# OBJECT ORIENTED PROGRAMMING
# DEFINING CLASSES FOR ANIMALS
class animals:
   def __init__(self, eyes, legs, tail, covering):
      self.eyes=eyes
      self.legs=legs
      self.tail=tail
      self.covering=covering
   def info(self):
      print("It have %s eyes & %s legs also %s as a protective covering" %(self.eyes,self.legs,self.covering))
      print("Is this animal have a tail? ans is %s"%(self.tail))


class wild(animals):
   print("This is an animal who is Independent on human for their survival ")
   def place(self):
     print("Jungle")

class carnivores(wild):
   def food(self):
     print("Meat")

class lion(carnivores):
   def special(self):
     print("King of jungle")
     print("Symbols of strength & courage")
   def sound(self):
     print("Roar")
   def colour(self):
     print("mostly Orange-Brown")
    
class tiger(carnivores):
   def special(self):
     print("Largest cat species in the world")
     print("National animal of India")
   def sound(self):
     print("Roar")
   def colour(self):
     print("mostly Orange")
 
class polarbeers(carnivores):
   def special(self):
     print("Largest species of Bear")
     print("Marine animal")
   def sound(self):
     print("Can't get it")
   def colour(self):
     print("White")
 

class harbivores(wild):
   def food(self):
     print("Food from plant source")

class deer(harbivores):
   def special(self):
     print("Only animals that have antlers")
     print("Fastest growing living tissue on earth")
   def sound(self):
     print("Dummyvalue")
   def colour(self):
     print("mostly varies between Red & Brown")

class rabbit(harbivores):
   def special(self):
     print("Long ear, can listen longway sound")
     print("Happy rabbits jump in air & twist and spin arround when they are happy")
   def sound(self):
     print("Squeak")
   def colour(self):
     print("mostly White")

class koala(harbivores):
   def special(self):
     print("Arboreal animals which have special sound producing organs")
     print("Excellent sence of hearing")
   def sound(self):
     print("snarls")
   def colour(self):
     print("mostly Gray-Brown")

    
class omnivores(animals):
   def food(self):
     print("Variety of food of both plant and animal origin")

class rat(omnivores):
   def special(self):
     print("Nocturnal and live underground")
     print("Super strong teeth never stop growing")
   def sound(self):
     print("chewing")
   def colour(self):
     print("mostly Brown")


class domestic(animals):
   print("This is an animal who is Dependent on human for their survival")
   def place(self):
     print("Regions where human communities are located")
   def food(self):
     print("Varies from animal to animal")

class goat(domestic):
   def special(self):
     print("Provides milk")
     print("Independent, tolerant of intraction")
   def sound(self):
     print("maa")
   def colour(self):
     print("Varies from Black, White, Brown")
 
class horse(domestic):
   def special(self):
     print("Can display broad range of emotions")
     print("one of most fast running animal")
   def sound(self):
     print("whinny")
   def colour(self):
     print("mostly Brown & Black")


class bird(animals):
   def feature(self):
     print("Can Fly")
   def food(self):
     print("Worms, Insects, seeds")

class cuckoo(bird):
   def special(self):
     print("Known as Brood Parasites")
     print("Lay eggs in other birds nest")
   def sound(self):
     print("ka-ka-kaw")
   def colour(self):
     print("mostly Greyish")  


a=animals(2,4,'no','skin') # a is an object belonging to class animal
print(a.covering)
print(a.legs)

rocky=tiger(2,4,'yes','hair') # rocky is an objest belonging to class tiger
rocky.special()
rocky.colour()
rocky.food() #inherited method from class carnivores
rocky.place() #inherited method from class wild
rocky.info()  #inherited from super class animal

roha=deer(2,4,'yes but small', 'skin') #roha is an object belonging to class deer
roha.sound()
roha.info() 
roha.place() #inherited method from class wild
roha.food() #inherited methof from class harbivores

raja=horse(2,4,'yes a long one', 'skin')
raja.info()
raja.place() #inherited from class domestic
raja.special()

rani=cuckoo(2,2,'no','feathers')
rani.special()
rani.info()
rani.feature() #inherited from class bird
