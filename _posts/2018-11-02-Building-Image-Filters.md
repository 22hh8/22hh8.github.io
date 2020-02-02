# How to Use Python to Transform Images

### RGB Colorspace
Colors are the result of mixing the three colored lights: red, green, and blue. The intensities of these colors can be represented by an integer between 0 and 1 where 0 is no light and 1 is full light. 

Colors will be represented by 3-tuples such as (r,g,b) of integers between 0 and 1. Black would be (0,0,0) as no colored light is reflected where as white is (1,1,1). All shades of gray will have equal amounts of red, green, and blue.

### HSV Colorspace
Colors can also be represented in the HSV colorspace which is amixture of hue, saturation, and value. 

The hue is a degree of angles where 0 is red, 120 is green, and 240 is blue. For other colors, pick a degree between the primary colors so that the known hue values can be mixed. For example, yellow would be 60 degrees, right between red and green. 

The saturation is a value between 0 and 1 that represents what % of the hue color you keep, then filling it with white. The greater the saturation, the darker the color.

Then, take a % of the saturated color to top it off with black paint. As the value gets closer to 0, the final color will be darker. 

### Classes Needed to Transform Images

The Color object allows the colors to be represented by either RGB or HSV. There are components within the Color class that allows individual color components to come out with methods red(), green(), blue(), hue(), saturation(), and value().

The Filter classes are objects that are used to transform the pixels of an image. I have provided a LighterFilter, DarkerFilter, TargetFilter, and RedFilter. 

The python code is provided below:

[Color Classes](http://22hh8.github.io/filter.py)
[Filter Classes](http://22hh8.github.io/lab7.py)

# Filter Results

### LighterFilter and DarkerFilter

The LighterFilter brings all the RGB values closer to white and the DarkerFilter brings all the RGB values closer to black. 

This is the original image of Van Gogh's *Bedroom*.
![Original Image](/img/Bedroom.png)

This is the image after the LighterFilter.
![Lighter Image](/img/BedroomLighter.png)

This is the image after the DarkerFilter. 
![Darker Image](/img/DarkerBedroom.png)

### RedFilter

The RedFilter increases the red color to match the conservator's expectation of the *Bedroom*. This filter rempas the colors to what the conservator would expect. 

This is the original image of Van Gogh's *Bedroom*.
![Original Image](/img/Bedroom.png)

This is the image after the RedFilter.
![Red Image](/img/BedroomResult.png)

### TargetFilter

The TargetFilter will only keep pixels that are close to a target color while the rest of the image turns white. I have extended the Color class to include a slot that remembers the target color. There is a distance metric that decided what if the pixel color is close enough to the targeted color. 

This is the original image of Van Gogh's *Bedroom*.
![Original Image](/img/Bedroom.png)

This is the image after the TargetFilter.
![Target Image](/img/BedroomTarget.png)


