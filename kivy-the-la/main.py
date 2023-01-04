from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.metrics import dp  # FOR SIZE


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

#Widget

class WidgetsExample(GridLayout):

    count = 1

    # text on the Button
    my_text = StringProperty("Not Clicked")
    # variable for enabling the counter
    count_enabled = BooleanProperty(False)

    # slider_value_txt
    # slider_value_txt = StringProperty("Value")


    # Counter
    # Excercise solved by me
    # my_count = NumericProperty(0)

    # Function that manages the click of the button
    def on_button_click(self):
        print("Button clicked")
        if self.count_enabled == True:
            self.my_text = str(self.count)
            self.count += 1

        # Exercise solved by me
        # self.my_count = self.my_count + 1

    def on_toggle_button_state(self, widget):     # self is concerning this object
        print("toggle state: " + widget.state)
        if widget.state == "normal":
            # OFF
            widget.text = "OFF"
            self.count_enabled = False
        else:
            # ON
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    # def on_slider_value(self, widget):
    #    print("Slider:" + str(int(widget.value)))
    #    self.slider_value_txt = str(int(widget.value))     # widget.value is a float



#Layout

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "lr-tb"

        for i in range(0, 100):
            # b = Button(text=str(i+1), size_hint=(.2, .2))

            # size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

class GridLayoutExample(GridLayout):
    pass

class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass

"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #Orientation Property
        self.orientation = "vertical"   #default is horizontal


        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")


        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass

#Base class of our application

class TheLabApp(App):
    pass

TheLabApp().run()