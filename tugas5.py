import random

class Father:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Mother:
    def __init__(self, blood_types):
        self.blood_types = blood_types

class Child:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        father_allele = random.choice(self.father.blood_types)
        mother_allele = random.choice(self.mother.blood_types)
        return father_allele + mother_allele

# Example usage
father_blood_types = input("Enter father's blood types (e.g., 'AO'): ")
mother_blood_types = input("Enter mother's blood types (e.g., 'BO'): ")

father = Father(father_blood_types)
mother = Mother(mother_blood_types)
child = Child(father, mother)

print(f"Child's blood type: {child.blood_type}")