class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass
        return dict.__getitem__(self, key)

fd = FlexibleDict()
print(fd)
fd['a'] = 100
print(fd)
fd[5] = 500
print(fd)
fd[1] = 1000
print(fd)
fd['1'] = 100
print(fd[1])