from tkinter import * 
import requests 
import json

root = Tk()
root.geometry("833x833")
root.title("Weather App")

# def click():
#     Label1 = Label(root, text="Harp 151 Label")
#     Label1.pack()

# button = Button(root, text="man", cursor="man", padx="30", pady="30", highlightbackground="green", bg="orange", command=click)
# button2 = Button(root, text="box spiral", cursor="box_spiral", padx="30", pady="30", highlightbackground="orange", bg="green")
# button3 = Button(root, text = "umbrella", cursor="umbrella", padx="30", pady="30", highlightbackground="blue", bg="red")
# button4 = Button(root, text="star", cursor="star", padx="30", pady="30", highlightbackground="red", bg="blue")


# button.pack()
# button2.pack()
# button3.pack()
# button4.pack()




lat = StringVar()
lat.set("")
lon = StringVar()
lon.set("")

#source https://forecast.weather.gov/stations.php?foo=0
city_list = ["Binghamton", "New York", "Chicago", "Atlanta", "Denver"]

#list syntax: [lat, lon]
city_latlon = {"Binghamton": ["42.09", "-75.91"], 
               "New York": ["40.78", "-73.96"],
              "Chicago": ["41.98", "-87.9"],
              "Atlanta": ["33.66", "-84.42"],
              "Denver": ["39.87", "-104.67"]}

forecast_text = Text(root, font = ("Helvitica", "16"),
                  height=10, width=25)

def weekly_forecast(lat, lon):
    location_get = location.get()
    lat = city_latlon[location_get][0]
    lon = city_latlon[location_get][1]
    forecast_text.delete("1.0", "end")
    weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
    json = weather.json()
    forecast = json["properties"]["forecast"]
    daily_forecast = requests.get(forecast).json()

    for section in daily_forecast["properties"]["periods"]:
        day = section["name"]
        temp = section["temperature"]
        detail = section["detailedForecast"]
        text = f"{day} --- {temp} \n "
        forecast_text.insert(END, text)




location = StringVar()
location.set("Select A Location")
dropdown = OptionMenu(root, location, *city_list)

dropdown.pack()


# lambda required for command if need to pass function with more than one parameter
button = Button(root, font = 24, text="Get Forecast", command=lambda: weekly_forecast(lat.get(), lon.get()))
button2 = Button(root, font=24, text="Close Window", command=root.destroy)  # can put any wdiget in .destroy

button.pack(pady=20)

forecast_text.pack()

button2.pack(pady=20)


root.mainloop()
