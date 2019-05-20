f = set(open("primenumbers.txt").read().split("\n"))
f2 = set(open("happynumbers.txt").read().split("\n"))

print(f & f2)