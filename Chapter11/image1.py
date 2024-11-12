from PIL import Image
image = Image.new('RGB', (640, 480), (255, 255, 0)) #0, 100, 255
image.save('yellow.png')