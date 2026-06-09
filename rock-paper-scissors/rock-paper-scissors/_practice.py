#PRACTICE CLASSES


class Dog:
    def __init__(self, name, breed = ""):
        self.name = name
        self.breed = breed
        

    
    def __str__(self):
        return(f'{self.name} {self.breed}')
    
    def __repr__(self):
        return(f'{self.name} {self.breed}')
    


dog_collection = []

def collect_dogs():
    while True:
        dog_name = input("Dog Name: ")
        dog_breed = input("Dog Breed: ")
        return dog_name, dog_breed





dog_names = []
dog_names.append(Dog("Brian", "Frenchie"))
print(dog_names)

find_keys = dog_names[0].__dict__.keys()
print(find_keys)