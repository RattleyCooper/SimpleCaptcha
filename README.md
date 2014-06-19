SimpleCaptcha
=============

A simple captcha system written in python.  Its aim is to provide an easy to use, non-web-based captcha system.  The images can be generated and embeded into GUI applications, or shown while in a command line interface.

Quick Examples
==============

**Server-side:**


    # Set up SimpleCaptcha and get a random captcha.
    
    from simplesaptcha import *
    
    # The base image must be given as the first argument.
    # Either the random_fonts or font keyword arguments
    # are required as well.
    
    baseimage = '/path/to/base/captcha/image.tiff'
    randfonts = ['/path/to/font.ttf', '/path/to/font.ttf']
    
    sc = SimpleCaptcha(baseimage,
                        colored_lines=4,
                        colored_line_width=5,
                        random_fonts=randfonts)
    
    # Create SimpleCaptcha instance with required options.
    
    sc = SimpleCaptcha(baseimg, random_fonts=randfonts)
    
    # Generate a captcha image and get the answer to the 
    # captcha for comparison purposes.
    
    answer, imagedata = sc.get_captcha(sc.random_alphanumeric(4))
    
    # Create a captcha package that can be sent to the 
    # client.
    
    captcha_pack = sc.make_captcha_pack(imagedata)
    
    # Once the client sends their answer back, compare it
    # to the answer that was generated with the captcha.
    
    solved = sc.compare_captcha(answer, given_answer)

    # solved will equal True or False.  You could easily
    # compare them without this added function.
    
    # After comparing the results, the server can decide
    # what to do with the connection.

    
**Client-side:**


    # After receiving image data, we un-pack it,
    # display the image and ask for input from the 
    # user.
    
    from simplecaptcha import *
    from PIL import Image
    
    # Initiate the SimpleCaptcha instance with dummy data.
    # It does not generate captchas so it doesn't need a
    # base image or any fonts.
    
    sc = SimpleCaptcha('dummy')
    
    # The data you receive on the client-side needs to be
    # unpacked and then displayed.
    
    img = sc.unpack(imagedata)
    img.show()
    userinput = raw_input('Answer: ')
    
    # Then send the input back to the server.

Options
=======

Any of these options can be passed as keyword arguments when initializing the SimpleCaptcha instance to change the default behaviour.  
**Either the font or random_fonts keyword argument is required on the server end.**

* save_captcha - True or False - Save the captcha image for debug purposes.

* font - /path/to/font.ttf - This is a required keyword argument.

* font_size - integer - Sets the font size.

* random_fonts - [/paths/to/font.ttf] - List of paths/to/fonts.ttf so that the fonts used in the captcha are random.

* colored_lines - integer - The amount of colored lines in the image.

* colored_line_width - integer - The width of colored lines in the image.

* black_lines - integer - The amount of black lines in the image.

* black_line_width - integer - The width of black lines in the image.

* white_lines - integer - The amount of white lines in the image.

* white_line_width - integer - The width of white lines in the image

* white_dots - integer - the amount of white dots in the image.

* image_object - True or False - Returns a PIL image object instead of a string representation.

* image_string - True of False - True by default, but will return a string representation of the image.

* letter_mask_size - integer - This needs to be adjusted when changing font sizes.

* print_letter_colors - True or False - Used if you want to see the RGB value of the letter colors.

* y_offset - integer - Used when the letters aren't centered in the image on the y axis.

* kerning - integer - The amount of space between letters in pixels.
