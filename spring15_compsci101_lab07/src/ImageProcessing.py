'''
Created on Oct 25, 2011
Modified on Oct 31, 2012
Modified on Oct 23, 2014 by Susan Rodger

@author: rcd, alexandrudutu, ola
'''
import Image    # standard python image library


def apply_filter(image, filter):
    '''
    Create and return a NEW image, based on a
    transform of each pixel in the given image using the given filter
    image is an open Image object
    filter is a function to apply to each pixel in image
    return new image, same size, to which filter has been applied to each pixel of image
    '''
    pixels = [ filter(p) for p in image.getdata() ]
    nim = Image.new("RGB",image.size)
    nim.putdata(pixels)
    return nim

def open_image(filename):
    '''
    opens the given image and converts it to RGB format
    returns a default image if the given one cannot be opened
    filename is the name of a PNG, JPG, or GIF image file
    '''
    image = Image.open(filename)
    if image == None:
        print("Specified input file " + filename + " cannot be opened.")
        return Image.new("RGB", (400, 400))
    else:
        print(str(image.size) + " = " + str(len(image.getdata())) + " total pixels.")
        return image.convert("RGB")


'''
During this lab a pixel is a tuple of 3 values (R, G, B)
representing the red, green, and blue components of a color
that each range from [0-255] inclusive. 
The filter functions:
    - take one pixel as an argument,
    - modify the channels of the pixel and
    - return the transformed pixel
'''
def identity(pixel):
    '''
    returns a pixel that is unchanged from the original
    '''
    r,g,b = pixel
    return (r,g,b)
    

def invert(pixel):
    '''
    returns a pixel where every pixel channel is 255 minus its value
    '''
    r,g,b = pixel
    return (255 - r, 255-g, 255-b)

def darken(pixel):
    """
    returns a pixel whose red, green, and blue values are all 90% of those given
    """
    r,g,b = pixel
    return (int(r*.90), int(.90*g), int(.90*b))
    pass
 
def brighten(pixel):
    """
    returns a pixel whose red, green, and blue values are all 110% of those given
    but not over 255 (the maximum value).
    """
    r,g,b = pixel
    newtuple = [int(r*1.10), int(1.10*g), int(1.10*b)]
    for newpixel in newtuple:
        if newpixel > 255:
            newpixel == 255
    return newtuple
    
    pass
    pass
 
def gray_scale(pixel):
    '''
    returns a pixel whose red, green, and blue values are all set to the same value: 
      the average of the original channels 
    '''
    r,g,b = pixel
    average = int((r*g*b)/3)
    return (average, average, average)
    pass

    
def posterize(pixel):
    """
    returns a pixel whose red, green, and blue values are all changed in
    the following way:
     - divide channel's range into 4 equal pieces (i.e., 0-63, 64-127, 128-191, 192-255)
     - set the channel's value to a fixed value within that range (i.e., 50, 100, 150, 200)
    """
    r,g,b = pixel
    newList = [r,g,b]
    for i in range(len(newList)):
        element = newList[i]
        if element > 0 and element < 63:
            element = 50
        if element >= 63 and element < 127:
            element = 100
        if element >= 127 and element < 191:
            element = 150
        if element >= 191 and element <= 255:
            element = 200
        newList[i] = element
    return tuple(newList)
            
    
    pass

def solarize(pixel):
    """
    returns a pixel whose red, green, and blue values are all changed in
    the following way:
     - if the value is less than 128, set it to 255 - the original value.
     - if the value is 128 or greater, don't change it.
    """
    r,g,b = pixel
    newList = [r,g,b]
    for i in range(len(newList)):
        element = newList[i]
        if element < 128:
            element = 255 - element
        newList[i] = element
    return tuple(newList)
    pass

def denoise(pixel):
    '''
    take noise out of a pixel
    '''
    r,b,g = pixel
    return (int(r*10), 0,0)
    
    pass

def denoise2(pixel):
    '''
    take noise out of a pixel
    '''
    r,g,b = pixel
    return (0, int(b*20), int(g*20))
    pass

def denoise3(pixel):
    '''
    take noise out of a pixel
    '''
    r,g,b = pixel
    if r == 255 and g == 0 and b == 0:
        r = 0
    if r == 255 and g == 255 and b == 255:
        r = 0 
        g = 0
        b = 0
    return r,g,b
    pass 

def load_and_go(fname,filterfunc):
    image = open_image(fname)
    nimage = apply_filter(image,filterfunc)
    image.show()
    nimage.show()
    '''
    processedImage.jpg is the name of the file
    the image is saved in. The first time you do 
    this you may have to refresh to see it.
    '''
    nimage.save("processedImage.jpg")


if __name__ == "__main__":
    ''' Change the name of the file and the function
        to apply to the file in the line below
    '''
    input_file = "clue2.bmp"
    load_and_go(input_file, denoise3)

