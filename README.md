# Code in Place Spring 2023 - Stanford University

Extra suplemental materials dedicated to Code in Place Spring 2023 with Stanford University

Topics to be covered:

## Input Arguments (Week 2: May 05, 2023) ##
<details>
<summary> User Input Prompt: remember all data types are still in string </summary>

```python
def main():
  user_name = input("Enter your name: ")
  print("Good morning " + user_name)
```
</details>  

## Console Programming (Week 3: May 12, 2023) ##

### Conditional Branching ###
<details>
<summary> 1. <b>IF-ELIF-ELSE</b> Statement </summary>

```python
def main():
  pass
```
</details>

<details>
<summary> 2. <b>MATCH-CASE</b> Statement (Require Python 3.10 or above) </summary>

```python
def main():
  pass
```
</details>

### Printing in Python ###
<b> 1. String Concatenation </b>
- Notice that both "+" and "," can be used interchangably
- Concatenate multiple strings with + (plus) or , (comma)
- All concatenated items have to be converted to the same data type (string)
```python
planetName = "Mars"
planetWeight = 175.26
print("The weight on " + planetName + ": " + str(marsWeight))
print("The weight on " , planetName + ": " , str(marsWeight))
```

<b> 2. Reference </b>
- Notice the ```.format(,)``` patten
- Unlike concatenation method, this method requires no string conversion
- Use the {} (curly brackets) to place your variable
```python
planetName = "Mars"
planetWeight = 175.26
print("The weight on {}: {}".format(planetName, planetWeight))
```
<b> 3. F-word </b>
- Notice the f letter inside print()
- Similar to method 2 (reference), but now variable name is placed inside the curly brackets 
- Likewise, no variable casting (conversion) is needed
```python
print(f"The weight on {planetName}: {planetWeight}")
```

## Functions with Parameters (Week 4: May 19, 2023) ##
<details>
<summary> 1. <b>Single</b> Output Return </summary>

```python
def single_output_function(input_1, input_2, input_3):
  output = input_1 * input_2 * input_3
  return output
```
</details>

<details>
<summary> 2. <b>Multiple</b> Outputs Return </summary>

```python
def multi_output_function(input_1, input_2):
  # Begin by declaring def, brackets, and colon sign (:)
  output_1 = input_1 + input_2
  output_2 = input_1 * input_2
      
  # The correct word is return, NOT result
  return output_1, output_2
```
</details>

## Graphics and Image Processing (Week 5: May 26, 2023) ##

  - Coming Soon

## Data Structures: Containers (Week 6: June 02, 2023) ##

  - Coming Soon
