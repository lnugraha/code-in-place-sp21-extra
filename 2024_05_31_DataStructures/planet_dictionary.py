planet_dict_list = [
  {"mercury": 0.376}, 
  {"venus": 0.889},
  {"earth": 1.0},  
  {"mars": 0.378},
  {"jupiter": 2.36}, 
  {"saturn": 1.081}, 
  {"uranus": 0.815}, 
  {"neptune": 1.14}
]

planet_dict = {
  "mercury": 0.376, 
  "venus": 0.889,
  "earth": 1.0,  
  "mars": 0.378,
  "jupiter": 2.36, 
  "saturn": 1.081, 
  "uranus": 0.815, 
  "neptune": 1.14
  }

def calculate_weight_alternative(target_planet, earth_weight):
    planet_name = target_planet.lower()
    planet_constant = -1.0

    if planet_dict[ planet_name ] is not None:
        planet_constant = planet_dict[planet_name]
    
    planet_weight = planet_constant * earth_weight

    return planet_weight

def calculate_weight(target_planet, earth_weight):
    # TODO: Check the earth weight, make sure >= 0 and numbers only
    # TODO: Check that the target planet name is listed in the dictionary, otherwise return an error

    planet_name = target_planet.lower()
    planet_constant = -1.0
    for i in range( len(planet_dict_list) ):
        for name, gravity in planet_dict_list[i].items():
            if (planet_name == name):
                planet_constant = gravity
    planet_weight = planet_constant * earth_weight

    return planet_weight

def main():
  earth_weight = float(input("Enter the object weight: "))
  planet_name = input("Enter a planet name: ")
  
  # planet_weight = calculate_weight(planet_name, earth_weight)

  planet_weight = calculate_weight_alternative(planet_name, earth_weight)
  print("The name of the planet: " + planet_name + " with weight: " + str(planet_weight))

if __name__ == '__main__':
    main()
