import numpy as np
import matplotlib.pyplot as plt

def subplot(channels: dict[str, np.ndarray], cmap: str | None = None) -> None:

    for i, k in enumerate(channels):
        plt.subplot(1, len(channels), i+1)
        plt.title(k)
        plt.imshow(channels[k], cmap=cmap)