# Additional Definitions

# * Variables
K_MIN: int = 3
K: int = 10
MAX_RND: int = 100_000

# * Modules
import random

# * Definitions
def ask_for_mode() -> list[int]:
    """Handling input as stated in the task description"""
    # Program powinien obsługiwać następujące dane wejściowe: n-elementowy ciąg liczb naturalnych wczytywany z klawiatury (n<=10), ciąg liczb naturalnych generowany przez generator danych będący częścią programu.
    dataset: list[int] = []
    ans: str = input('do you want to manually type in the numbers? [y/n] ')
    match ans.upper():
        case 'Y':
            dataset = provide_dataset()
        case 'N':
            print(f'generating random dataset (range: {MAX_RND:,}; k: {K})...')
            dataset = gen_ds_rnd(K)
        case _:
            print(f'{FT.ERR}err: unknown answer{FT.RESET}\nfallback: generating random dataset (range: {MAX_RND:,}; k: {K})...')
            dataset = random.sample(range(MAX_RND), k = K)
    return dataset

def provide_dataset() -> list[int]:
    dataset: list[int] = []
    ans: str = input(f'enter n ({K_MIN}-{K}) numbers separated by a space that will serve as the dataset: ')
    for idx, word in enumerate(ans.split()):
        if len(dataset) >= K:
            break
        try:
            num: int = int(word)
        except Exception as e:
            print(f'{FT.ERR}err: trouble converting \'{word}\' to int...{FT.RESET}')
        else:
            dataset.append(num)
    if len(dataset) < 3:
        print(f'{FT.ERR}err: provided dataset is too short{FT.RESET}\ngenerating additional {K_MIN - len(dataset)} number(s)...')
        dataset.extend(random.sample(range(MAX_RND), k = K_MIN - len(dataset)))
    return dataset

def gen_ds_rnd(n: int = 100, max_rnd: int = MAX_RND) -> list[int]:
    """Generate n-sized Random Dataset"""
    return random.sample(range(max_rnd), k = n)

def gen_ds_asc(n: int = 100) -> list[int]:
    """Generate n-sized Ascending Dataset"""
    return list(range(1, n+1))

def gen_ds_desc(n: int = 100) -> list[int]:
    """Generate n-sized Descenging Dataset"""
    return list(range(n, 0, -1))

def gen_ds_as(n: int = 100) -> list[int]:
    """Generate n-sized A-Shaped Dataset"""
    front: list[int] = []
    back: list[int] = []
    for idx, x in enumerate(range(1, n+1)):
        if idx % 2 == 0: front.append(x)
        else: back.insert(0, x)
    return front + back
    # return [*list(range(1, n+1, 2)), *list(range(n, 0, -2))] # <- not working as intended :(

def gen_ds_vs(n: int = 100) -> list[int]:
    """Generate n-sized V-Shaped Dataset"""
    front: list[int] = []
    back: list[int] = []
    for idx, x in enumerate(range(n, 0, -1)):
        if idx % 2 == 1: front.append(x)
        else: back.insert(0, x)
    return front + back

# --- VISUAL PURPOSES ONLY --- #

def header() -> None:
    """Print Header"""
    print(f'{FT.TITLE}Poznań University of Technology 🎓{FT.RESET}')
    print(f'{FT.SUBTITLE}Algorithms and Data Structures{FT.RESET}')
    print(f'Exercise {FT.NUM}#1{FT.RESET} — Sorting Algorithms')
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
    ERR = '\033[31m'
