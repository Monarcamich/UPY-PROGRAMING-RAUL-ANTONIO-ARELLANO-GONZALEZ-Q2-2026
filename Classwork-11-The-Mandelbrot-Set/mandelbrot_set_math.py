config={}
file = open ('config.txt','r')

for line in file:
    parameter, value =line.strip().split('=')
    config[parameter] = float(value) if "." in value else int(value)
file.close()

width, height, max_iter = config["ancho"], config["alto"], config["max_iter"]

output = open("mandelbrot.csv", "w")
output.write("row,column,iterations\n")


ancho = config['ancho']
alto = config['alto']
max_iter = config['max_iter']
'''
Formula:

real = real_min + (columna / ancho) * (real_max - real_min)
imag = imag_min + (fila /alto) * (imag_max - imag_min)
c = complex (real, imag)

'''
for fila in range(alto):
    for columna in range(ancho):
        real = config['real_min'] + (columna / ancho) * (config['real_max'] - config['real_min'])
        imag = config['imag_min'] + (fila / alto) * (config['imag_max'] - config['imag_min'])      
        c = complex (real, imag)

for fila in range (alto):
    for columna in range(ancho):
        z = 0 + 0j
        iteraciones = 0

        while abs(z) < 2 and iteraciones < config['max_iter']:
            z = z * z +c
            iteraciones += 1
        output.write(f"{columna} {fila} {iteraciones}\n")

print("DONE")


