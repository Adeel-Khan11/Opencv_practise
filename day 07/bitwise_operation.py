import cv2
import numpy as np

# C:\\Users\\khan\\Desktop\\cv2_practise\\1.jpg


image=None
process_image=None

    
    
def save_image(image, path):
    if not path:
        print("No path to save!")
        return
    if image is None:
        print("No image to save!")
        return
    success = cv2.imwrite(path, image)
    print("Image saved successfully!" if success else "Save failed!")

def OR_bitwise(img1,img2):
    if img1 is not None and img2 is not None:

     bitwise_or=cv2.bitwise_or(img1,img2)
     cv2.imshow('original image 1',img1)
     cv2.imshow('original image 2',img2)
     cv2.imshow('OR image',bitwise_or)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     print('Want to save this OR_Bitwise image use option 0 !')
     return bitwise_or
    else:
        print('No image to process')


def AND_bitwise(img1,img2):
    if img1 is not None and img2 is not None:
     bitwise_and=cv2.bitwise_and(img1,img2)
     cv2.imshow('original image 1',img1)
     cv2.imshow('original image 2',img2)
     cv2.imshow('AND image',bitwise_and)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     print('Want to save this AND_Bitwise image use option 0 !')
     return bitwise_and
    else:
        print('No image to process')


def NOT_bitwise(img1):
    if img1 is not None:
     bitwise_not=cv2.bitwise_not(img1)
     cv2.imshow('original image 1',img1)
     cv2.imshow('NOT image',bitwise_not)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     print('Want to save this NOT_Bitwise image use option 0 !')
     return bitwise_not
    else:
        print('No image to process')


img1=np.zeros((300,300),dtype='uint8')
img2=np.zeros((300,300),dtype='uint8')

cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2,(100,100),(250,250),255,-1)


while True:
    print('''
          0:For save Image
          1:For OR Bitwise
          2:For AND Bitwise
          3:For NOT Bitwise
          9:For Exit''')
    choice=int(input('Enter your choice:'))
    if choice == 0:
     if process_image is not None:
        input_path = input('Enter the file path and name to save: ')
        cv2.imwrite(input_path, process_image)
        print("Image saved successfully!")
     else:
        print('No image to save')

        
    elif choice==1:
        print('OR Bitwise')
        process_image=OR_bitwise(img1,img2)
        
    elif choice==2:
        print('AND Bitwise')
        process_image=AND_bitwise(img1,img2)
    elif choice==3:
        print('NOT Bitwise')
        process_image=NOT_bitwise(img1)
    elif choice==9:
        print("Thanks For Using !")
        break
    else:
        print('Invalid choice')
    
        
    