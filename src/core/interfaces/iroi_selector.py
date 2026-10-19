from abc import ABC, abstractmethod

import numpy as np

from core.entities.roi import ROI


class IROISelector(ABC):

    @abstractmethod
    def __call__(self, src: np.ndarray, *args, **kwargs) -> ROI:
        pass