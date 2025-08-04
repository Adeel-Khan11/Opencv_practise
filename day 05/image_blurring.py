import cv2
import numpy as np

# C:\\Users\\khan\\Downloads\\Compressed\\G\\mytest.png


def load_image(path):
    if path:
        img = cv2.imread(path)
        if img is None:
            print("Failed to load—check your path!")
        else:
            print("Image loaded successfully!")
        return img
    else:
        print("Path is empty!")
        return None

def save_image(img):
    path_input = input("Enter the path to save the image: ")
    if path_input:
        success = cv2.imwrite(path_input, img)
        print("Image saved successfully!" if success else "Save failed!")
    else:
        print("Path is empty!")

def gaussian_blur(img):
    if img is not None:
        return cv2.GaussianBlur(img, (7,7), 5)
    else:
        print("No image loaded to blur.")
        return None
def median_blur(img):
    if img is not None:
        return cv2.medianBlur(img,15)
    else:
        print("No image loaded to blur.")
        return None

def sharpening_image(img):
    if img is not None:
        sharp_kernal=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        sharp_image=cv2.filter2D(img,-1,sharp_kernal)
        return sharp_image
    else:
        print("No image loaded to sharpen.")
        return None
    


img = None
blurred_image = None
sharp_image=None


while True:
    choice = input("""
Enter your choice:
  0: Load image
  1: Gaussian Blur
  2: Median Blur
  3: Sharpening Image
  5: Save image
  6: Exit
""")
    if choice == "0":
        path = input("Enter image path: ")
        img = load_image(path)
    elif choice == "1":
        if img is not None:
            blurred_image = gaussian_blur(img)
            if blurred_image is not None:
                cv2.imshow("Blurred Image", blurred_image)
                cv2.imshow("Original Image", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        else:
            print("No image loaded.")

    elif choice=='2':
        if img is not None:
            blurred_image = median_blur(img)
            if blurred_image is not None:
                cv2.imshow("Median_Blurred Image", blurred_image)
                cv2.imshow("Original Image", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        else:
            print("No image loaded.")
    elif choice=='3':
        if img is not None:
            sharp_image=sharpening_image(img)
            if sharp_image is not None:
             cv2.imshow("sharpening  Image", sharp_image)
             cv2.imshow("Original Image", img)
             cv2.waitKey(0)
             cv2.destroyAllWindows()
        
        else:
            print("No image loaded.")
            
    elif choice == "5":
        if blurred_image is not None:
            save_image(blurred_image)
        elif sharp_image is not None:
            save_image(sharp_image)
        else:
            print("Nothing to save—no blurred image available.")     
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
