import cv2
import cv2 as cv
import numpy as np

from core.entities.roi import ROI
from core.interfaces.iroi_selector import IROISelector


class ROISelector(IROISelector):
    """
    A class to select the ROI on the image.

    src: cv2 image
    selector = ROISelector()
    roi = selector(src)
    """
    WINDOW_NAME = "ROI Selector"
    START_X: int = 0
    START_Y: int = 0
    CURRENT_X: int = 0
    CURRENT_Y: int = 0
    IS_DRAWING: bool = False
    COLOR: tuple[int, int, int] = (150, 225, 150)
    THICKNESS: int = 2
    OVERLAY: np.ndarray = None

    def __draw_rectangle(self, event, x, y, flags, param) -> None:
        """
        Internal function for drawing a rectangle on the image.
        Allow drawing in different ways: from top to bottom, from left to right,
        from bottom to top and from right to left.

        Args:
            event (cv2 event): cv2 event object
            x (int): x coordinate
            y (int): y coordinate
            flags (cv2 flags): cv2 flags object
            param: cv2 params object
        """
        self.CURRENT_X, self.CURRENT_Y = x, y

        if event == cv.EVENT_LBUTTONDOWN:
            self.START_X, self.START_Y = 0, 0
            self.CURRENT_X, self.CURRENT_Y = 0, 0
            self.IS_DRAWING = True
            self.START_X, self.START_Y = x, y
        elif event == cv.EVENT_MOUSEMOVE and self.IS_DRAWING:
            self.OVERLAY = param.copy()
            cv.rectangle(
                img=self.OVERLAY,
                pt1=(self.START_X, self.START_Y),
                pt2=(x, y),
                color=self.COLOR,
                thickness=self.THICKNESS,
            )
        elif event == cv.EVENT_LBUTTONUP:
            self.IS_DRAWING = False
            cv.rectangle(
                img=self.OVERLAY,
                pt1=(self.START_X, self.START_Y),
                pt2=(x, y),
                color=self.COLOR,
                thickness=self.THICKNESS,
            )


    def __call__(self, src: np.ndarray, *args, **kwargs) -> ROI:
        """
        Args:
            src: cv2 image
        Returns:
            ROI: ROI object with the selected ROI x, y, w, h values
        """

        self.OVERLAY = src.copy()
        cv.namedWindow(self.WINDOW_NAME)
        cv.setMouseCallback(self.WINDOW_NAME, self.__draw_rectangle, src)

        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            cv.imshow(self.WINDOW_NAME, self.OVERLAY)

        cv.destroyAllWindows()

        roi_x = min(self.START_X, self.CURRENT_X)
        roi_y = min(self.START_Y, self.CURRENT_Y)

        roi_w = abs(self.START_X - self.CURRENT_X)
        roi_h = abs(self.START_Y - self.CURRENT_Y)

        return ROI(roi_x, roi_y, roi_w, roi_h)

