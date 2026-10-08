import cv2

# load the image
image = cv2.imread("spec_sheet.png")

# check if the image loaded
if image is None:
    print("could not load image")
else:
    print("image loaded successfully")
    print("image size:", image.shape)

    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # save the grayscale image
    cv2.imwrite("grayscale.png", gray)

    print("grayscale image saved")

    # resize the grayscale image to 2x its original size
    upscaled = cv2.resize(
        gray,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    # save the upscaled image
    cv2.imwrite("grayscale_upscaled.png", upscaled)

    print("2x upscaled image saved")

    # apply thresholding to make the text stand out
    _, thresholded = cv2.threshold(
        upscaled,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # save the thresholded image
    cv2.imwrite("thresholded.png", thresholded)

    print("thresholded image saved")