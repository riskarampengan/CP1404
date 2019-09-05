COLOR_CODES = {"Black": "#000000",
               "blue1": "#0000ff",
               "blue4": "#00008b",
               "gold1": "#ffd700",
               "gray": "#bebebe",
               "green3": "#00cd00",
               "LavenderBlush2": "#eee0e5",
               "LightBlue1": "#bfefff",
               "NavyBlue": "#000080",
               "red1": "#ff0000",
               "yellow1": "#ffff00"}

color_name = input("Enter a color name: ")
while color_name != "":
    print("The color code for \"{}\" is {}".format(color_name, COLOR_CODES.get(color_name)))
    color_name = input("Enter a color name: ")