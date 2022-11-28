import math
import webcolors
from webcolors import rgb_to_name
from webcolors import hex_to_rgb
    # https://medium.com/codex/rgb-to-color-names-in-python-the-robust-way-ec4a9d97a01f
from scipy.spatial import KDTree

#from rangeSelection import getResult
from rangeSelection import getAreaCorners

import PIL
from PIL import ImageGrab
    # https://stackoverflow.com/questions/42636933/get-rgb-value-from-screen-pixels-with-python

# Color counter variables
red_count = 0
green_count = 0
blue_count = 0
black_count = 0
gray_count = 0
purple_count = 0
yellow_count = 0
orange_count = 0
white_count = 0
brown_count = 0
pink_count = 0
count_array = []
average_array = []
range_size = 0

#Detect color function definition
def detect_color():
    #Calls rangeSelector function and sets it to selected range

    selectedRange = getAreaCorners()
    #Determines the starting location of the range
    startX = selectedRange[0][0]
    startY = selectedRange[0][1]
    #Determines the ending location of the range
    endX = selectedRange[1][0]
    endY = selectedRange[1][1]
    #Determines the range of x of the selected range
    xRange = endX - startX
    #Determines the range of y of the selected range
    yRange = endY - startY
    #Determines how many pixels are in the selected range
    global range_size
    range_size = xRange * yRange
    #Gets the RGB values of each pixel in the range and sends it to be counted
    for x in range(startX, endX):
        for y in range(startY, endY):
            try:
                rgb = PIL.ImageGrab.grab().load()[x, y]
                named_color = rgb_to_name(rgb, spec='css3')
                count_color(named_color)
            except Exception:
                name_database = webcolors.CSS3_HEX_TO_NAMES
                names = []
                rgb_values = []
                for color_hex, color_name in name_database.items():
                    names.append(color_name)
                    rgb_values.append(hex_to_rgb(color_hex))

                database_dt = KDTree(rgb_values)

                distance, index = database_dt.query(rgb)
                count_color(f'{names[index]}')


    #Calls the function to print the color breakdown

    #Calls the function to print the color average


