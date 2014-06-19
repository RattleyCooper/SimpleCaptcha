SimpleCaptcha
=============

A simple captcha system written in python.  Its aim is to provide an easy to use, non-web-based captcha system.

Quick Examples
==============
    from simplesaptcha import *
    
    sc = SimpleCaptcha('/path/to/base/captcha/image.tiff',
                      )



Options
=======

Any of these options can be passed as keyword arguments when initializing the SimpleCaptcha instance to change the default behaviour.  
Either the font or random_fonts keyword is required.

* save_captcha - True or False - Save the captcha image.  Probably a shitty option unless you really like captchas.

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
