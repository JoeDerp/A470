# Part 1
x = 5

# Part 2
l = []
l = [num+1 for num in range(5)]

# Part 3
l = [num*x for num in l]

# Part 4
D = {
    123:"{",
    61:"=",
    33:"!",
    50:"2",
    75:"K"
}
# Part 5
D = dict(sorted(D.items()))
text = "The decimal number, {}, is the ASCII code for the character '{}'"
for key in D:
    print(text.format(key,D[key]))