count = input()

string = input()
arr = [int(x) for x in string.split(' ') if x != '']

for _ in range(2):
    for i in arr:
        print(i)