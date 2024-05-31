from matplotlib import pyplot as plt

snow_yield_dictionary = [
        {"Snow": 
         [23.1, 32.8, 31.8, 32.0, 30.4, 24.0, 39.5, 24.2, 52.5, 37.9, 30.5, 25.1, 12.4, 35.1, 31.5, 21.1, 27.6]
         },
        {"Yield": 
         [10.5, 16.7, 18.2, 17.0, 16.3, 10.5, 23.1, 12.4, 24.9, 22.8, 14.1, 12.9, 8.8, 17.4, 14.9, 10.5, 16.1]
         }
        ]

def plot_the_curve():
    snow_dictionary = snow_yield_dictionary[0]
    yield_dictionary = snow_yield_dictionary[1]

    snow_list = snow_dictionary["Snow"]
    yield_list = yield_dictionary["Yield"]

    plt.title("Plot of Snow vs Yield"); plt.xlabel("Snow"); plt.ylabel("Yield")
    plt.scatter(snow_list, yield_list, c='blue', marker='H')
    plt.show()
    plt.savefig('plot_of_snow_vs_yield.png')

def main():
    plot_the_curve()

if __name__ == "__main__":
    main()


