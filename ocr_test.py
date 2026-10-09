
from rapidocr_onnxruntime import RapidOCR

# create the OCR object
ocr = RapidOCR()

# images to test and their output text files
tests = [
    ("spec_sheet.png", "ocr_original.txt"),
    ("grayscale_upscaled.png", "ocr_upscaled.txt"),
    ("grayscale_3x.png", "ocr_3x.txt"),
    ("thresholded.png", "ocr_thresholded.txt"),
    ("contrast_adjusted.png", "ocr_contrast.txt"),
    ("thresholded_3x.png", "ocr_thresholded_3x.txt"),
]

# run OCR on each image
for image_path, output_path in tests:
    print("testing:", image_path)

    result, _ = ocr(image_path)

    # save the detected text
    with open(output_path, "w", encoding="utf-8") as file:
        if result:
            for line in result:
                file.write(line[1] + "\n")

    print("saved:", output_path)

print("all OCR tests completed")