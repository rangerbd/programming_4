

class atom:
    #1A
    def __init__(self,symbol, atomic_number, number_of_neutrons):
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.number_of_neutrons = number_of_neutrons

    def __repr__(self):
        return f"Symbol is = {self.symbol}, atomic number is = {self.atomic_number}, number of neutrons are = {self.number_of_neutrons}"
    
    #1B
    def proton_number(self):
        return self.atomic_number
    
    def mass_number(self):
        return self.atomic_number + self.number_of_neutrons
    
    #1C

    def isotope(self, n_neutron):
        self.number_of_neutrons = n_neutron 
        return self.number_of_neutrons


    #1D
    def equal(self,other):
        if self.atomic_number != other.atomic_number:
            raise ValueError("this is not comparable")
        return self.mass_number() == other.mass_number()
    def less_than(self,other):
        if self.atomic_number != other.atomic_number:
            raise ValueError("this is not comparable")
        return self.mass_number() < other.mass_number()
    
    def greater_than(self, other):
        if self.atomic_number != other.atomic_number:
            raise ValueError("this is not comparable")
        return self.mass_number() > other.mass_number()

protium = atom('H',6,2)
a = atom ('H',5,6)
b = atom('K',2,3)
print(protium)

print(f"proton number is {protium.proton_number()}  ")
print(f"mass_number is {protium.mass_number()}")
print(f"new assigned neutron number is {protium.isotope(5)}")

#debug
protium = atom('H', 1, 0)
deuterium = atom('H', 1, 1)
oxygen = atom('O', 8, 8)
tritium = atom('H', 1, 2)
oxygen.isotope(9)

assert tritium.number_of_neutrons == 2
assert tritium.mass_number() == 3
assert protium.less_than(deuterium)
assert deuterium.less_than(tritium) 
assert tritium.greater_than(protium)








