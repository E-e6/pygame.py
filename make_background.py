from PIL import Image, ImageDraw

# Create background
img = Image.new("RGB", (1600, 600), color="skyblue")
draw = ImageDraw.Draw(img)

# Add green hills
draw.rectangle([0, 400, 1600, 600], fill="forestgreen")

img.save("vista_background.jpg")
print("✅ Created vista_background.jpg")