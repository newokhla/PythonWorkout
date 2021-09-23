class MyEnumerate():
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value

for index, letter in MyEnumerate('abc'):
    print(f'{index} : {letter}')

# mylist = [1, 2, 3]

# def list_iterator(a_list):
#     for item in a_list:
#         yield item

# for item1 in list_iterator(mylist):
#     print(item1)