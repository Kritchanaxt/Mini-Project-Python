
from PIL import Image
import os

def Image_Pdf(filenames, output):
    images = []
    for file in filenames:
        if os.path.exists(file):  
            im = Image.open(file)
            im = im.convert('RGB')  
            images.append(im)
        else:
            print(f"File not found: {file}")  
    
    if images:  
        images[0].save(output, save_all=True, append_images=images[1:])
        print(f"PDF created successfully: {output}")
    else:
        print("No valid images to convert.")


# Image_Pdf(['Convert/Convert-ImageToPDF/baseketball.jpeg', 
#            'Convert/Convert-ImageToPDF/Jordan.jpeg', 
#            'Convert/Convert-ImageToPDF/Leborn.jpeg'], 'output1.pdf')

Image_Pdf(['Esan.txt', 
           'Esan.png'], 'output1.pdf')