import math

def main():
  MERCURY_GRAVITY = (37.6 / 100)
  VENUS_GRAVITY = (88.9 / 100)
  MARS_GRAVITY = (37.8 / 100)
  JUPITER_GRAVITY = (236 / 100)
  SATURN_GRAVITY = (108.1 / 100)
  URANUS_GRAVITY = (81.5 / 100)
  NEPTUNE_GRAVITY = (114 / 100)    

  earthWeight = float(input("Enter the object weight: "))
  planetName = input("Enter a planet name: ")
  
  match planetName:
    case "Mercury":
        planetWeight = float(earthWeight) * MERCURY_GRAVITY
  
    case "Venus":
        planetWeight = float(earthWeight) * VENUS_GRAVITY
  
    case "Mars":
        planetWeight = float(earthWeight) * MARS_GRAVITY
  
    case "Jupiter":
        planetWeight = float(earthWeight) * JUPITER_GRAVITY
      
    case "Saturn":
        planetWeight = float(earthWeight) * SATURN_GRAVITY
  
    case "Uranus":
        planetWeight = float(earthWeight) * URANUS_GRAVITY
  
    case "Neptune":
        planetWeight = float(earthWeight) * NEPTUNE_GRAVITY
  
    case "Earth":
        planetWeight = float(earthWeight)

    case other:
        planetWeight = -1.0 # Why put a negative value here?

  print("The name of the planet: " + planetName + " with weight: " + str(planetWeight))

if __name__ == '__main__':
    main()