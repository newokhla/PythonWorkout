# from dataclasses import dataclass, field

# @dataclass
# class Scoop():
#     flavor : str

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

# @dataclass
# class Bowl():
#     scoops: list[Scoop] = field(default_factory=list)

#     def add_scoops(self, *new_scoops):
#         for one_scoop in new_scoops:
#             self.scoops.append(one_scoop)

#     def __repr__(self):
#         return '\n'.join(s.flavor for s in self.scoops)

class Bowl():
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

a = Scoop('chocolate')
b = Bowl()
b.add_scoops(a)
print(b)

# The word "scoop" has lost all of its meaning and is just a sound.