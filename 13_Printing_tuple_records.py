import operator

people = [('Donald', 'Trump', 7.85),
        ('Vladimir', 'Putin', 3.626), 
        ('Jinping', 'Xi', 10.603)]

def format_sort_records(tuple_list):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(tuple_list, key=operator.itemgetter(1,0)):
        output.append(template.format(*person))
    return output

# print('\n'.join(format_sort_records(people)))

names = ['abc', 'b', 'ab']

print(sorted(names))