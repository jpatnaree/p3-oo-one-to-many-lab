#Owner --< Pet # Pet belongs to owner
# sst pet is tracking the owner its belongs to

class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type #_private property meant to let others developer knows not to change it
    
    @pet_type.setter
    def pet_type(self, new_pet_type):
        if new_pet_type not in Pet.PET_TYPES:
            raise Exception(f'{new_pet_type} not in pet type')
        else:
            self._pet_type = new_pet_type
            

parakeet = Pet("Peter", "bird", "Annie")
print(parakeet)


class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [ p for p in Pet.all if p.owner == self ]
    
    def add_pet(self, new_pet):
        if isinstance(new_pet, Pet):
            new_pet.owner = self
        else:
            raise Exception('NOOOOOOOO!!!!!!')
        

    def get_sorted_pets(self):
        my_pet = self.pets() #Get all pets belong to self owner
        sorted_pet =  sorted(my_pet, key= lambda each_pet: each_pet.name.lower()) #sorted(list, key, reverse of needed)
        #sorted_pet =  sorted(my_pet, key= lambda each_pet: each_pet.name[0]) this one works to sort by first letter of each_pet but may cause some problem if some pets have same first letter name
        return sorted_pet
        