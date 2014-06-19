SimpleCaptcha
=============

A simple captcha system written in python.  Its aim is to provide an easy to use, non-web-based captcha system.

Options
=======

Any of these options can be passed when initializing the SimpleCaptcha instance to change the default behaviour.

* save_captcha - True or False

* font - /path/to/font.ttf

* font_size - integer

* random_fonts - [/paths/to/font.ttf]

* colored_lines - integer

* colored_line_width - integer

* black_lines - integer

* black_line_width - integer

* white_lines - integer
* white_line_width - integer
* white_dots - integer
* image_object - True or False - Returns a PIL image object instead of a string representation.
* image_string - True of False - True by default, but will return a string representation of the image.
* letter_mask_size - integer - this needs to be adjusted when changing font sizes.
* print_letter_colors - True or False - used if you want to see the RGB value of the letter colors.
* y_offset - integer - used when the letters aren't centered in the image on the y axis.
* kerning - integer - the amount of space between letters in pixels.
