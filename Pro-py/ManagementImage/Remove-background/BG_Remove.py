
from rembg import remove
from PIL import Image

input_path = "Compression-Image/Remove-background/bus.png"
# input_path = "Esan.png"  
output_path = "output.png"
input = Image.open(input_path)

output = remove(input)
output.save(output_path)
