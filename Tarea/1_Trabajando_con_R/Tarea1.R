# Ejercicio 1
duration = 250000000
time = 0
sec_solar_year = 24*3600*365
sec_b_year = 24*3600*366

#Primeros 2 años no bisiestos
time = duration - (2 * sec_solar_year)
#Primer año bisiesto
time = time - sec_b_year
#4 años no bisistos
time = time - (4 * sec_solar_year)

year = 7

#dias
days = time %/% (24*3600)
rest_days = time %% (24*3600)

#horas
hours = rest_days %/% 3600
rest_hours = rest_days %% 3600

#minutes
minutes = rest_hours %/% 60
seconds = rest_hours %% 60

sprintf("Año: %i, Día: %i a las %i:%i:%i", (2018+year), days, hours, minutes, seconds)


#Ejercicio 2
ecuacion = function(A,B,C){
  x = (C-B)/A
}

z1 = ecuacion(5,3,0)
sprintf("La ecuacion 5x+3=0 es igual a: %f",z1)
z2 = ecuacion(7,4,18)
sprintf("La ecuacion 7x+4= es igual a: %f",z2)
z3 = ecuacion(1,1,1)
sprintf("La ecuacion x+1=1 es igual a: %f",z3)


# Ejercicio 3

#Calcular 3e-pi
round((3*exp(1) - pi), 3)

#Calcular el modulo de (2+3i)^2/(5+8i)
z1 = (2+3i)^2 / (5+8i)
round(Mod(z1),3)
