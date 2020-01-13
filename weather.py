from tkinter import *
import pyowm


def format_response(weather):
	try:
		#name = weather.get_city();
		Ftemp = weather.get_temperature('celsius')
		Ctemp = weather.get_temperature('fahrenheit') 

		final_str = 'Temperature (°C): %s \nTemperature (°F): %s' % (Ctemp['temp'], Ftemp['temp'])
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str
def get_weather(city):
    owm = pyowm.OWM('50cc86805efa08568cc4f3bceb8394f0') # get access using key
    observation = owm.weather_at_place(city) # get a json observation
    weather = observation.get_weather() # get the weather component

    label_description['text']= "Temperature for the city",city ,"is:"
    label_show['text']= format_response(weather)
    
window = Tk()
window.title("Weather app")
window.geometry("300x300")

l1 = Label(window, text="City:")
txt = Entry(window,width=30)
bt = Button(window, text='Get weather', command=lambda:get_weather(txt.get()))
label_description=Label(window)
label_show=Label(window)

l1.grid(column = 3, row = 7)
txt.grid(column=4, row=7)
bt.grid(column = 4, row = 9)
label_description.grid(column= 4, row = 11)
label_show.grid(column = 4, row=12)
window.mainloop()
 
