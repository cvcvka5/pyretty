"""
    pyretty -> Easy, pretty print.
    
    This is to make your coloring and formatting easier for the terminal.
    Instead of manually formatting the string you can just insert it in a function.
    The function will automatically open and close the color.
"""

from colorama import Fore, Style


# Custom color
def c(text: str, color: str) -> str:
    return f"{color}{text}{Style.RESET_ALL}"

# Info
def i(text: str, logtext: (str or None) = None) -> str:
    """Formats string to an info string.

    Args:
        text (str): The string that follows up the brackets.
        logtext (str or None): The string portion in the brackets.

    Returns:
        str: The formatted string.
    """
    second = Fore.BLUE
    main = Fore.CYAN
    return  f"[{c(logtext, second)}] {c(text, main)}" if (logtext != None) else c(text, main)
# Warning
def w(text: str, logtext: (str or None) = None) -> str:
    """Formats string to an warning string.

    Args:
        text (str): The string that follows up the brackets.
        logtext (str or None): The string portion in the brackets.

    Returns:
        str: The formatted string.
    """
    second = Fore.RED
    main = Fore.YELLOW
    return  f"[{c(logtext, second)}] {c(text, main)}" if (logtext != None) else c(text, main)
# Error
def e(text: str, logtext: (str or None) = None) -> str:
    """Formats string to an error string.

    Args:
        text (str): The string that follows up the brackets.
        logtext (str or None): The string portion in the brackets.

    Returns:
        str: The formatted string.
    """
    second = Fore.MAGENTA
    main = Fore.RED
    return  f"[{c(logtext, second)}] {c(text, main)}" if (logtext != None) else c(text, main)
# Sucess
def s(text: str, logtext: (str or None) = None) -> str:
    """Formats string to an sucess string.

    Args:
        text (str): The string that follows up the brackets.
        logtext (str or None): The string portion in the brackets.

    Returns:
        str: The formatted string.
    """
    second = Fore.LIGHTGREEN_EX
    main = Fore.GREEN
    return  f"[{c(logtext, second)}] {c(text, main)}" if (logtext != None) else c(text, main)