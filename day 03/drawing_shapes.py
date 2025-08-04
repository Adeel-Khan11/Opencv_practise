import cv2

# C:\\Users\\khan\\Downloads\\Compressed\\G\\mytest.png

def save_image(img):
    choise = int(input('Do you want to save image 1 for yes and 0 for No :'))
    if choise==1:
        input_path=input('Enter the Image destination name to save:')
        if input_path:
         cv2.imwrite(input_path, img)
         print("Image save Succesfully !")
        else:
            print("Please enter the destination name to save the image")
    elif choise==0:
        print("Image did not save !")
    else:
        print("Your choise is not valid")
        save_image(img)

def load_image(path_img):
    img = cv2.imread(path_img)
    if img is not None:
        print(" Image loaded successfully!")
        return img
    else:
        print(" Error: Image not loaded / Wrong path")
        return None

def draw_line(img):
    pt1_input = input("Enter starting point (x1,y1): ")
    pt2_input = input("Enter ending point (x2,y2): ")
    color_input = input("Enter line color (B,G,R): ")
    thickness = int(input("Enter line thickness: "))

    pt1 = tuple(map(int, pt1_input.split(',')))
    pt2 = tuple(map(int, pt2_input.split(',')))
    color = tuple(map(int, color_input.split(',')))

    line_image = cv2.line(img.copy(), pt1, pt2, color, thickness)
    cv2.imshow('line image', line_image)
    cv2.imshow('Origianl image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return line_image

def draw_rectangle(img):
    pt1_input = input("Enter top-left corner (x1,y1): ")
    pt2_input = input("Enter bottom-right corner (x2,y2): ")
    color_input = input("Enter rectangle color (B,G,R): ")
    thickness = int(input("Enter rectangle thickness: "))

    pt1 = tuple(map(int, pt1_input.split(',')))
    pt2 = tuple(map(int, pt2_input.split(',')))
    color = tuple(map(int, color_input.split(',')))

    rec_image = cv2.rectangle(img.copy(), pt1, pt2, color, thickness)
    cv2.imshow('rectangle image', rec_image)
    cv2.imshow('Original Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return rec_image

def draw_circle(img):
    center_input = input("Enter center of circle (x,y): ")
    radius = int(input("Enter radius: "))
    color_input = input("Enter circle color (B,G,R): ")
    thickness = int(input("Enter circle thickness: "))

    center = tuple(map(int, center_input.split(',')))
    color = tuple(map(int, color_input.split(',')))

    circle_img = cv2.circle(img.copy(), center, radius, color, thickness)
    cv2.imshow('circle image', circle_img)
    cv2.imshow('Original image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return circle_img

def write_text(img):
    text = input("Enter your text: ")
    xy_input = input("Enter position to put text (x,y): ")
    color_input = input("Enter text color (B,G,R): ")
    thickness = int(input("Enter text thickness: "))
    font_scale = float(input("Enter font scale: "))

    xy = tuple(map(int, xy_input.split(',')))
    color = tuple(map(int, color_input.split(',')))
    font = cv2.FONT_HERSHEY_SIMPLEX

    text_image = cv2.putText(img.copy(), text, xy, font, font_scale, color, thickness)
    cv2.imshow('Text image', text_image)
    cv2.imshow('Original image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return text_image

image = None

while True:
    print('''Enter your choice
      0: For load image
      1: For drawing line
      2: For drawing rectangle
      3: For drawing circle
      4: For Text on image
      5: For exit''')

    choice = int(input("Enter your choice: "))

    if choice == 0:
        path_img = input("Enter the path of an image: ")
        image = load_image(path_img)

    elif choice == 1:
        if image is not None:
            line_image = draw_line(image)
            save_image(line_image)
        else:
            print("Please load an image first (choice 0).")

    elif choice == 2:
        if image is not None:
            rec_image = draw_rectangle(image)
            save_image(rec_image)
        else:
            print("Please load an image first (choice 0).")

    elif choice == 3:
        if image is not None:
            circle_image = draw_circle(image)
            save_image(circle_image)
        else:
            print("Please load an image first (choice 0).")

    elif choice == 4:
        if image is not None:
            text_image = write_text(image)
            save_image(text_image)
        else:
            print("Please load an image first (choice 0).")

    elif choice == 5:
        print("viesel Danke ,Auf Wiedersehen")
        break

    else:
        print("Invalid choice")
