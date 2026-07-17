# INPUT
config = {}

file = open("config.txt", "r")

for line in file:
    parameter, value = line.strip().split("=")
    config[parameter] = float(value) if "." in value else int(value)
file.close()

ancho = int(config["ancho"])
alto = int(config["alto"])
max_iter = int(config["max_iter"])

output = open("mandelbrot.csv", "w")
output.write("fila,columna,iteraciones\n")

# PROCESS
for fila in range(alto):
    for columna in range(ancho):
        real = config["real_min"] + (columna / ancho) * (config["real_max"] - config["real_min"])
        imag = config["imag_min"] + (fila / alto) * (config["imag_max"] - config["imag_min"])
        c = complex(real, imag)
        
        z = 0 + 0j
        iteraciones = 0
        
        while (abs(z) <= 2) and (iteraciones < max_iter):
            z = z * z + c
            iteraciones += 1
        
        output.write(f"{fila},{columna},{iteraciones}\n")

output.close()

# OUTPUT
print("DONE")