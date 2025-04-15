import os
import cv2
import numpy as np
from pathlib import Path

def blur_faces(input_folder, output_folder):
    """
    Process all images in the input folder, detect faces, blur them with a circular mask,
    and save the result to the output folder.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output directory: {output_folder}")

    # Load the face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Get all image files from the input folder
    valid_extensions = ['.jpg', '.jpeg', '.png']
    image_files = [f for f in os.listdir(input_folder) 
                  if any(f.lower().endswith(ext) for ext in valid_extensions)]
    
    if not image_files:
        print(f"No images found in {input_folder}")
        return
    
    print(f"Found {len(image_files)} images to process.")
    
    # Process each image
    for img_file in image_files:
        try:
            input_path = os.path.join(input_folder, img_file)
            output_path = os.path.join(output_folder, img_file)
            
            # Read the image
            img = cv2.imread(input_path)
            if img is None:
                print(f"Failed to read image: {img_file}")
                continue
                
            # Convert to grayscale for face detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            # Create a copy of the image for blurring
            blurred_img = cv2.GaussianBlur(img, (99, 99), 30)
            
            # If faces are detected, apply circular blur
            if len(faces) > 0:
                for (x, y, w, h) in faces:
                    # Create a mask for circular blurring
                    mask = np.zeros(img.shape[:2], dtype=np.uint8)
                    
                    # Calculate center and radius for the circle
                    center_x = x + w // 2
                    center_y = y + h // 2
                    
                    # Use the larger dimension for radius to ensure full face coverage
                    radius = max(w, h) // 2
                    
                    # Increase radius to ensure full face coverage (adjust as needed)
                    radius = int(radius * 1.2)
                    
                    # Draw the circle on the mask
                    cv2.circle(mask, (center_x, center_y), radius, 255, -1)
                    
                    # Create a 3-channel mask
                    mask_3d = np.stack([mask, mask, mask], axis=2) / 255.0
                    
                    # Blend the original and blurred images
                    img = (blurred_img * mask_3d + img * (1.0 - mask_3d)).astype(np.uint8)
                
                # Save the processed image
                cv2.imwrite(output_path, img)
                print(f"Processed {img_file} - {len(faces)} face(s) blurred with circular mask")
            else:
                # If no faces detected, just copy the original image
                cv2.imwrite(output_path, img)
                print(f"No faces detected in {img_file}")
                
        except Exception as e:
            print(f"Error processing {img_file}: {str(e)}")

if __name__ == "__main__":
    input_folder = "Dress"
    output_folder = "blur_image"
    
    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist!")
    else:
        blur_faces(input_folder, output_folder)
        print("Processing complete!")