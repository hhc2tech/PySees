
try:
    import opensees as _ops
except ImportError:
    print("PySees: cannot import OpenSeesPy.",
          "Make sure it's available in sys.path and compiled correctly.")
    raise

from pysees.core import *
import pysees.uniaxialMaterial
