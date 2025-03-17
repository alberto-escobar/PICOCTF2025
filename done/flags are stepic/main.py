import stepic
from PIL import Image

# Open the encoded image
encoded_img = Image.open("upz.png")

# Decode the hidden message
decoded_msg = stepic.decode(encoded_img)
print("Hidden Message:", decoded_msg)
