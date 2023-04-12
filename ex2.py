cars= 100
space_in_car= 4.0
drivers= 30
passenger= 90
cars_not_driven= cars - drivers
cars_driven= drivers
carpool_capacity= cars_driven*space_in_car
average_passengers_per_car= passenger/cars_driven

print("Existen", cars,"carros disponibles." )
print("Solo hay", drivers, "choferes disponibles. ")
print("Habrá",cars_not_driven,"carros sin usar. ")
print("Podemos transportar",carpool_capacity,"personas hoy." )
print("Tenemos",passenger,"pasajeros para transportar hoy. ")
print("necesitamos poner alrededor de",average_passengers_per_car,"personas por auto")
