import cv2
# C:\\Users\\khan\\Downloads\\Compressed\\G\\mytest.png
image=None

while True:
    print('''
          Enter your choise :
          1:For load image
          2:For view image
          3:For resized image
          4:For crop image
          5:For Rotation
          6:For flip image
          10:For exit
         ''')
    input_choise=int(input('Selected:'))
    if input_choise==1:
        path_image=input("Enter the path of image:")
        image=cv2.imread(path_image)
        
        if image is not None:
            print('Image loaded succesfully')
        else:
            print('Error:Image not loaded/wrong path')
    elif input_choise ==2:
        if image is not None:
            cv2.imshow('My image',image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    elif input_choise==3:
        if image is not None:
            width=int(input("Enter the width of image:"))
            height=int(input("Enter the height of image:"))
            resized=cv2.resize(image,(width,height))
            cv2.imshow('origianl image',image)
            
            cv2.imshow('resized image',resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            path_choise = input("Enter the path to save the image (e.g., saved_image.jpg): ")
            if path_choise:
              cv2.imwrite(path_choise, resized)
              print('Image saved successfully.')
            else:
             print('No path provided. Image not saved.')
    elif input_choise==4:
        if image is not None:
            cropped=image[150:200,300:350]
            cv2.imshow('Cropped image',cropped)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            path_choise = input("Enter the path to save the image (e.g., saved_image.jpg): ")
            if path_choise:
              cv2.imwrite(path_choise, cropped)
              print('Image saved successfully.')
            else:
             print('No path provided. Image not saved.')
            
        else:
            print('Error:Image not loaded')
            
    elif input_choise==5:
        if image is not None:
            h,w=image.shape[:2]
            center=(w//2,h//2)
            M=cv2.getRotationMatrix2D(center,-90,2.0)
            rotated_image=cv2.warpAffine(image,M,(w,h))
            cv2.imshow('Original image',image)
            cv2.imshow('Rotated image',rotated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            path_choise = input("Enter the path to save the image (e.g., saved_image.jpg): ")
            if path_choise:
              cv2.imwrite(path_choise, rotated_image)
              print('Image saved successfully.')
            else:
             print('No path provided. Image not saved.')
    elif input_choise==6:
        if image is not None:
            horizontal_flip=cv2.flip(image,1)
            vertical_flip=cv2.flip(image,0)
            both_flip=cv2.flip(image,-1)
            cv2.imshow('Origianl image',image)
            cv2.imshow('Horizonatl flip',horizontal_flip)
            cv2.imshow('vertical_flip',vertical_flip)
            cv2.imshow('both_flip',both_flip)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            path_choise = input("Enter the path to save the image (e.g., saved_image.jpg) for example we will save both_flip (only one image): ")
            if path_choise:
              cv2.imwrite(path_choise, both_flip)
              print('Image saved successfully.')
            else:
             print('No path provided. Image not saved.')
            
            
    elif input_choise==10:
        print('Danke ,Auf Widersehen !')
        break
            
    else:
            print('Load the image first !')
    
        