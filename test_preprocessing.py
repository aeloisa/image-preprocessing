
import cv2

# load the original image
image = cv2.imread("spec_sheet.png")

# check if the image loaded
if image is None:
    print("could not load image")
else:
    print("image loaded successfully")
    print("image size:", image.shape)

    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale.png", gray)
    print("grayscale image saved")

    # resize the grayscale image to 2x its original size
    upscaled = cv2.resize(
        gray, None, fx=2, fy=2,
        interpolation=cv2.INTER_CUBIC
    )
    cv2.imwrite("grayscale_upscaled.png", upscaled)
    print("2x upscaled image saved")

    # resize the grayscale image to 3x its original size
    upscaled_3x = cv2.resize(
        gray, None, fx=3, fy=3,
        interpolation=cv2.INTER_CUBIC
    )
    cv2.imwrite("grayscale_3x.png", upscaled_3x)
    print("3x upscaled image saved")

    
    # apply thresholding to the 3x upscaled image
    _, thresholded_3x = cv2.threshold(
        upscaled_3x,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # save the 3x thresholded image
    cv2.imwrite("thresholded_3x.png", thresholded_3x)

    print("3x thresholded image saved")

    # apply thresholding to the 2x image
    _, thresholded = cv2.threshold(
        upscaled, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )
    cv2.imwrite("thresholded.png", thresholded)
    print("thresholded image saved")

    # apply mild contrast adjustment to the 2x image
    contrast_adjusted = cv2.convertScaleAbs(
        upscaled, alpha=1.15, beta=0
    )
    cv2.imwrite("contrast_adjusted.png", contrast_adjusted)
    print("contrast-adjusted image saved")