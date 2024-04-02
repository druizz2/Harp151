from tkinter import * 
import requests 
import json

root = Tk()
root.geometry("833x833")
root.title("Weather App")

def click():
    Label1 = Label(root, text="Harp 151 Label")
    Label1.pack()

# button = Button(root, text="man", cursor="man", padx="30", pady="30", highlightbackground="green", bg="orange", command=click)
# button2 = Button(root, text="box spiral", cursor="box_spiral", padx="30", pady="30", highlightbackground="orange", bg="green")
# button3 = Button(root, text = "umbrella", cursor="umbrella", padx="30", pady="30", highlightbackground="blue", bg="red")
# button4 = Button(root, text="star", cursor="star", padx="30", pady="30", highlightbackground="red", bg="blue")


# button.pack()
# button2.pack()
# button3.pack()
# button4.pack()

# lat = "42.098701"
# lon = "-75.912537"
lat = StringVar()
lat.set("")
lon = StringVar()
lon.set("")

def weekly_forecast(lat, lon):
    weather = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

    json = weather.json()
    forecast = json["properties"]["forecast"]
    daily_forecast = requests.get(forecast).json()

    for section in daily_forecast["properties"]["periods"]:
        day = section["name"]
        temp = section["temperature"]
        detail = section["detailedForecast"]
        labell = Label(root, text=f"{day} \n {temp} \n ")
        # print(day, "\n",  temp, "\n", detail)
        labell.pack()

lat_label = Label(root, text="Enter Latitude: ").pack()
lat_entry = Entry(root, textvariable=lat, width=35, borderwidth=.5).pack()
lon_label = Label(root, text="Enter Longitude: ").pack()
lon_entry = Entry(root, textvariable=lon,width=35, borderwidth=.5).pack()


# lambda required for command if need to pass function with more than one parameter
button = Button(root, font = 24, text="Get Forecast", command=lambda: weekly_forecast(lat.get(), lon.get()))
button2 = Button(root, font=24, text="Close Window", command=root.destroy)  # can put any wdiget in .destroy

button.pack(pady=20)
button2.pack(pady=20)

root.mainloop()
