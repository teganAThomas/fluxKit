import numpy as np
from .athena_mc import Photons

class Screener:
    def inner_radius(self,phots):
        """
        Screen for photons going through inner radial boundary
        """
        mask = np.where((phots.x1 < 5.9))
        return mask

    def outer_radius(self,phots):
        """
        Screen for photons going through outer radial boundary
        """
        mask = np.where((phots.x1 > 6.0))
        return mask
