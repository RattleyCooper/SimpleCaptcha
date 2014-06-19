# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Written by Wykleph June, 2014                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

from thread import start_new_thread
from random import randint, choice
import base64
try:
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
except ImportError:
    print 'PIL module was not found.  Aborting.'
    exit()
from textwrap import wrap

class SimpleCaptcha:
    def __init__(self, baseimagepath, **kwargs):
        # Set some strings that can be used for random captchas if desired.
        self.alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.safe_alphanumeric = 'abcdefghijkmnpqrstuvwxyz23456789' # No 1s, 0s, ls or os
        
        self.baseimagepath = baseimagepath
        
        # Unpack kwargs
        if kwargs:
            try:
                self.save_captcha = kwargs['save_captcha']
            except KeyError, TypeError:
                self.save_captcha = False
                
            try:
                self.fnt = kwargs['font']
            except KeyError:
                self.fnt = '/usr/share/fonts/truetype/freefont/FreeSerif.ttf'
                
            try:
                self.font_size = int(kwargs['font_size'])
            except KeyError, ValueError:
                self.font_size = 70
                
            try:
                self.random_fonts = kwargs['random_fonts']
            except KeyError:
                self.random_fonts = False
                
            try:
                self.colored_lines = int(kwargs['colored_lines'])
            except KeyError, ValueError:
                self.colored_lines = 3
            
            try:
                self.colored_line_width = int(kwargs['colored_line_width'])
            except KeyError, ValueError:
                self.colored_line_width = 4
                
            try:
                self.black_lines = int(kwargs['black_lines'])
            except KeyError, ValueError:
                self.black_lines = 0
                
            try:
                self.black_line_width = int(kwargs['black_line_width'])
            except KeyError, ValueError:
                self.black_line_width = 1
            
            try:
                self.white_lines = int(kwargs['white_lines'])
            except KeyError, ValueError:
                self.white_lines = 0
            
            try:
                self.white_line_width = int(kwargs['white_line_width'])
            except KeyError, ValueError:
                self.white_line_width = 2
            
            try:
                self.white_dots = int(kwargs['white_dots'])
            except KeyError, ValueError:
                self.white_dots = 0
                
            try:
                self.image_object = kwargs['image_object']
            except KeyError, TypeError:
                self.image_object = False
            
            try:
                self.image_string = kwargs['image_string']
            except KeyError, TypeError:
                self.image_string = True
                
            try:
                self.letter_mask_size = int(kwargs['letter_mask_size'])
            except KeyError, TypeError:
                self.letter_mask_size = 100
                
            try:
                self.kerning = int(kwargs['kerning'])
            except KeyError, TypeError:
                self.kerning = 50
                
            try:
                self.print_letter_colors = kwargs['print_letter_colors']
            except KeyError:
                self.print_letter_colors = False
                
            try:
                self.y_offset = int(kwargs['y_offset'])
            except KeyError, TypeError:
                self.y_offset = 0
            
        else:
            self.save_captcha = False
            self.font_size = 70
            self.fnt = '/usr/share/fonts/truetype/freefont/FreeSerif.ttf'
            self.random_fonts = False
            self.colored_lines = 3
            self.colored_line_width = 2
            self.black_lines = 0
            self.black_line_width = 1
            self.white_lines = 0
            self.white_line_width = 2
            self.white_dots = 0
            self.image_object = False
            self.image_string = True
            self.letter_mask_size = 100
            self.kerning = 50
            self.y_offset = 0
            self.print_letter_colors = False
    
    def parse_alphanumeric(self):
        for i in range(0, len(self.alphanumeric)):
            l = self.alphanumeric[i]
            
            if self.alphanumeric.count(l) > 1:
                self.alphanumeric = self.alphanumeric.replace(l, self.random_alphanumeric(1), 1)
                self.parse_alphanumeric()
        return
    
    def random_alphanumeric(self, length):
        self.alphanumeric = ''.join(choice(self.safe_alphanumeric) for i in range(0, length))
        
        self.parse_alphanumeric()
                
        return self.alphanumeric
                        
    
    def compare_captcha(self, captcha, answer):
        """Simple function that compares an answer to the given captcha
        string.  You could easily write your own if you want to.  It 
        returns True if the answer matches the captcha string and False
        if it doesn't"""
        
        if answer == captcha:
            return True
        else:
            print 'The answer was False.'
            return False
            
    def showimage(self, image):
        """Function the thread is started on.  This is not the function
        you want to call if you are using SimpleCaptcha from the console.
        Use thread_showimage to start a new thread which will allow the user
        to type."""
        
        image.show()
        print 'image closed'
        return

    def make_captcha_pack(self, imagedata):
        """Takes a PIL image object and turns it into something that can
        be sent with the socket module."""
        mode, size, imgstring = imagedata
        imgx, imgy = size
        imgx, imgy = str(imgx), str(imgy)
        imgpack = ' '.join([mode, imgx, imgy, base64.b64encode(imgstring)])
        return imgpack
    
    def unpack(self, imagepack):
        """Takes data generated with the image_pack function and recompiles
        it into a PIL image object."""
        options = imagepack.split()
        mode, imgx, imgy = options[:3]
        imgstring = ' '.join(options[3:])
        size = int(imgx), int(imgy)
        return Image.fromstring(mode, size, base64.b64decode(imgstring))
        
    def thread_showimage(self, image):
        """Call this function to display an PIL Image object.  You should
        construct the image using something like:
        image = Image.fromstring(mode, size, imgstring)"""
        
        x = 'dummy'
        thread.start_new_thread(self.showimage, (image,))

    def reconstruct(self, captchadata):
        """Returns a PIL image object by reconstructing the data returned 
        by the get_random_captcha function.  Once the image is reconstructed
        you can use thread_showimage(image) to display the image."""
        
        # Separate captcha string from image data
        try:
            captcha, imagedata = captchadata
        except ValueError:
            print 'Incorect data.  Check the help for clarification.'
            return False
            
        # Grab data we need to reconstruct the image
        try:
            mode, size, imageobj = imagedata
        except ValueError:
            print 'Incorect data.  Check the help for clarification.'
            return False
        except TypeError:
            pass
        
        # Reconstruct the image and return PIL object
        if self.image_string:
            return Image.fromstring(mode, size, imageobj)
        elif self.image_object:
            return imagedata
    
    def approved_colors(self, filepath):
        """Returns a list of tuples containing approved colors in RGB
        format.  The list is taken from a file that the user specifies. 
        Each line in the file should have 1 color"""
        acolors = []
        with open(filepath, 'r') as f:
            for line in f:
                line = line.rstrip()
                
                if line != '':
                    tline = tuple(i for i in line if i.isdigit())
                    acolors.append(tline)
                    
            f.close()
            return acolors
    
    def create_captcha(self, text):
        """Generates a captcha and stores the image data in a tuple.  The
        tuple looks like this:
        
        (mode, size, imgstr), where size is also a tuple containing x, y 
        coordinates.  Look at the reconstruct_imagedata function for
        clarification.
        
        The image is actually converted to a string so it can be sent 
        over a socket and reconstruct it on the other end.  
        
        NOTE: Base64 may be needed to send images over a socket since PIL 
        image objects contain \\s in them when they are represented as 
        strings."""
        
        # Get text and make sure it's a string
        text = str(text)
        
        # Open background image to draw on
        img = Image.open(self.baseimagepath)
        draw = ImageDraw.Draw(img)

        imgsize = img.size
        
        # Decide what to do with fonts
        if not self.random_fonts:
            # Set font
            font = ImageFont.truetype(self.fnt, self.font_size)
        else:
            font = ImageFont.truetype(self.random_fonts[randint(0,len(self.random_fonts)-1)], 
                                    self.font_size)
                                    
        if self.colored_lines > 0:
            # Draw random colored lines
            for i in range(0, self.colored_lines):
                ImageDraw.Draw(img).line((randint(1, imgsize[0]), randint(1, imgsize[1]), randint(1,imgsize[0]), randint(1, imgsize[1])), 
                                        fill=(randint(0,255), randint(0,255), randint(0, 255)),
                                        width=self.colored_line_width)
                                        
        if self.black_lines > 0:
            # Draw random black lines
            for i in range(0, self.black_lines):
                ImageDraw.Draw(img).line((randint(1, imgsize[0]), randint(1, imgsize[1]), randint(1,imgsize[0]), randint(1, imgsize[1])), 
                                        fill='black',width=self.black_line_width)
        
        if self.white_dots > 0:
            # Draw random white points
            for i in range(0, self.white_dots):
                draw.point((randint(1, imgsize[0]), randint(1, imgsize[1]), randint(1,imgsize[0]), randint(1, imgsize[1])), 
                                        fill='white')
        if self.white_lines > 0:
            # Draw random white lines
            for i in range(0, self.white_lines):
                ImageDraw.Draw(img).line((randint(1, imgsize[0]), randint(1, imgsize[1]), randint(1,imgsize[0]), randint(1, imgsize[1])), 
                                        fill='white',width=self.white_line_width)                                                                   
        
        # Draw text on to new image
        x = 0
        lms = self.letter_mask_size
        
        # Draw each character individually
        for char in text:
            textimg = Image.new('RGBA', (lms, lms), (0, 0, 0))
            tmpdraw = ImageDraw.Draw(textimg)
            
            # Draw char with random color
            color = (randint(0,255), randint(0,255), randint(0,255))
            tmpdraw.text((15,0), char, color, font=font)
            
            if self.print_letter_colors:
                print char, color
                            
            # Rotate text
            textimg = textimg.rotate(randint(-25, 25))

            # Make image mask
            mask = Image.new('L', (lms, lms), 0)     
            mask.paste(textimg,(0,0))
        
            # Paste text image with mask, on to the main image.
            img.paste(textimg, (x,self.y_offset), mask)
            
            # Adjust letter spacing
            x += self.kerning
        
        # Save image if specified
        if self.save_captcha:
            img.save('captcha/pics/%s.tiff' % ''.join(choice(self.alphanumeric) for i in range(12)))
        
        # Check to see if the user wants the image object, or the image
        # string and associated data needed for reconstruction.           
        if self.image_object:
            # Return PIL image object
            return img
        elif self.image_string:
            # Compile data that is needed to re-construct the image
            imgdata = img.mode, imgsize, img.tostring()
            return imgdata


    def get_captcha(self, captcha):
        """Gets a random captcha and returns the text that is used in the 
        captcha, for comparison purposes, along with the image data that
        is needed to reconstruct the captcha image.  Look at the create_captcha
        help section for clarification on this."""
        
        imgdata = self.create_captcha(captcha)
        captchadata = captcha, imgdata
        return captchadata
