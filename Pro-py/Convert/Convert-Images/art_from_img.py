
import pywhatkit

pywhatkit.image_to_ascii_art('Convert/Convert-images/dog.png', 'MyArt')
# pywhatkit.image_to_ascii_art('output.png', 'MyArt')

read_file = open("MyArt.txt", "r")
print(read_file.read())


