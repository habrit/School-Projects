#Hunter Britton AERO 201 HW 1 Standard Atmosphere Table
#UIN: 228007278
#2/5/2021

#This program helps calculate the pressure, temperature, density and the speed of sound from a given geometric altitude
import math

h2 = 0
pressureSeaLevel = 2116.2
densitySeaLevel = 0.002377
tempSeaLevel = 518.69
gravity = 32.17405
radius = 20902000
gas_constant = 1716
lambd = 1.4 #lambda

geometric_altitude = float(input("Please enter the geometric altitude."))

geopotential_altitude = (radius / (radius + geometric_altitude)) * geometric_altitude

if ( 0 <= geopotential_altitude <= 36089.24): #first gradient region
#First Gradient
    a = -0.0065
    a0 = a * (1.8 / 3.28084)
    temp = tempSeaLevel + (a0 * geopotential_altitude)
    pressure = pressureSeaLevel * (temp / tempSeaLevel)**((-1 * gravity) / (a0 * gas_constant))
    density = densitySeaLevel * (temp / tempSeaLevel)**(-1 * ((gravity / (a0 * gas_constant))+ 1))
    speedSound = math.sqrt(lambd * gas_constant * temp)

    print ("Geopotential Altitude: ", geopotential_altitude, "feet" ,"temperature:", temp, "Rankine","Pressure: ", pressure, "lb/ft^2 ", "density: ", density, "slugs/ft^3","speed of sound: ", speedSound, "feet/s")

elif (36089.24 < geopotential_altitude < 82021): #first isothermal region

    temp = 389.988
    pressureIsoBase = 472.688
    densityIsoBase = 0.000706201
    pressure = pressureIsoBase * math.exp(-1 * (gravity / (gas_constant * temp)) * (geopotential_altitude - 36089.24))
    density = densityIsoBase * math.exp(-1 * (gravity / (gas_constant * temp)) * (geopotential_altitude - 36089.24))
    speedSound = math.sqrt(lambd * gas_constant * temp)

    print ("Geopotential Altitude: ", geopotential_altitude, "feet" ,"temperature:", temp, "Rankine","Pressure: ", pressure, "lb/ft^2", "density: ", density, "slugs/ft^3","speed of sound: ", speedSound, "feet/s")


elif (82021 <= geopotential_altitude <= 154199):
#Second Gradient
    a = .003
    pressureGradTwo = 52.4441
    tempGradTwoStart = 389.99
    tempGradTwoEnd = 508.788
    a1 = a * (1.8 / 3.28084)
    densityGradTwo = 0.0000765854
    temp = (a1 * geopotential_altitude) + (tempGradTwoStart - 135.823)
    pressure = pressureGradTwo * (temp / tempGradTwoStart) ** ((-1 * gravity) / (a1 * gas_constant))
    density = densityGradTwo * (temp / tempGradTwoStart) ** (-1 * ((gravity / (a1 * gas_constant)) + 1))
    speedSound = math.sqrt(lambd * gas_constant * temp)

    print ("Geopotential Altitude: ", geopotential_altitude, "feet" ,"temperature:", temp, "Rankine","Pressure: ", pressure, "lb/ft^2", "density: ", density, "slugs/ft^3","speed of sound: ", speedSound, "feet/s")



h2 = 0

while (h2 <= 36000):
    geopotential_altitude = h2
    a = -0.0065
    a0 = a * (1.8 / 3.28084)
    temp = tempSeaLevel + (a0 * geopotential_altitude)
    pressure = pressureSeaLevel * (temp / tempSeaLevel)**((-1 * gravity) / (a0 * gas_constant))
    density = densitySeaLevel * (temp / tempSeaLevel)**(-1 * ((gravity / (a0 * gas_constant))+ 1))
    speedSound = math.sqrt(lambd * gas_constant * temp)

    print ("Geopotential Altitude: ", h2, "feet" ,"temperature:", temp, "Rankine","Pressure: ", pressure, "lb/ft^2", "density: ", density, "slugs/ft^3","speed of sound: ", speedSound, "feet/s")
    print('--------------------------------------------------------')
    h2 = h2 + 500

while (36000 < h2 <= 82000):
    temp = 389.988
    pressureIsoBase = 472.688
    densityIsoBase = 0.000706201
    pressure = pressureIsoBase * math.exp(-1 * (gravity / (gas_constant * temp)) * (h2 - 36089.24))
    density = densityIsoBase * math.exp(-1 * (gravity / (gas_constant * temp)) * (h2 - 36089.24))
    speedSound = math.sqrt(lambd * gas_constant * temp)

    print ("Geopotential Altitude: ", h2, "feet" ,"temperature:", temp, "Rankine","Pressure: ", pressure, "lb/ft^2", "density: ", density, "slugs/ft^3","speed of sound: ", speedSound, "feet/s")
    print('--------------------------------------------------------')
    h2 = h2 + 500
while (82000 < h2 <= 100000):
    a = .003
    pressureGradTwo = 52.4441
    tempGradTwoStart = 389.99
    tempGradTwoEnd = 508.788
    a1 = a * (1.8 / 3.28084)
    densityGradTwo = 0.0000765854
    temp = (a1 * h2) + (tempGradTwoStart - 135.823)
    pressure = pressureGradTwo * (temp / tempGradTwoStart) ** ((-1 * gravity) / (a1 * gas_constant))
    density = densityGradTwo * (temp / tempGradTwoStart) ** (-1 * ((gravity / (a1 * gas_constant)) + 1))
    speedSound = math.sqrt(lambd * gas_constant * temp)

    print ("Geopotential Altitude: ", h2, "feet" ,"temperature:", temp, "Rankine","Pressure: ", pressure, "lb/ft^2", "density: ", density, "slugs/ft^3","speed of sound: ", speedSound, "feet/s")
    print('--------------------------------------------------------')
    h2 = h2 + 500
