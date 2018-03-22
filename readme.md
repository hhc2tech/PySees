# ♓ PySees: a wrapper for the OpenSeesPy interpreter

The implementation of a more generic interpreter system for OpenSees and the
subsequent port to Python has been very welcome, however actual use of the
functions can be frustrating, as the functions are a (relatively) bare
interface to the underlying C++ code. A short list of missing functionality:

- Duck typing / safe type conversion
- Support for numpy/scipy datatypes (e.g. `np.float64`)
- Docstrings

Other things that have frustrated/irritated me in particular:

- Excessive use of strings: the original commands were written with Tcl's
  "everything is a string" model in mind, and thus many commands have
  options along the line of ("-ndm", ndm); the number of quotes can be
  substantially reduced by using namespaces and keyword arguments.
- No list passing for arguments (must be expanded)

This package seeks to provide a thin layer between the compiled commands and
the user, allowing for easier use of the system.

## Simple truss example

OpenSeesPy:

```Python
import opensees as ops
ops.model('basic', '-ndm', 2, '-ndf', 2)
ops.node(0, 0.0, 0.0)
ops.node(1, 0.0, 1.0, '-mass', 1.0, 1.0)
ops.uniaxialMaterial('Elastic', 0, 29000.0)
ops.element('truss', 0, 0, 1, 10.0, '-doRayleigh', True)
```

PySees:

```Python
import pysees as ps
ps.model(ndm=2, ndf=2)
ps.node(0, [0, 0])
ps.node(1, [0, 1], mass=[1, 1])
ps.uniaxialMaterial.Elastic(0, 29000)
ps.element.truss(0, 0, 1, 10, 0, doRayleigh=True)
```
