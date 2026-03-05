#!/usr/bin/env python3
"""
Simple script to remove background from an accordion image
"""

from PIL import Image
import os

def remove_background_simple(image_path, output_path):
    """
    Remove background from an image using simple thresholding
    """
    try:
        # Open the image
        img = Image.open(image_path)
        print(f"Original image size: {img.size}")
        print(f"Original image mode: {img.mode}")
        
        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Get pixel data
        pixels = img.load()
        width, height = img.size
        
        # Process each pixel
        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                
                # If the pixel is mostly white/light, make it transparent
                # Adjust the threshold as needed (200 is quite bright)
                if r > 200 and g > 200 and b > 200:
                    pixels[x, y] = (r, g, b, 0)  # Set alpha to 0 for transparency
        
        # Save the result
        img.save(output_path, 'PNG')
        print(f"Background removed image saved to: {output_path}")
        
        return True
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

def main():
    input_image = "c7dabebe6c6230f5574780414b5c1c3b.jpeg"
    output_image = "accordion_no_background.png"
    
    if not os.path.exists(input_image):
        print(f"Input image not found: {input_image}")
        return
    
    print("Removing background from accordion image...")
    success = remove_background_simple(input_image, output_image)
    
    if success:
        print("Background removal completed successfully!")
    else:
        print("Background removal failed.")

if __name__ == "__main__":
    main()