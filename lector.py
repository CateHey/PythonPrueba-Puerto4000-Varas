import urllib, json
#nombre del archivo

data = []
with open("palabras.txt") as f:
        for line in f:
                line = line.split()
                data.append({"nombre": line[0]})

data = {"datos": data}

out_file = open("listacompleta.json", "w")
json.dump(data, out_file, indent = 1)
out_file.close()