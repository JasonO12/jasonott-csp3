import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
AMOGUS_COLOR = u"\u001B[31m\u001B[2D"
NON_COLOR = u"\u001B[0m\u001B[2D"

# print ship with colors and leading spaces


def pattern_print(position):
    print(ANSI_HOME_CURSOR)
    sp = " " * position
    print(AMOGUS_COLOR)
    print(sp + "    .-----.   ")
    print(sp + "  /|    ___|  ")
    print(sp + " | |   (____) ")
    print(sp + " | |       |  ")
    print(sp + "  \|       |  ")
    print(sp + "   |  .-.  |  ")
    print(sp + "   |  | |  |  ")
    print(sp + "   |__| |__|  ")
    print(NON_COLOR)

  
# Pattern function, interface into this file
def patternfunc():

    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    # loop purpose is to animate candle moving
    for position in range(start, distance, step):
        pattern_print(position)  # call to function with parameter
        time.sleep(.1)

if __name__ == "__main__":
  patternfunc()