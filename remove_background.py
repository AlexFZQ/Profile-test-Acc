#!/usr/bin/env python3
"""
Script to remove background from an accordion image
"""

from PIL import Image
import numpy as np
import os

def remove_background(image_path, output_path):
    """
    Remove background from an image using color thresholding
    """
    try:
        # Open the image
        img = Image.open(image_path)
        print(f"Original image size: {img.size}")
        print(f"Original image mode: {img.mode}")
        
        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Get image data
        data = np.array(img)
        red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
        
        # Define background color range (assuming white/light background)
        # You may need to adjust these thresholds based on the actual background
        background_threshold = 200
        
        # Create mask for background pixels
        # This assumes the background is light/white
        background_mask = (
            (red > background_threshold) & 
            (green > background_threshold) & 
            (blue > background_threshold)
        )
        
        # Set alpha channel to 0 for background pixels
        data[background_mask, 3] = 0
        
        # Create result image
        result = Image.fromarray(data, 'RGBA')
        
        # Save the result
        result.save(output_path, 'PNG')
        print(f"Background removed image saved to: {output_path}")
        
        return result
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def main():
    input_image = "c7dabebe6c6230f5574780414b5c1c3b.jpeg"
    output_image = "accordion_no_background.png"
    
    if not os.path.exists(input_image):
        print(f"Input image not found: {input_image}")
        return
    
    print("Removing background from accordion image...")
    result = remove_background(input_image, output_image)
    
    if result:
        print("Background removal completed successfully!")
    else:
        print("Background removal failed.")

if __name__ == "__main__":
    main()