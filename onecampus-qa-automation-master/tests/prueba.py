import glob
path = "hola.txt"
d = {}
files = glob.glob(path)
for file in files:
    with open(file) as fileobj:
        for line in fileobj:
            (key, value) = line.split("=")
            d[key] = value

print(d['Monday'])