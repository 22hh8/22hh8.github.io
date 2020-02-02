#!/usr/bin/env python3
# (c) 2018 hailey han
"""This file contains image Filters I have designed:
TargetFilter, RedFilter,RotateFilter, LighterFilter, and DarkerFilter
"""

from PIL import Image
from filter import *

class TargetFilter(PlainFilter):
    """ This will only keep pixels that are close to a target color while
    the rest of the image turns white."""
    __slots__ = ['target']
    def __init__(self, base,targetC=Color((.2,.3,.8))): # setting target color
        """Initialize filter based on an image or other filter."""
        # call the PlainFilter initializer
        self.target = targetC # creating a target slot
        super().__init__(base) 
    def after(self,x,y):
        """Pixel color after filtering."""
        (r,g,b) = self.before(x,y).rgb()
        (r1,g1,b1) = self.target.rgb()
        distance=((r1-r)**2+(g1-g)**2+(b1-b)**2)**.5  # set distance eq
        if distance<=.5: #if within distance
            return Color( (r,g,b) )
        else:
            return Color( (1,1,1) ) #turn white

class RedFilter(PlainFilter):
    """ Makes Van Gogh's Bedroom painting more red. """
    
    def __init__(self, base):
        """Initialize filter based on an image or other filter."""
        # call the PlainFilter initializer
        super().__init__(base) 

    def after(self,x,y):
        """Pixel color after filtering."""
        (r,g,b) = self.before(x,y).rgb()
        if r > 0 and b > .25: # setting a min to blue helps to make it purple
            r += .2
        c = Color( ((r+1)/2,g,b) )
        return c


class LighterFilter(PlainFilter):
    """ This makes an image lighter overall. """
    
    def __init__(self, base):
        """Initialize filter based on an image or other filter."""
        # call the PlainFilter initializer
        super().__init__(base) 

    def after(self,x,y):
        """Pixel color becomes whiter after filtering."""
        (r,g,b) = self.before(x,y).rgb()
        r += 1 # mix with white rgb
        g += 1
        b += 1
        c = Color( (r/2,g/2,b/2) )
        return c
    
class RotateFilter(PlainFilter):
    """ Make red green and green blue and blue red """
    
    def __init__(self, base):
        """Initialize filter based on an image or other filter."""
        # call the PlainFilter initializer
        super().__init__(base) 

    def after(self,x,y):
        """The new Pixel color after filtering."""
        (h,s,v) = self.before(x,y).hsv()
        if x >= self.width/2:
            h = (h+120)%360
        c = Color( (h,s,v), model='hsv' )
        return c

class DarkerFilter(PlainFilter):
    """ This makes an image darker overall."""
    
    def __init__(self, base):
        """Initialize filter based on an image or other filter."""
        # call the PlainFilter initializer
        super().__init__(base) 

    def after(self,x,y):
        """Pixel color after filtering."""
        (r,g,b) = self.before(x,y).rgb()
        c = Color( (r/2,g/2,b/2) ) # make it darker, closer to 0
        return c

if __name__ == '__main__':
    # In this section of code, you should demonstrate how your
    # filters work.
    bedroom = Image.open('images/Bedroom.png')
    result = DarkerFilter(bedroom)
    result.image().save('DarkerBedroom.png')


