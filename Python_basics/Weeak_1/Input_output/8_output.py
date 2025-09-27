# ANSI color codes
class Colors:
    RESET = '\033[0m'
    END = RESET
    BOLD = '\033[1m'

    # Standard colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright variants
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Aliases and additional names used in examples
    ORANGE = BRIGHT_YELLOW
    PURPLE = MAGENTA
    PINK = BRIGHT_MAGENTA
    BROWN = YELLOW
    GREY = '\033[90m'
    LIGHT_BLUE = BRIGHT_BLUE
    LIGHT_GREEN = BRIGHT_GREEN
    LIGHT_CYAN = BRIGHT_CYAN
    LIGHT_RED = BRIGHT_RED
    LIGHT_YELLOW = BRIGHT_YELLOW
    LIGHT_PURPLE = BRIGHT_MAGENTA
    LIGHT_GREY = BRIGHT_WHITE
    DARK_BLUE = BLUE
    DARK_GREEN = GREEN
    DARK_CYAN = CYAN
    DARK_RED = RED
    DARK_YELLOW = YELLOW
    DARK_PURPLE = MAGENTA

# Colored output examples
print(f"{Colors.RED}Error: Something went wrong!{Colors.END}")
print(f"{Colors.GREEN}Success: Operation completed!{Colors.END}")
print(f"{Colors.BOLD}{Colors.BLUE}Important message{Colors.END}")
print(f"{Colors.YELLOW}Warning: Check your input!{Colors.END}")
print(f"{Colors.MAGENTA}Info: This is a colored message.{Colors.END}")
print(f"{Colors.CYAN}Note: This is a note.{Colors.END}")
print(f"{Colors.WHITE}Regular message in white.{Colors.END}")
print(f"{Colors.BOLD}Bold text example.{Colors.END}")
print(f"{Colors.RED}Red text example.{Colors.END}")
print(f"{Colors.GREEN}Green text example.{Colors.END}")
print(f"{Colors.BLUE}Blue text example.{Colors.END}")
print(f"{Colors.YELLOW}Yellow text example.{Colors.END}")
print(f"{Colors.MAGENTA}Magenta text example.{Colors.END}")
print(f"{Colors.CYAN}Cyan text example.{Colors.END}")

# Additional color examples — use getattr so names must match class attributes above
_examples = [
    "ORANGE", "PURPLE", "PINK", "BROWN", "GREY",
    "LIGHT_BLUE", "LIGHT_GREEN", "LIGHT_CYAN", "LIGHT_RED",
    "LIGHT_YELLOW", "LIGHT_PURPLE", "LIGHT_GREY",
    "DARK_BLUE", "DARK_GREEN", "DARK_CYAN", "DARK_RED"
]

for name in _examples:
    color = getattr(Colors, name)
    print(f"{color}{name.replace('_', ' ').title()} text example{Colors.END}")