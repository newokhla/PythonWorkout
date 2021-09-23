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
    max_scoops = 3
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

class BigBowl(Bowl):
    max_scoops = 5

    # def add_scoops(self, *new_scoops):
    #     for one_scoop in new_scoops:
    #         if len(self.scoops) < BigBowl.max_scoops:
    #             self.scoops.append(one_scoop)


a1 = Scoop('chocolate1')
a2 = Scoop('chocolate2')
a3 = Scoop('chocolate3')
a4 = Scoop('chocolate4')
a5 = Scoop('chocolate5')
a6 = Scoop('chocolate6')

bb = BigBowl()
bb.add_scoops(a1, a2, a3, a4, a5, a6)
print(bb)
print(bb.max_scoops)

# The word "scoop" has lost all of its meaning and is just a sound.