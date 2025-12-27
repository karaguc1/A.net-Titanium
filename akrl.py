import colorama
def red(value):
    print(colorama.Fore.RED + f"{value}" + colorama.Fore.RESET)
def blue(value):
    print(colorama.Fore.BLUE + f"{value}" + colorama.Fore.RESET)
def green(value):
    print(colorama.Fore.GREEN + f"{value}" + colorama.Fore.RESET)
def yellow(value):
    print(colorama.Fore.YELLOW + f"{value}" + colorama.Fore.RESET)
def cyan(value):
    print(colorama.Fore.CYAN + f"{value}" + colorama.Fore.RESET)
def lred(value):
    print(colorama.Fore.LIGHTRED_EX + f"{value}" + colorama.Fore.RESET)
def lblue(value):
    print(colorama.Fore.LIGHTBLUE_EX + f"{value}" + colorama.Fore.RESET)
def lgreen(value):
    print(colorama.Fore.LIGHTGREEN_EX + f"{value}" + colorama.Fore.RESET)
def lyellow(value):
    print(colorama.Fore.LIGHTYELLOW_EX + f"{value}" + colorama.Fore.RESET)
def lcyan(value):
    print(colorama.Fore.CYAN + f"{value}" + colorama.Fore.RESET)
def test():
    red("red")
    blue("blue")
    green("green")
    yellow("yellow")
    cyan("cyan")
    lred("light red")
    lblue("light blue")
    lgreen("light green")
    lyellow("light yellow")
    lcyan("light cyan")

