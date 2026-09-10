import cv2
from matplotlib import pyplot as plt
from core.entities.constants import Paths as p


img_path = p.IMAGE_ASSETS / "cat1.png"
img = cv2.imread(img_path)

plt.figure()
plt.imshow(img)
plt.show()
