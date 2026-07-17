from PIL import Image

# INPUT
config = {}
file = open("config.txt", "r")
lines = file.readlines()
for line in lines:
    parameter, value = line.strip().split("=")
    config[parameter] = float(value) if "." in value else int(value)
file.close()

print(config)

archivo = open("mandelbrot.csv", "r")
lineas = archivo.readlines()
archivo.close()

# NO OLVIDAR QUITAR ENCABEZADOS
lineas.pop(0)

# PROCESS
max_iter = config["max_iter"]
ancho, alto = config["ancho"], config["alto"]

img = Image.new("L", (ancho, alto))

for linea in lineas:
    row, column, iterations = linea.strip().split(",")
    iterations = int(iterations)
    row = int(row)
    column = int(column)
    
    # Puntos que no escapan (pertenecen al conjunto) son negros
    if iterations == max_iter:
        brillo = 0
    else:
        # Normalización de 0 a 255
        brillo = int((iterations / max_iter) * 255)
    
    img.putpixel((column, row), brillo)

# OUTPUT
img.save("mandelbrot.png")
print("DONE")