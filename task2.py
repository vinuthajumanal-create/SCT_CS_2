from PIL import Image

def swap_pixels(img):
    width, height = img.size
    pixels = img.load()

    for x in range(width // 2):
        for y in range(height):
            # Swap left and right pixels
            pixels[x, y], pixels[width - x - 1, y] = pixels[width - x - 1, y], pixels[x, y]

    return img

def apply_shift(img, key):
    width, height = img.size
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Modify pixel values using key
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    return img

def reverse_shift(img, key):
    width, height = img.size
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    return img

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)

    img = swap_pixels(img)       # Step 1: Pixel swapping
    img = apply_shift(img, key)  # Step 2: Apply shift

    img.save(output_path)
    print("🔐 Image Encrypted Successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)

    img = reverse_shift(img, key)  # Step 1: Reverse shift
    img = swap_pixels(img)         # Step 2: Swap back pixels

    img.save(output_path)
    print("🔓 Image Decrypted Successfully!")

print("=== Image Encryption Tool ===")

choice = input("Enter 'encrypt' or 'decrypt': ").lower()
input_path = input("Enter input image path: ")
output_path = input("Enter output image path: ")
key = int(input("Enter key (0-255): "))

if choice == "encrypt":
    encrypt_image(input_path, output_path, key)

elif choice == "decrypt":
    decrypt_image(input_path, output_path, key)

else:
    print("❌ Invalid choice!")
