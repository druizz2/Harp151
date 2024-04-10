
import requests
import json
from tkinter import *

root = Tk()
root.geometry("800x900") 
root.title("Weather App")



lat = StringVar() # lat = "42.098701"
lat.set("")
lon = StringVar() # lon = "-75.912537"
lon.set("")
city_select = StringVar()
city_select.set("Select a City")

#source https://forecast.weather.gov/stations.php?foo=0
city_list = ["Binghamton", "New York", "Chicago", "Atlanta", "Denver"]

#list syntax: [lat, lon]
city_latlon = {"Binghamton": ["42.09", "-75.91"],
               "New York": ["40.78", "-73.96"],
              "Chicago": ["41.98", "-87.9"],
              "Atlanta": ["33.66", "-84.42"],
              "Denver": ["39.87", "-104.67"]}

def weekly_forecast(lat, lon, option=None):
    weather_text.delete("1.0", "end")   # deleting any possible input in the text box
    weather_text.insert(END, f"Weather for {option} \n")    # inserting text for selected/chosen city
    weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")   # making a request based on coords given or from city

    json = weather.json()
    forecast = json["properties"]["forecast"]
    daily_forecast = requests.get(forecast).json()

    for section in daily_forecast["properties"]["periods"]:
        day = section["name"]
        temp = section["temperature"]
        detail = section["detailedForecast"]
        text = f"{day} ---- {temp} \n"
        weather_text.insert(END, text)  # inserting weather forecast text into textbox
        weather_text.tag_config("tag_name", justify="center")   # centering the text in the textbox
        weather_text.tag_add("tag_name", "1.0", "end")  # apply "tag_name" to the whole textbox

def chosen_option():
    option = city_select.get()
    value = city_latlon[option]
    lat = value[0]
    lon = value[1]
    weekly_forecast(lat,lon, option)

def clear_forecast():
    weather_text.delete("1.0", "end") 

entry_frame = Frame(root)   # creating a frame within the root window 
entry_frame.grid(row=0, column=0)   # places the frame at 0 row, 0 column
drop_frame = Frame(root)    # creating a frame within the root window 
drop_frame.grid(row=0, column=1) # places the frame at  0 row, 1 column

label_lat = Label(entry_frame , text="Enter Latitude").pack()   
# label for latitude & gets packed in the entry frame
entry_lat = Entry(entry_frame , width=35, borderwidth=5, textvariable=lat).pack()
# creates entry widget & and is placed in entry_frame, and takes the StringVar lat as a text var.
label_lon = Label(entry_frame , text="Enter Longitude").pack() 
# label for lon & gets oacked in the entry frame
entry_lon = Entry(entry_frame , width=35, borderwidth=5, textvariable=lon).pack()
# creates entry widget & is placed in entry_frame, takes the StringVar lon as a textvariable
button = Button(entry_frame , font = 24, text = "Get Forecast", 
                command=lambda: weekly_forecast(lat.get(), lon.get()))
# creates a button in the entry frame, and its commmand is weekly_forecast taking the values of 
# lat and lon as parameters
# uses lambda since there is more than one parameter
button.pack(pady = 20)  # packs the button, with y padding 20

drop_label = Label(drop_frame, text="You can also select a city:").pack() # label for selecting a city in drop_frame
dropdown = OptionMenu(drop_frame, city_select, *city_list).pack()  
# creates a dropdown/option menu in the drop_frame, using city_list as a variable & is packed
choose_button = Button(drop_frame, text="Select City", command=chosen_option)
# creates a button in drop_frame, with the function chosen_option as the command when pressed
choose_button.pack(pady = 20)
# gives the button y padding of 20
weather_text = Text(root, height=16)    # creates textbox in the root with height 16
weather_text.grid(columnspan=2) 
# grids the waether textbox and will span 2 column

button_clear_forecast= Button(root, font=24, text="Clear Forecast", command = clear_forecast)
button_clear_forecast.grid(columnspan=2, pady=20)
"""
I added a clear forecast button and command in order to make the program a bit 
cleaner, as before, the program only cleared the textbox when a new forecast was\
chosen. This makes the program experience for the user a little bit better.
"""

button2 = Button(root, font = 24, text = "Close Window", 
                command=root.destroy)
# creates buttton the closes the application due to root.destroy
button2.grid(columnspan=2, pady = 20)
# grids the button spanning 2 columns and y padding of 20
root.mainloop()
# keeps the root running
