from rapidocr_onnxruntime import RapidOCR

# create the OCR object
ocr = RapidOCR()

# run OCR on the thresholded image
result, _ = ocr("thresholded.png")

# save the detected text
with open("ocr_thresholded.txt", "w", encoding="utf-8") as file:
    for line in result:
        file.write(line[1] + "\n")

print("thresholded OCR results saved")