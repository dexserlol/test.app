

import kivy
#kivy.require('1.10.1') # replace with your current kivy version !
from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (.9, .9, .9, 1)

def callback(instance):
	global label
	if instance.text=="=":
		try:
			label.text=str(eval(label.text))
			return
		except SyntaxError:
			label.text=""
			return
	elif instance.text=="C":
		label.text=""
		return
	label.text+=instance.text
def widget():
	global label
	text=""
	buttonText=[["7","8","9","*"],["4","5","6","-"],["1","2","3","+"],["C","0",".","="]]
	layout=BoxLayout(spacing=10,orientation='vertical',padding=[10,10,10,10])
	label=TextInput(text=text,size_hint=(1,.5),readonly=True)
	layout.add_widget(label)
	for btn_line in buttonText:
		layoutline=BoxLayout(spacing=10,orientation='horizontal')
		for btn in btn_line:
			button=Button(text=btn)
			button.bind(on_press=callback)
			layoutline.add_widget(button)
		layout.add_widget(layoutline)
	return layout
class MyApp(App):

    def build(self):
    	return widget()

if __name__ == '__main__':
    MyApp().run()