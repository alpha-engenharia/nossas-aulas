def z(a, b):
    return [a, b]

def re(z):
    return z[0]

def im(z):
    return z[1]

def oposto(z):
    return [-re(z), -im(z)]

def conjugado(z):
    return [re(z), -im(z)]

def modulo(z):
    return (re(z)**2 + im(z)**2)**0.5

def rad(z):
    from math import acos
    if modulo(z) == 0:
        return 0
    else:    
        return acos(re(z)/modulo(z))
    
def grau(z):
    from math import pi
    return 180 * rad(z)/pi

def somar(z1, z2):
    return [re(z1) + re(z2), im(z1) + im(z2)]

def multiplicar(z1, z2):
    return [re(z1)*re(z2) - im(z1)*im(z2), re(z1)*im(z2) + re(z2)*im(z1)]

def subtrair(z1, z2):
    return somar(z1, oposto(z2))

def dividir(z1, z2):
    z = multiplicar(z1, conjugado(z2))
    return  [re(z)/modulo(z2)**2, im(z)/modulo(z2)**2]