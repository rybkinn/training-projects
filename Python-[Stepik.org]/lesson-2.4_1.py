genome = input().upper()
a = len(genome)
b = genome.count('G')
d = genome.count('C')
e = b + d
f = float((e / a) * 100)
print(f)
