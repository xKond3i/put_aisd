# Config Variables

# ! NOTICE: executable file containing whole configuration is not a good idea,
# !         but it's just for a class project purposes only
# TODO - use `configparser` and `config.ini` file

# * Definitions
class Config():
    """
    Program Config
    """
    DEFAULT_N: int = 10
    N_MIN: int = 1
    N_MAX: int = 48
    RND_RNG_MIN: int = 1
    RND_RNG_MAX: int = 99
    REPEAT_CHOICES: bool = False
