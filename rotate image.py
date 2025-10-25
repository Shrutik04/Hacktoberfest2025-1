from PIL import Image

# Open the image
try:
    img = Image.open("input_image.jpg")
except FileNotFoundError:
    print("Error: 'input_image.jpg' not found. Please provide a valid image path.")
    exit()

# Rotate the image by a specific angle (e.g., 45 degrees counter-clockwise)
# You can also use expand=True to ensure the entire rotated image is visible,
# even if it requires expanding the canvas.
rotated_img = img.rotate(45, expand=True)

# Save the rotated image
rotated_img.save("rotated_image_pillow.jpg")

print("Image rotated and saved as 'rotated_image_pillow.jpg'")
