mars_dictionary = { "mars" : 0.378 }

def calculate_mars_weight(earth_weight_float):
    if earth_weight_float <= 0:
        raise ValueError("Cannot have weight equals to or less than zero")

    if type(earth_weight_float) not in [int, float]:
        raise TypeError("Cannot have weight that is not in rational number")

    mars_weight_float = mars_dictionary['mars'] * earth_weight_float

    return mars_weight_float

def main():
    earth_weight_string = input('Enter a weight on earth: ')
    earth_weight_float = float(earth_weight_string)

    mars_weight_float = calculate_mars_weight(earth_weight_float)
    mars_weight_string = str(mars_weight_float)

    print('The equivalent weight on Mars: ' + mars_weight_string)

if __name__ == '__main__':
    main()
