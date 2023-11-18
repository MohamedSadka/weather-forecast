import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ar',
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    if response.status_code == 200:
        return weather_data
    else:
        messagebox.showerror("Error", "there's a proplem , make sure you're looking for somthing real !")
        return None

def display_weather():
    location = location_entry.get()
    if not location:
        messagebox.showwarning("Warning", "Please enter a location.")
        return

    api_key = "ec1fdcdfc740be73f7d8eb42ac4634b9"  
    weather_data = get_weather(api_key, location)

    if weather_data:
        if 'message' in weather_data:
            messagebox.showerror("Error", f"Invalid location: {weather_data['message']}")
        else:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            rain_chance = weather_data.get('rain', {}).get('1h', 0)
            pressure = weather_data['main']['pressure']

            result_label.config(text=f'Temperature: {temperature}°C\n'
                                     f'Humidity: {humidity}%\n'
                                     f'Wind Speed: {wind_speed} km/h\n'
                                     f'Rain Chance: {rain_chance}%\n'
                                     f'Pressure: {pressure} hPa')

def clear_data():
    # Clear only the result label
    result_label.config(text="")

# GUI Setup
app = tk.Tk()
app.title("Weather Forecast App")
app.geometry("600x400")  # Set the initial size of the window

# Styles
font_style = ("Helvetica", 10)

# Widgets
location_label = tk.Label(app, text="Location:", font=font_style)
location_entry = tk.Entry(app, font=font_style)
search_button = tk.Button(app, text="Search", command=display_weather, font=font_style)
clear_button = tk.Button(app, text="Clear", command=clear_data, font=font_style)
result_label = tk.Label(app, text="", font=font_style)

# Layout
location_label.grid(row=0, column=0, padx=10, pady=10)
location_entry.grid(row=0, column=1, padx=10, pady=10)
search_button.grid(row=0, column=2, pady=10 , padx=10)
clear_button.grid(row=0, column=3, pady=10)
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the app
app.mainloop()
