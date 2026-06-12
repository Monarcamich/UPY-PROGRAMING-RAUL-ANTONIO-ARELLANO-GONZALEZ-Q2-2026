#INPUT
a = (input("Write left endpoint of the interval:"))
b = (input("Write the rigth endpoint of the interval:"))
f_x = (input("Write the function to integrate: "))
method =(input("selecet the method to integrate (LRM/RRM): "))
#PROCESS
area: 0.0
n = 1000
h = (b-a)/n
constant = 0
if method == "RRM":
    shift = 1
elif method == "MPM":
    constant = h/2
else:
    pass

for i in range (n):
    xi = a+ i * h + constant
    height = eval(f_x.replace("x", str(xi)))
    area += height * h

#OUTPUT
print(f"The integration of {f_x} is {area}")