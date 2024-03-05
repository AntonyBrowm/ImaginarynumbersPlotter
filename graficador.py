import numpy as np
import matplotlib.pyplot as plt
import re

def calcular_forma_polar(z, theta, angulo_en_grados=True):
    # Convertir theta a radianes si está en grados
    if angulo_en_grados:
        theta_rad = np.deg2rad(theta)
    else:
        theta_rad = theta
    
    # Calcular r
    r = np.abs(z)
    
    # Calcular las partes real e imaginaria en forma polar
    real_part = r * np.cos(theta_rad)
    imaginary_part = r * np.sin(theta_rad)
    
    return r, theta_rad, real_part, imaginary_part

def graficar_forma_polar(z, r, theta_rad, real_part, imaginary_part):
    # Crear el gráfico
    plt.figure(figsize=(6,6))
    plt.plot([0, real_part], [0, imaginary_part], 'r', label=f'z = {z_str}')
    plt.plot(real_part, imaginary_part, 'ro')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.title(f'Forma Polar de z = {z_str}')
    plt.legend()
    plt.show()

def parse_complex_number(complex_str):
    try:
        # Tratar de convertir directamente la cadena a un número complejo
        z = complex(complex_str)
        return z, f"{z.real}{'+' if z.imag >= 0 else '-'}{abs(z.imag)}i"
    except ValueError:
        # Si falla, entonces usar expresiones regulares para extraer las partes real e imaginaria
        match = re.match(r'([-+]?\d*\.?\d*)([-+][-+]?\d*\.?\d*)i', complex_str)
        if match:
            real_part = float(match.group(1))
            imag_part = float(match.group(2))
            return complex(real_part, imag_part), f"{real_part}{'+' if imag_part >= 0 else '-'}{abs(imag_part)}i"
        else:
            raise ValueError("Formato incorrecto para el número complejo. Debe ser en el formato a + bi.")

# Solicitar al usuario el valor de z y theta
z_str = input("Ingrese el valor de z en formato a + bi (por ejemplo, 1+2i): ")
theta_str = input("Ingrese el valor de theta (en grados o radianes): ")

# Convertir theta a radianes si es necesario
theta = eval(theta_str.replace('pi', str(np.pi)))  # Reemplazar 'pi' con el valor de pi

# Parsear el número complejo
try:
    z, z_str = parse_complex_number(z_str.replace('i', 'j'))  # Reemplazar 'i' con 'j' para evaluar la expresión
except ValueError as e:
    print(e)
    exit()

# Calcular la forma polar
r, theta_rad, real_part, imaginary_part = calcular_forma_polar(z, theta)

# Graficar la forma polar
graficar_forma_polar(z, r, theta_rad, real_part, imaginary_part)
