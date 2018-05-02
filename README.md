# pyOcrWrapper
## Use tesseract, gocr, ocrad or cuneiform on opencv images with this wrapper for python.
A very small wrapper to call ocr software on opencv images.
gocr, ocrad and cuneiform executables are needed in your path(if you want to use them).

## Test
```Original text: "joy of data"
pytesseract: joy of data, took 1.39073300362s for 10 runs
gocr: Joy or data, took 0.241178035736s for 10 runs
ocrad: joy or data, took 0.14460682869s for 10 runs
cuneiform: joy of data, took 0.853563070297s for 10 runs
```
