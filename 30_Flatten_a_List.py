l = [[1,2, [5,6]], [3,4]]

def flatten(a_list):
    return [j for i in a_list for j in i]

print(flatten(l))