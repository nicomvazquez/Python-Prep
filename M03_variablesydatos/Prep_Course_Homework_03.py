#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

num = 912
print(num)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

type(8.5)


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

type(num)



# 4) Crear una variable que contenga tu nombre

# In[2]:

mi_nombre = 'Nicolas Vazquez'



# 5) Crear una variable que contenga un número complejo

# In[3]:

num_complejo = 3+4j



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

type(num_complejo)




# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:

pi = 3.1416
pi_redondeado = round(pi, 4)

print(pi_redondeado)


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

verdadero_string = "true"

verdadero_booleano = True

# no son lo mismo, uno es un string y el otro es un booleano


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

type(verdadero_string)
type(verdadero_booleano)



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma = 3 + 5.4



# 11) Realizar una operación de suma de números complejos

# In[2]:

suma_compleja = 4j + 1j



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

suma_real_compleja = 3 +4j


# 13) Realizar una operación de multiplicación

# In[5]:

producto = 3 * 5


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

potencia = 2**8


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

cociente = 27 / 4


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

part_entera = 27 // 4

print(part_entera)


# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

resto = 27 % 4

print(resto)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

num27 = part_entera * 4 + resto

print(num27)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

ejemplo1 = "Hola "
ejemplo2 = "Mundo"

texto = ejemplo1 + ejemplo2 
print(texto)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

# "2" es un string y 2 es un entero



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

num2 = "2"
num2 == int(num2)

print(num2 = 2)


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

# da erroe porque en python el separador decimal es "." y no ","


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

variable_cambia = 3
variable_cambia -= 1


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

print(1 << 2)

# El sistema de numeración binario es un sistema de numeración en el que se utilizan solamente dos dígitos: 0 y 1. 
# La operación << es un operador de desplazamiento a la izquierda en el cual cada bit en la representación binaria se desplaza a la izquierda por un número de posiciones indicado por el segundo operando. En el caso de 1 << 2, estamos desplazando el bit 1 dos posiciones a la izquierda


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

# no esta permitido porque estas operando con dos datos de distinto tipo


# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

number = 3000
cadena = "server listening in port: "

print(cadena + str(number))