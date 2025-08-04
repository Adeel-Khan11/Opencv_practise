import cv2

# C:\\Users\\khan\\Downloads\\Compressed\\G\\mytest.png

img = None
process_img = None

def load_image(path):
    if not path:
        print("Path is empty!")
        return None
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Failed to load—check your path!")
    else:
        print("Image loaded successfully!")
    return image

def edge_canny(image, low_thresh, high_thresh):
    if image is None:
        print("Load the image first!")
        return None
    edges = cv2.Canny(image, low_thresh, high_thresh)
    cv2.imshow("Original", image)
    cv2.imshow("Edges", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Use option 9 to save the processed image.")
    return edges

def thresh_hold_binary(image, thresh_val, max_val):
    if image is None:
        print("Load the image first!")
        return None
    ret, thresh_img = cv2.threshold(image, thresh_val, max_val, cv2.THRESH_BINARY)
    cv2.imshow("Original image", image)
    cv2.imshow("Thresholded image", thresh_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("Use option 9 to save the processed image.")
    return thresh_img

def save_image(image, path):
    if not path:
        print("No path to save!")
        return
    if image is None:
        print("No image to save!")
        return
    success = cv2.imwrite(path, image)
    print("Image saved successfully!" if success else "Save failed!")

while True:
    print("""
    1: Load image
    2: Edge detection (Canny)
    3: Threshold binary
    9: Save processed image
    0: Exit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        p = input("Enter the path of image: ")
        img = load_image(p)

    elif choice == '2':
        if img is not None:
            low_input = input("Enter lower threshold for Canny: ")
            high_input = input("Enter upper threshold for Canny: ")
            if not low_input.isdigit() or not high_input.isdigit():
                print("Please enter valid integer values.")
            else:
                low = int(low_input)
                high = int(high_input)
                process_img = edge_canny(img, low, high)
        else:
            print("Load the image first!")

    elif choice == '3':
        if img is not None:
            t_input = input("Enter threshold value (0–255): ")
            m_input = input("Enter maximum value (0–255): ")
            if not t_input.isdigit() or not m_input.isdigit():
                print("Please enter valid integer values.")
            else:
                thresh_val = int(t_input)
                max_val = int(m_input)
                process_img = thresh_hold_binary(img, thresh_val, max_val)
        else:
            print("Load the image first!")

    elif choice == '9':
        save_path = input("Enter the path and file name to save: ")
        save_image(process_img, save_path)

    elif choice == '0':
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
