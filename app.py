# Sample Python application demonstrating 
# the working of AnchorLayout in Kivy 

# Module imports 

# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App

# The AnchorLayout aligns its children to a border 
# (top, bottom, left, right) or center 
from kivy.uix.anchorlayout import AnchorLayout

# BoxLayout arranges children in a vertical or horizontal box. 
# or help to put the childrens at the desired location. 
from kivy.uix.boxlayout import BoxLayout

# creates the button in kivy 
# if not imported shows the error 
from kivy.uix.button import Button


# A Kivy app demonstrating the working of anchor layout 
class MainLayoutApp ( App ) :

    def build (self) :
        # Anchor Layout1
        # Anchor Layout1

        anchorLayout1 = AnchorLayout ( anchor_x='left', anchor_y='bottom' )

        button1 = Button ( text='Home', size_hint=(0.3, 0.3) )

        anchorLayout1.add_widget ( button1 )

        # Anchor Layout2

        anchorLayout2 = AnchorLayout ( )

        anchorLayout2.anchor_x = 'center'

        anchorLayout2.anchor_y = 'bottom'

        # Add the anchor layouts to a box layout

        button2 = Button ( text='Report', size_hint=(0.3, 0.3) )

        anchorLayout2.add_widget ( button2 )

        # Anchor Layout2

        anchorLayout3 = AnchorLayout ( )

        anchorLayout3.anchor_x = 'right'

        anchorLayout3.anchor_y = 'bottom'

        # Add the anchor layouts to a box layout

        button3 = Button ( text='setting', size_hint=(0.3, 0.3) )

        anchorLayout3.add_widget ( button3 )
        # Create a box layout

        boxLayout = BoxLayout ( )

        # Add both the anchor layouts to the box layout

        boxLayout.add_widget ( anchorLayout1 )

        boxLayout.add_widget ( anchorLayout2 )
        boxLayout.add_widget ( anchorLayout3 )

        # Return the boxlayout widget

        return boxLayout

    # creating the object root for AnchorLayoutApp() class



root = MainLayoutApp ( )
# Run the Kivy app 
root.run ( )
