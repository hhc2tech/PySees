
import opensees as _ops
from pysees.core import _ndm, _ndf

def Elastic(matTag, E, eta=0.0, Eneg=None):
    """Elastic uniaxial material."""
    matTag = int(matTag)
    E = float(E)
    eta = float(eta)

    if Eneg is not None:
        Eneg = float(Eneg)
    else:
        Eneg = E
    
    _ops.uniaxialMaterial('Elastic', matTag, E, eta, Eneg)


def ElasticPP(matTag, E, eps_yP, eps_yN=None, eps0=0.0):
    """Elastic-perfectly-plastic uniaxial material."""
    matTag = int(matTag)
    E = float(E)
    eps_yP = float(eps_yP)
    
    if eps_yN is not None:
        eps_yN = float(eps_yN)
    else:
        eps_yN = eps_yP

    eps0 = float(eps0)

    _ops.uniaxialMaterial('ElasticPP', matTag, E, eps_yP, eps_yN, eps0)


def ElasticPPGap(matTag, E, Fy, gap, eta=0.0, damage=False):
    """Elastic-perfectly-plastic uniaxial material with gap."""
    matTag = int(matTag)
    E = float(E)
    Fy = float(Fy)
    gap = float(gap)
    eta = float(eta)

    if damage:
        damage = 'damage'
    else:
        damage = 'noDamage'

    _ops.uniaxialMaterial('ElasticPPGap', matTag, E, Fy, gap, eta, damage)


