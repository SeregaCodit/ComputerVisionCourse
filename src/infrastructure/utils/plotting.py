import cv2
import numpy as np
import matplotlib.pyplot as plt

def subplot(channels: dict[str, np.ndarray], cmap: str | None = None) -> None:

    for i, k in enumerate(channels):
        plt.subplot(1, len(channels), i+1)
        plt.title(k)
        plt.imshow(channels[k], cmap=cmap)


def draw_points(src: np.ndarray, points: np.ndarray, color=(255, 0, 0)):
    src = src.copy()

    if points.dtype != np.int64:
        points = points.astype(np.int64)

    for i in range(points.shape[0]):
        cv2.circle(src, points[i], 3, color, -1)
        cv2.putText(src,
                    f"p_{i}",
                    (points[i, 0] + 10, points[i, 1]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

    return src