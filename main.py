from PIL import Image

print("Welcome To Image Manipulation S/W")
print("You have two options to select from:")
print("Press 1 for black and white image")
print("Press 2 to Add colored filters")
choice = int(input("Enter Your Choice: "))
print("Please Enter Image Path")
path = input()

if(choice == 1):
    image_file = Image.open(path)  # Opens Original Image
    image_file = image_file.convert('1') #Converts Image to black and white
    image_file.save('black and white image.png')
    print("your image is generated. Thank you for using the S/W")

if(choice == 2):
    im = Image.open(path)
    print("Enter Color Choice Press 1.For Red 2.For Green and 3.For Blue")
    colorChoice = int(input())

    if(colorChoice == 1):
        color = "red"
    elif(colorChoice == 2):
        color = "green"
    else:
        color = "blue"

    layer = Image.new('RGB', im.size, color)
    output = Image.blend(im, layer, 0.5)
    output.save('colored Output.png', 'PNG')

    print("your image is generated. Thank you for using the S/W")
