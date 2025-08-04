import cv2

while True:
    print('''
          Enter your choise :
          1:For load image
          2:For view image
          3:For view Image Dimensions and colors
          4:For save/Write image
          5:For convert image bgr to gray
          6:For Exit''')
    input_choise=int(input('Selected:'))
    if input_choise==1:
        path_image=input("Enter the path of image:")
        image=cv2.imread(path_image)
        
        if image is not None:
            print('Image loaded succesfully')
        else:
            print('Error:Image not loaded/wrong path')
    elif input_choise==2:
          path_image=input("Enter the path of image:")
          image=cv2.imread(path_image)
        
          if image is not None:
            print('Image loaded succesfully')
            cv2.imshow('your image',image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
          else:
            print('Error:Image not loaded/wrong path')
    elif input_choise==3:
        path_image=input("Enter the path of image:")
        image=cv2.imread(path_image)
        if image is not None:
            print('Image loaded succesfully')
            h,w,c=image.shape
            print('Height is:',h,'\nWidth is:',w,'\nColors are:',c)
        else:
            print('Error:Image not loaded/wrong path')
    elif input_choise==4:
        path_image=input("Enter the path of image:")
        image=cv2.imread(path_image)
        
        if image is not None:
         print('Image loaded successfully')
         path_choise = input("Enter the path to save the image (e.g., saved_image.jpg): ")
         if path_choise:
            cv2.imwrite(path_choise, image)
            print('Image saved successfully.')
         else:
            print('No path provided. Image not saved.')
        else:
            print('Error:Image not loaded/wrong path')
    elif input_choise==5:
        path_image=input("Enter the path of image:")
        image=cv2.imread(path_image)
        if image is not None:
            print('Image loaded successfully')
            gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            cv2.imshow('gray',gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            save_option=int(input("Want to save this gray image press 1 for yes and 0 for No:"))
            if save_option==1:
                path_choise = input("Enter the path to save the image")
                if path_choise is not None:
                    cv2.imwrite(path_choise,gray)
                    print('Save Succesfully')
                else:
                    print('No path provided. Image not saved.')
            elif save_option==0:
                print('Image not saved')
            else:
                print('Invalid option')
            
            
        else:
            print('Error:Image not loaded/wrong path')
    elif input_choise==6:
        print('Danke ! Auf Wiedersehen')
        break
            
        
        
        
        

            
        
        