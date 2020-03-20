import numpy;
import cv2;
from PIL import Image, ImageDraw;
import pytesseract;

cap = cv2.VideoCapture('sample2.mp4')
cap.set(cv2.CAP_PROP_POS_FRAMES, 4597)


def printLevelId(frame, context):
    #level Id
    y = 85;
    y_height = 20;
    x = 35;
    x_width = 100;
    context.rectangle((x, y, x + x_width, y + y_height), outline=(255, 0, 0));
    cropped_region_of_interest = frame[y:y + y_height, x:x + x_width];
    text = pytesseract.image_to_string(cropped_region_of_interest);
    print("Level Id: " + text);
    return not text;
#end printLevelId

def printLevelName(frame, context):
    #level Id
    y = 35;
    y_height = 40;
    x = 35;
    x_width = 565;
    context.rectangle((x, y, x + x_width, y + y_height), outline=(255, 0, 0));
    cropped_region_of_interest = frame[y:y + y_height, x:x + x_width];
    text = pytesseract.image_to_string(cropped_region_of_interest);
    print("Level Name: " + text);
    return not text;
#end printLevelId

def printCreatorName(frame, context):
    #level Id
    y = 85;
    y_height = 20;
    x = 435;
    x_width = 95
    context.rectangle((x, y, x + x_width, y + y_height), outline=(255, 0, 0));
    cropped_region_of_interest = frame[y:y + y_height, x:x + x_width];
    text = pytesseract.image_to_string(cropped_region_of_interest);
    print("Creator Name: " + text);
    return not text;
#end printLevelId

while(cap.isOpened()):
    ret, frame = cap.read();
    
    frame = cv2.resize(frame, dsize=(640,360));
   
    #draw functions
    pilImage = Image.fromarray(frame);
    context = ImageDraw.Draw(pilImage);
    
    #convert to b and w for better detection
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    printLevelId(frame, context);
    printLevelName(frame, context);
    printCreatorName(frame, context);


    frame = numpy.array(pilImage);

    cv2.imshow('frame',frame);
    
    if cv2.waitKey(2000) & 0xFF == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();
