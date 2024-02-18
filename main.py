import os
from PIL import Image

#Replace 'crop' with 'resize' depending on usage
action = 'crop'

def resize_image(input_image_path, output_image_path, side_length):
    with Image.open(input_image_path) as image:
        max_side = max(image.size)
        new_size = (max_side, max_side)
        
        resized_image = image.resize(new_size)
        resized_image.save(output_image_path)

def crop_image(input_image_path, output_image_path, side_length):
    with Image.open(input_image_path) as image:
        width, height = image.size
        if width > height:
            left = (width - height) / 2
            top = 0
            right = (width + height) / 2
            bottom = height
        else:
            left = 0
            top = (height - width) / 2
            right = width
            bottom = (height + width) / 2
        
        crop_rectangle = (left, top, right, bottom)
        cropped_image = image.crop(crop_rectangle)
        
        if side_length is not None:
            cropped_image = cropped_image.resize((side_length, side_length))
        
        cropped_image.save(output_image_path)

image_folder = './input'
output_folder = './results'


for filename in os.listdir(image_folder):
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
        file_path = os.path.join(image_folder, filename)
        output_path = os.path.join(output_folder, f"resized_{filename}") 

        if action == 'crop':
            crop_image(file_path, output_path, None)  
            print(f"Cropped {filename} and saved as {output_path}")
        elif action == 'resize':
            resize_image(file_path, output_path, None) 
            print(f"Resized {filename} and saved as {output_path}")
        else:
            print("Please enter a valid option")