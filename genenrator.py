def countdown(n):
    print("starting countdown...")
    while n > 0:
        n -= 1
    print("Done!")

gen = countdown(3)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# list comprehension
[i*i for i in range(1000)]

# generator expression
(i*i for i in range(1000))

# pasing generator 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = sum(x * x for x in numbers)
maximum = max(x for x in numbers if x % 2 == 0)
filtered = list(x for x in numbers if x > 5)

print(total)
print(maximum)
print(filtered)

# nested generator expression
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = (num for row in matrix for num in row)

print(list(flat))

# chaning generator into pipelines
def file_loading(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_error(lines):
   for line in lines:
       if "Error" in line:
           yield line

def parse_messages(lines):
    for line in lines:
        part = line.split('-')
        if len(part) >= 2:
            yield [-1] 

def uppercase(messages):
    for message in messages:
        yield message.upper()


csv = "example.csv"
main_csv = file_loading(csv)
f_error = filter_error(main_csv)
messages = parse_messages(f_error)