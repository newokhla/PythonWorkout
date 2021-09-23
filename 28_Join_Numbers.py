def join_numbers(integer):
    return ','.join(str(i) for i in range(integer))

print(join_numbers(15))

# With list comprehension
print(sum(x*x for x in range(10) if x%2 == 0))

# Without list comprehension
total = 0
for i in range(0,10):
    if i % 2 == 0:
        total += i*i
print(total)