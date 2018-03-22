"""Core module for PySees. Contains functions intended for the pysees
   namespace, as well as globals describing the current state of the model to
   the rest of the module."""

import opensees as _ops

_ndm = None
_ndf = None


def model(builder='basic', ndm=None, ndf=None):
    """Create a new OpenSees model.

    Input arguments:
        builder = The builder to use. Only 'basic' is currently supported.
        ndm     = number of dimensions (1-3)
        ndf     = number of degrees of freedom per node (1-6)
    """
    global _ndm, _ndf

    #--------- Process builder ---------#
    if builder.lower() == 'basic' or builder.lower() == 'basicbuilder':
        builder = 'basic'
    else:
        raise ValueError('Builder not supported: {}'.format(builder))

    #----------- Process ndm -----------#
    if ndm is None:
        raise ValueError('ndm required')
    else:
        ndm = int(ndm)

    #----------- Process ndf -----------#
    # OpenSees default ndfs:
    if ndf == None:
        if ndm == 1:
            ndf = 1
        elif ndm == 2:
            ndf = 3
        elif ndm == 3:
            ndf = 6
        else:
            raise ValueError('ndm must be between 1 and 3')
    else:
        ndf = int(ndf)
        if ndm == 1:
            if ndf != 1:
                raise ValueError('ndf must == 1 for ndm == 1')
        elif ndm == 2:
            if ndf not in range(1, 4):
                raise ValueError('ndf must be between 1 and 3 for ndm == 2')
        elif ndm == 3:
            if ndf not in range(1, 7):
                raise ValueError('ndf must be between 1 and 6 for ndm == 3')

    _ndm = ndm
    _ndf = ndf
    _ops.model(builder, '-ndm', ndm, '-ndf', ndf)


def node(nodeTag, coords, mass=None):
    """Create a new node in the model."""

    nodeTag = int(nodeTag)

    if len(coords) != _ndm:
        raise ValueError("node must have ndm coordinate values")
    else:
        for i in range(0, _ndm):
            coords[i] = float(coords[i])

    if mass is not None:
        if len(mass) != _ndf:
            raise ValueError("mass must have ndf mass values")
        else:
            for i in range(0, _ndf):
                mass[i] = float(mass[i])
    else:
        mass = [0.0]*_ndf

    _ops.node(nodeTag, *coords, '-mass', *mass)


def mass(nodeTag, mass):
    """Set the mass of an existing node."""

    nodeTag = int(nodeTag)

    if mass is not None:
        if len(mass) != _ndf:
            raise ValueError("mass must have ndf mass values")
        else:
            for i in range(0, _ndf):
                mass[i] = float(mass[i])
    else:
        mass = [0.0]*_ndf

    _ops.mass(nodeTag, *mass)
