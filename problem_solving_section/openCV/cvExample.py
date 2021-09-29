import cv2 as cv


def test_openCV_Func():
    image_1 = cv.imread('imageA.jpg', 1)
    assert (image_1-image_1).all
    cv.imshow('original', image_1)
    cv.waitKey(1)
    cv.destroyAllWindows()


if __name__ == "__main__":
    test_openCV_Func()
