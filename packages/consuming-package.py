
# --- simple way to import a module from a package -----
# import animals.mamals.lion

# animals.mamals.lion.f_lion()

# ----- import with from -------
# from animals.mamals import lion

# lion.f_lion()

# ----- the mamals package has a __init__.py that defines
#   the __all__ list

from animals.mamals import *

human.f_human()
lion.f_lion()