#Count color function definition, takes variable named_color
def count_color(named_color):
    #Includes the global variables
    global red_count
    global green_count
    global blue_count
    global black_count
    global gray_count
    global purple_count
    global yellow_count
    global orange_count
    global white_count
    global brown_count
    global pink_count

    #Shows the program is running...will be removed later
    print("Running...")

    #Determines what color to count the pixel towards
    if named_color == "black":
        black_count += 1
    elif named_color == "silver":
        gray_count += 1
    elif named_color == "gray":
        gray_count += 1
    elif named_color == "white":
        white_count += 1
    elif named_color == "maroon":
        red_count += 1
    elif named_color == "red":
        red_count += 1
    elif named_color == "purple":
        purple_count += 1
    elif named_color == "fuchsia":
        purple_count += 1
    elif named_color == "green":
        green_count += 1
    elif named_color == "lime":
        green_count += 1
    elif named_color == "olive":
        green_count += 1
    elif named_color == "yellow":
        yellow_count += 1
    elif named_color == "navy":
        blue_count += 1
    elif named_color == "blue":
        blue_count += 1
    elif named_color == "teal":
        blue_count += 1
    elif named_color == "aqua":
        blue_count += 1
    elif named_color == "aliceblue":
        blue_count += 1
    elif named_color == "antiquewhite":
        white_count += 1
    elif named_color == "aquamarine":
        blue_count += 1
    elif named_color == "azure":
        blue_count += 1
    elif named_color == "beige":
        white_count += 1
    elif named_color == "bisque":
        white_count += 1
    elif named_color == "blanchealmond":
        white_count += 1
    elif named_color == "blueviolet":
        purple_count += 1
    elif named_color == "brown":
        brown_count += 1
    elif named_color == "burlywood":
        brown_count += 1
    elif named_color == "cadetblue":
        blue_count += 1
    elif named_color == "chartreuse":
        green_count += 1
    elif named_color == "chocolate":
        brown_count += 1
    elif named_color == "coral":
        orange_count += 1
    elif named_color == "cornflowerblue":
        blue_count += 1
    elif named_color == "cornsilk":
        white_count += 1
    elif named_color == "crimson":
        red_count += 1
    elif named_color == "cyan":
        blue_count += 1
    elif named_color == "darkblue":
        blue_count += 1
    elif named_color == "darkcyan":
        blue_count += 1
    elif named_color == "darkgoldenrod":
        brown_count += 1
    elif named_color == "darkgray":
        gray_count += 1
    elif named_color == "darkgreen":
        green_count += 1
    elif named_color == "darkkhaki":
        yellow_count += 1
    elif named_color == "darkmagenta":
        purple_count += 1
    elif named_color == "darkolivegreen":
        green_count += 1
    elif named_color == "darkorange":
        orange_count += 1
    elif named_color == "darkorchid":
        purple_count += 1
    elif named_color == "darkred":
        red_count += 1
    elif named_color == "darksalmon":
        red_count += 1
    elif named_color == "darkseagreen":
        green_count += 1
    elif named_color == "darkslateblue":
        blue_count += 1
    elif named_color == "darkslategray":
        green_count += 1
    elif named_color == "darkturquoise":
        blue_count += 1
    elif named_color == "darkviolet":
        purple_count += 1
    elif named_color == "deeppink":
        pink_count += 1
    elif named_color == "deepskyblue":
        blue_count += 1
    elif named_color == "dimgray":
        gray_count += 1
    elif named_color == "dodgerblue":
        blue_count += 1
    elif named_color == "firebrick":
        red_count += 1
    elif named_color == "floralwhite":
        white_count += 1
    elif named_color == "forestgreen":
        green_count += 1
    elif named_color == "gainsboro":
        gray_count += 1
    elif named_color == "ghostwhite":
        white_count += 1
    elif named_color == "gold":
        yellow_count += 1
    elif named_color == "goldenrod":
        yellow_count += 1
    elif named_color == "greenyellow":
        green_count += 1
    elif named_color == "honeydew":
        green_count += 1
    elif named_color == "hotpink":
        pink_count += 1
    elif named_color == "indianred":
        red_count += 1
    elif named_color == "indigo":
        blue_count += 1
    elif named_color == "ivory":
        white_count += 1
    elif named_color == "khaki":
        yellow_count += 1
    elif named_color == "lavender":
        purple_count += 1
    elif named_color == "lavenderblush":
        pink_count += 1
    elif named_color == "lawngreen":
        green_count += 1
    elif named_color == "lemonchiffon":
        yellow_count += 1
    elif named_color == "lightblue":
        blue_count += 1
    elif named_color == "lightcoral":
        red_count += 1
    elif named_color == "lightcyan":
        blue_count += 1
    elif named_color == "lightgoldenrodyellow":
        yellow_count += 1
    elif named_color == "lightgray":
        gray_count += 1
    elif named_color == "lightgreen":
        green_count += 1
    elif named_color == "lightpink":
        pink_count += 1
    elif named_color == "lightsalmon":
        orange_count += 1
    elif named_color == "lightseagreen":
        green_count += 1
    elif named_color == "lightskyblue":
        blue_count += 1
    elif named_color == "lightslategray":
        gray_count += 1
    elif named_color == "lightsteelblue":
        blue_count += 1
    elif named_color == "lightyellow":
        yellow_count += 1
    elif named_color == "limegreen":
        green_count += 1
    elif named_color == "linen":
        white_count += 1
    elif named_color == "magenta":
        purple_count += 1
    elif named_color == "mediumaquamarine":
        green_count += 1
    elif named_color == "mediumblue":
        blue_count += 1
    elif named_color == "mediumorchid":
        purple_count += 1
    elif named_color == "mediumpurple":
        purple_count += 1
    elif named_color == "mediumseagreen":
        green_count += 1
    elif named_color == "gainsboro":
        gray_count += 1
    elif named_color == "lemonchiffon":
        yellow_count += 1
    elif named_color == "mediumslateblue":
        purple_count += 1
    elif named_color == "mediumspringgreen":
        green_count += 1
    elif named_color == "mediumturqoise":
        blue_count += 1
    elif named_color == "mediumvioletred":
        pink_count += 1
    elif named_color == "midnightblue":
        blue_count += 1
    elif named_color == "mintcream":
        white_count += 1
    elif named_color == "mistyrose":
        pink_count += 1
    elif named_color == "moccasin":
        yellow_count += 1
    elif named_color == "navajowhite":
        brown_count += 1
    elif named_color == "oldlace":
        white_count += 1
    elif named_color == "olivedrab":
        green_count += 1
    elif named_color == "orangered":
        orange_count += 1
    elif named_color == "orchid":
        purple_count += 1
    elif named_color == "palegoldenrod":
        yellow_count += 1
    elif named_color == "palegreen":
        green_count += 1
    elif named_color == "paleturquoise":
        blue_count += 1
    elif named_color == "palevioletred":
        pink_count += 1
    elif named_color == "papayawhip":
        yellow_count += 1
    elif named_color == "peachpuff":
        brown_count += 1
    elif named_color == "peru":
        brown_count += 1
    elif named_color == "pink":
        pink_count += 1
    elif named_color == "rebeccapurple":
        purple_count += 1
    elif named_color == "rosybrown":
        brown_count += 1
    elif named_color == "royalblue":
        blue_count += 1
    elif named_color == "saddlebrown":
        brown_count += 1
    elif named_color == "salmon":
        pink_count += 1
    elif named_color == "sandybrown":
        orange_count += 1
    elif named_color == "seagreen":
        green_count += 1
    elif named_color == "seashell":
        white_count += 1
    elif named_color == "sienna":
        brown_count += 1
    elif named_color == "skyblue":
        blue_count += 1
    elif named_color == "slateblue":
        blue_count += 1
    elif named_color == "slategray":
        gray_count += 1
    elif named_color == "snow":
        white_count += 1
    elif named_color == "springgreen":
        green_count += 1
    elif named_color == "steelblue":
        blue_count += 1
    elif named_color == "tan":
        brown_count += 1
    elif named_color == "teal":
        green_count += 1
    elif named_color == "thistle":
        purple_count += 1
    elif named_color == "tomato":
        red_count += 1
    elif named_color == "turquoise":
        blue_count += 1
    elif named_color == "violet":
        purple_count += 1
    elif named_color == "wheat":
        brown_count += 1
    elif named_color == "whitesmoke":
        white_count += 1
    elif named_color == "yellowgreen":
        green_count += 1

