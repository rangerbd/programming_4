

class Atom:
    def __init__(self,symbol,atomic_number, n_atom):
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.number_of_neurons = n_atom

    def isotope(self,new_neutrons):
        self.number_of_neurons = new_neutrons

    def __repr__(self):
        return f"Symbol = {self.symbol} , atomic_number = {self.atomic_number} and Number of atoms = {self.number_of_neurons} number of replaced neurons = {self.number_of_neurons}"

    def proton_number(n):
        proton_number = n
        return f"proton_number = {proton_number}"

    def mass_number(proton_number,neutrons):
        sum = proton_number + neutrons
        return f"The Atoms mass number = {sum}"

number_of_proton = Atom.proton_number(100)
print(number_of_proton)
sum_of_mass = Atom.mass_number(100,2)
print(sum_of_mass) 

protium = Atom('H',1,0)
print(protium)

protium.isotope(7)
print(protium)






