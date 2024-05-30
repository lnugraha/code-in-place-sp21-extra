# Code in Place Spring 2024 - Stanford University

Extra suplemental materials dedicated to Code in Place Spring 2024 with Stanford University

Topics to be covered:

## Input Arguments (Week 2: May 03, 2024) ##
<details>
<summary> User Input Prompt: remember all data types are still in string </summary>

```python
def main():
  user_name = input("Enter your name: ")
  print("Good morning " + user_name)
```
</details>  

## Console Programming (Week 3: May 10, 2024) ##

### Conditional Branching ###
<details>
<summary> 1. <b>IF-ELIF-ELSE</b> Statement </summary>

```python
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
  
  if (planetName == "Mercury"):
    planetWeight = float(earthWeight) * MERCURY_GRAVITY
        
  elif (planetName == "Venus"):
    planetWeight = float(earthWeight) * VENUS_GRAVITY
        
  elif (planetName == "Mars"):
    planetWeight = float(earthWeight) * MARS_GRAVITY

  elif (planetName == "Jupiter"):
    planetWeight = float(earthWeight) * JUPITER_GRAVITY
        
  elif (planetName == "Saturn"):
    planetWeight = float(earthWeight) * SATURN_GRAVITY

  elif (planetName == "Uranus"):
    planetWeight = float(earthWeight) * URANUS_GRAVITY
        
  elif (planetName == "Neptune"):
    planetWeight = float(earthWeight) * NEPTUNE_GRAVITY
    
  else:
    planetWeight = -1.0 # Why put a negative value here?
```
</details>

<details>
<summary> 2. <b>IF</b> Statement</summary>

```python
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
  planetWeight = -1 # Why put a negative value here?

  if (planetName == "Mercury"):
    planetWeight = float(earthWeight) * MERCURY_GRAVITY
        
  if (planetName == "Venus"):
    planetWeight = float(earthWeight) * VENUS_GRAVITY
        
  if (planetName == "Mars"):
    planetWeight = float(earthWeight) * MARS_GRAVITY

  if (planetName == "Jupiter"):
    planetWeight = float(earthWeight) * JUPITER_GRAVITY
        
  if (planetName == "Saturn"):
    planetWeight = float(earthWeight) * SATURN_GRAVITY

  if (planetName == "Uranus"):
    planetWeight = float(earthWeight) * URANUS_GRAVITY
        
  if (planetName == "Neptune"):
    planetWeight = float(earthWeight) * NEPTUNE_GRAVITY
```
</details>

<details>
<summary> 3. <b>MATCH-CASE</b> Statement (Require Python 3.10 or above) </summary>

```python
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
  
    case other:
      planetWeight = -1.0 # Why put a negative value here?
```
</details>

### Printing in Python ###
<b> 1. String Concatenation </b>
- Notice that both "+" and "," can be used interchangably
- Concatenate multiple strings with + (plus) or , (comma)
- All concatenated items have to be converted to the same data type (string)
<details>
<summary> Examples </summary>
  
```python
planetName = "Mars"; planetWeight = 175.26
print("The weight on " + planetName + ": " + str(marsWeight))
print("The weight on " , planetName + ": " , str(marsWeight))
```

</details>

<b> 2. Reference </b>
- Notice the ```.format(,)``` patten
- Unlike concatenation method, this method requires no string conversion
- Use the {} (curly brackets) to place your variable
<details>
<summary> Examples </summary>
 
```python
planetName = "Mars"; planetWeight = 175.26
print("The weight on {}: {}".format(planetName, planetWeight))
```
</details>

<b> 3. F-word </b>
- Notice the f letter inside print()
- Similar to method 2 (reference), but now variable name is placed inside the curly brackets 
- Likewise, no variable casting (conversion) is needed
<details>
<summary> Examples </summary>
  
```python
planetName = "Mars"; planetWeight = 175.26
print(f"The weight on {planetName}: {planetWeight}")
```
</details>

## Control Flow (Week 4: May 17, 2024) ##

### Writing Functions ###
<b> 1. Returning a Single Output </b>

<details>
<summary> Example: </summary>
  
```python
def calculate_mars_weight(earth_weight):
  MARS_GRAVITY = 0.376
  mars_weight = float(earth_weight) * MARS_GRAVITY
  return round(mars_weight, 2)
  
def main():
  earth_test = float(input("Enter the object weight on Earth: "))
  mars_test = calculate_mars_weight(earth_test)
```
</details>

<b> 2. Returning More than One Output </b>

<details>
<summary> Example: </summary>
  
```python
def calculate_planet_weights(earth_weight):
  MERCURY_GRAVITY = 0.376
  VENUS_GRAVITY = 0.889
  MARS_GRAVITY = 0.378

  mercury_weight = earth_weight * MERCURY_GRAVITY
  venus_weight = earth_weight * VENUS_GRAVITY
  mars_weight = earth_weight * MARS_GRAVITY

  return round(mercury_weight, 2), round(venus_weight, 2), round(mars_weight, 2)
  
def main():
  earth_test = float(input("Enter the object weight on Earth: "))
  mercury_test, venus_test, mars_test = calculate_planet_weights(earth_test)
```
</details>

## Canvas, Graphics, and Animation (Week 5: May 24, 2024) ##

## Data Structures (Week 6: May 31, 2024) ##
<b> 1. Calculating Factorial </b>

<b> 2. Revisiting Planetary Weight </b>

<b> 3. Plotting Regression Line </b>

