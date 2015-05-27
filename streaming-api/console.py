from __future__ import print_function

termcolors = {
    "bold": "\033[1m",
    "red":  "\033[31m",
    "blue": "\033[94m",
    "reset": "\033[0m"
}

def colorize(msg, color="red"):
    """ print the message using color on the console """
    colorcode = termcolors[color]
    resetcode = termcolors["reset"]
    return "".join((colorcode, msg, resetcode))

def hilight(msg, substring, color="bold"):
    """ print the message with the substring hilighted """
    before, substring, after = msg.partition(substring)
    return "".join((before, colorize(substring, color), after))

if __name__ == "__main__":
    print("In this sentence the word {} should be printed in red.".format( colorize("test", "red") ))
    print(hilight("In this sentence the word test should be hilighted.", "test"))
    print(hilight("In this sentence the word test should be printed in blue.", "test", "blue"))
