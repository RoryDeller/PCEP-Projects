def liters_100km_to_miles_gallon(liters):
    litres_per_metre = liters / 100000
    litres_per_mile = litres_per_metre * 1609.344
    gallons_per_mile = litres_per_mile / 3.785411784
    miles_per_gallon = 1 / gallons_per_mile  
    
    return miles_per_gallon
    


def miles_gallon_to_liters_100km(miles):
    metres_per_gallon = miles * 1609.344
    metres_per_litre = metres_per_gallon / 3.785411784
    litres_per_100km = 100000 / metres_per_litre 
    
    return litres_per_100km



print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
