# MM2LevelId
Simple Test of the OCR in Python with Google Tesseract. Needed an excuse to play around with the OCR library and 
used Mario Maker 2 streamers videos to detect Level Id, Creator Name, and Level Names uses regions and Google Tesseract.
Not a very useful utility as it stands but is a simple example of how to user OCR with defined regions. 

Note, very important to convert to b&w otherwise the OCR isn't that good. Would be a good exercise to do additional transformations
on the image to get better OCR quality. This is good enough for the learning I was interested. 

Also, interesting, read: annoying, python images are merely arrays so converting between B&W and Color actually breaks the code for
drawing with color overlays. 

Windows Install for Google Tesseract (Required installation)
https://github.com/UB-Mannheim/tesseract/wiki

Then pip install pytesseract

Also, add installation directory to your path (before running your notebook if you are using notebook). 

Linux Users, well probably don't have this issue. 