#Print breakdown function definition
def printBreakdown():
    #Includes the global variables
    global red_count
    global green_count
    global blue_count
    global black_count
    global gray_count
    global purple_count
    global yellow_count
    global orange_count
    global white_count
    global brown_count
    global pink_count

    count_array.append(("Red", red_count))
    count_array.append(("Orange", orange_count))
    count_array.append(("Yellow", yellow_count))
    count_array.append(("Green", green_count))
    count_array.append(("Blue", blue_count))
    count_array.append(("Pink", pink_count))
    count_array.append(("Purple", purple_count))
    count_array.append(("Black", black_count))
    count_array.append(("White", white_count))
    count_array.append(("Brown", brown_count))

    #Prints the color breakdown
    print("COLOR BREAKDOWN:")
    print("Red Count: ", red_count)
    print("Orange Count: ", orange_count)
    print("Yellow Count: ", yellow_count)
    print("Green Count: ", green_count)
    print("Blue Count: ", blue_count)
    print("Pink Count: ", pink_count)
    print("Purple Count: ", purple_count)
    print("Black Count: ", black_count)
    print("White Count: ", white_count)
    print("Brown Count: ", brown_count)

#Average function definition, takes variable range_size
def average(range_size):
    #Includes global variables
    global red_count
    global yellow_count
    global orange_count
    global pink_count
    global purple_count
    global green_count
    global white_count
    global brown_count
    global black_count

    #Determines the percent of each color in the selected range
    red_average = (red_count / range_size) * 100
    orange_average = (orange_count / range_size) * 100
    yellow_average = (yellow_count / range_size) * 100
    pink_average = (pink_count / range_size) * 100
    white_average = (white_count / range_size) * 100
    black_average = (black_count / range_size) * 100
    blue_average = (blue_count / range_size) * 100
    purple_average = (purple_count / range_size) * 100
    brown_average = (brown_count / range_size) * 100
    green_average = (green_count / range_size) * 100

    average_array.append(("Red", red_average))
    average_array.append(("Yellow", yellow_average))
    average_array.append(("Pink", pink_average))
    average_array.append(("White", white_average))
    average_array.append(("Black", black_average))
    average_array.append(("Blue", blue_average))
    average_array.append(("Purple", purple_average))
    average_array.append(("Brown", brown_average))
    average_array.append(("Green", green_average))
    average_array.append(("Orange", orange_average))

    #Prints the percentages
    print("\nCOLOR PERCENTAGE:")
    print("Red: ", round(red_average, 2),"%")
    print("Orange: ", round(orange_average, 2),"%")
    print("Yellow: ", round(yellow_average, 2),"%")
    print("Pink: ", round(pink_average, 2),"%")
    print("White: ", round(white_average, 2),"%")
    print("Black: ", round(black_average, 2),"%")
    print("Blue: ", round(blue_average, 2),"%")
    print("Purple: ", round(purple_average, 2),"%")
    print("Brown: ", round(brown_average, 2),"%")
    print("Green: ", round(green_average, 2), "%")

#Calls the detect_color function
detect_color()
printBreakdown()
average(range_size)
