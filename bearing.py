class Bearing:

    L = []

    def __init__(self, dynamic_load_capacity, id_bearing):
        self.C = dynamic_load_capacity
        self.id = id_bearing

    def calculate(self, force):
        self.L.append(self.C / force)

    def print_result(self):
        print(f" The durability of bearing is equal to {self.L}.\n")
        if {self.L} >= {self.allowed_durability}:
            print(f"{self.L} is too high, the {self.name} bearing is broken.\n")
        else:
            print(f"{self.L} is optimal, the {self.name} bearing is able to work.\n")
