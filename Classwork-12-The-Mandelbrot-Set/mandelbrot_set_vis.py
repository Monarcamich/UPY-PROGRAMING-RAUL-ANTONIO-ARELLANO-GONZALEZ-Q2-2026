from PIL import Image
config = {}

file = open('config.txt', 'r')

for line in file:
    parameter, value = line.strip().split('=')
    config[parameter] = float(value) if "." in value else int(value)
file.close()

print(config)

archivo = open("mandelbrot.csv", "r")
lineas = archivo.readlines()
archivo.close()

lineas.pop(0)  # Remove header line

#DESEMOAQUETAR VARIABLES 

max_iter = config['max_iter']
ancho, alto = config['ancho'], config['alto']
img= Image.new('L',(ancho,alto))

for linea in lineas:
    row, column, iterations = linea.strip().split(",")
    iterations = int(iterations)
    row = int(row)
    column = int(column)

    if iterations == max_iter:
        brillo = 40  # Black for points inside the Mandelbrot set
    else:
        brillo = int((iterations / max_iter)*255)  # White for points outside the Mandelbrot set

    img.putpixel((column, row), brillo)

img.save('mandelbrot.png')
print("DONE")


