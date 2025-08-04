import cv2
import numpy as np

# C:\\Users\\khan\\Downloads\\Compressed\\E\\any.jpg
# C:\\Users\\khan\\Desktop\\cv2_practise\\khan.



def image_load(path):
    if not path:
        print("Please enter a valid image path")
        return None
    image = cv2.imread(path)
    if image is None:
        print("Failed to load—check your path!")
    else:
        print("Image loaded successfully!")
    return image

def contour_func(image):
    if image is None:
        print("No image provided for contouring.")
        return [], None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    drawing = image.copy()
    cv2.drawContours(drawing, contours, -1, (0, 255, 0), 3)
    cv2.imshow('Contours', drawing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return contours, hierarchy


def shap_detection(image, contours):
    for cont in contours:
        peri = cv2.arcLength(cont, True)
        approx = cv2.approxPolyDP(cont, 0.01 * peri, True)
        v = len(approx)
        if v == 3:
            shape = 'Triangle'
        elif v == 4:
            shape = 'Rectangle'
        elif v > 5:
            shape = 'Circle'
        else:
            shape = 'None'

        cv2.drawContours(image, [approx], -1, (0,255,0), 2)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 10
        cv2.putText(image, shape, (x, y),
                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0), 2)

    print("The shapes detected on the image.")
    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image


def save_image(image, path):
    if not path:
        print("No path to save!")
        return
    if image is None:
        print("No image to save!")
        return
    success = cv2.imwrite(path, image)
    print("Image saved successfully!" if success else "Save failed!")

    
image = None
contours = None

while True:
    print('''
          0: For save image
          1: For load image
          2: For draw contours
          3: For shape detection
          4: For exit
    ''')
    choice = int(input("Enter your choice: "))
    if choice == 0:
        path = input("Enter the path to save the image: ")
        save_image(image, path)
    elif choice == 1:
        path = input("Enter the path to the image: ")
        image = image_load(path)
    elif choice == 2:
        contours, hierarchy = contour_func(image)
    elif choice == 3:
        if contours is None:
            print("First draw contours (option 2) before shape detection.")
        else:
            image = shap_detection(image, contours)
    elif choice == 4:
        print('Thanks For Using !')
        break
    else:
        print("Invalid choice. Please choose a valid option.")