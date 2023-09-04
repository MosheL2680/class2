from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class SimpleKivyApp(App):
    def build(self):
        # Create a BoxLayout to organize the widgets vertically
        layout = BoxLayout(orientation='vertical', spacing=10, padding=150)

        # Create two TextInput widgets for number input
        self.num1_input = TextInput(hint_text="Enter number 1", input_type='number')
        self.num2_input = TextInput(hint_text="Enter number 2", input_type='number')

        # Create Buttons to calculate
        calculate_sum_button = Button(text="Calculate Sum")
        calculate_sum_button.bind(on_press=self.calculate_sum)

        calculate_mult_button = Button(text="Calculate multiplication")
        calculate_mult_button.bind(on_press=self.calculate_mult)

        calculate_division_button = Button(text="Calculate division")
        calculate_division_button.bind(on_press=self.calculate_division)

        # Create a Label to display the result
        self.result_label = Label(text="Result will be shown here")

        # Create an Exit button and set its background color to red
        exit_button = Button(text="Exit", background_color=get_color_from_hex('#FF0000'))
        exit_button.bind(on_press=self.exit)

        # Add widgets to the layout
        layout.add_widget(self.num1_input)
        layout.add_widget(self.num2_input)
        layout.add_widget(calculate_sum_button)
        layout.add_widget(calculate_mult_button)
        layout.add_widget(calculate_division_button)
        layout.add_widget(self.result_label)
        layout.add_widget(exit_button)

        return layout

    def calculate_sum(self, instance):
        num1 = int(self.num1_input.text)
        num2 = int(self.num2_input.text)
        result = num1 + num2
        self.result_label.text = str(result)
    
    def calculate_mult(self, instance):
        num1 = int(self.num1_input.text)
        num2 = int(self.num2_input.text)
        result = num1 * num2
        self.result_label.text = str(result)
    
    def calculate_division(self, instance):
        num1 = int(self.num1_input.text)
        num2 = int(self.num2_input.text)
        result = num1 / num2
        self.result_label = str(result)
    
    def exit(self):
        App.get_running_app().stop()

if __name__ == '__main__':
    SimpleKivyApp().run()
