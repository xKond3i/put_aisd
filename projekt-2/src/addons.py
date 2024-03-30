# Additional Definitions

# * Modules
from config import Config

import random
# ! NOTICE: `argparse` could be used to benefit argument parsing,
# !         but for class project purposes I'll keep it simple
# TODO - use `argparse`
from sys import argv

# * Definitions
def get_arg(CONFIG: Config) -> int:
    """Get Program's first positional argument value `n` (random list size)"""
    DFLT_FB_MSG = f'random list size fallback to default: {CONFIG.DEFAULT_N}' # DEFAULT FALLBACK MESSAGE
    ERR_OOR_MSG = f'random list size of out range [{CONFIG.N_MIN}, {CONFIG.N_MAX}]' # ERROR OUT OF RANGE MESSAGE
    SET_MSG     = 'random list size has been set to: {n}'

    # No positional argument detected
    if (len(argv) < 2):
        print(DFLT_FB_MSG)
        return CONFIG.DEFAULT_N
    
    # Try to parse the positional random list size argument
    try:
        n: int = int(argv[1])
        if n < CONFIG.N_MIN or n > CONFIG.N_MAX:
            raise Exception(ERR_OOR_MSG)
    except Exception as e:
        print(e)
        print(DFLT_FB_MSG)
        return CONFIG.DEFAULT_N
    else:
        print(SET_MSG.format(n = n))
        return n

def gen_numbers(n: int, CONFIG: Config) -> list[int]:
    """Generate n-sized list of random numbers based on Config"""
    if CONFIG.REPEAT_CHOICES:
        return random.choices(range(CONFIG.RND_RNG_MIN, CONFIG.RND_RNG_MAX), k = n) # repeating random numbers
    return random.sample(range(CONFIG.RND_RNG_MIN, CONFIG.RND_RNG_MAX), n) # non-repeating random numbers

# --- VISUAL PURPOSES ONLY --- #

def header() -> None:
    """Print Header"""
    print(f'{FT.TITLE}Poznań University of Technology 🎓{FT.RESET}')
    print(f'{FT.SUBTITLE}Algorithms and Data Structures{FT.RESET}')
    print(f'Exercise {FT.NUM}#2{FT.RESET} — Complex Data Structures')
    print(f'Executed by {FT.AUTHOR_THEME}@ Konrad Ceglarski{FT.RESET}\n')

def point(mark: str) -> None:
    """Prints formatted bullet point"""
    print(f'\n{FT.BOLD}({mark}){FT.RESET}')

class FT:
    """Formatting"""
    TITLE = '\033[1;34m'
    SUBTITLE = BOLD = '\033[1m'
    NUM = '\033[36m'
    AUTHOR_THEME = '\033[38;2;106;87;203m'
    BOX = '\033[30;47m'
    RESET = '\033[0m'

NOT_IMPLEMENTED = Exception("NOT IMPLEMENTED")
