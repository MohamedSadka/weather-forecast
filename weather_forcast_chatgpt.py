import requests
import tkinter as tk
from tkinter import messagebox

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather Forecast App")
        master.geometry("600x400")

        self.setup_ui()

    def setup_ui(self):
        font_style = ("Helvetica", 10)

        self.location_label = tk.Label(self.master, text="Location:", font=font_style)
        self.location_entry = tk.Entry(self.master, font=font_style)
        self.search_button = tk.Button(self.master, text="Search", command=self.display_weather, font=font_style)
        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_data, font=font_style)
        self.result_label = tk.Label(self.master, text="", font=font_style)

        self.location_label.grid(row=0, column=0, padx=10, pady=10)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10)
        self.search_button.grid(row=0, column=2, pady=10, padx=10)
        self.clear_button.grid(row=0, column=3, pady=10)
        self.result_label.grid(row=2, column=0, columnspan=2, pady=10)

    def get_weather(self, api_key, location):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': location,
            'appid': api_key,
            'units': 'metric',
            'lang': 'ar',
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            weather_data = response.json()

            return weather_data
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            return None

    def display_weather(self):
        location = self.location_entry.get()
        if not location:
            messagebox.showwarning("Warning", "Please enter a location.")
            return

        api_key = "ec1fdcdfc740be73f7d8eb42ac4634b9"
        weather_data = self.get_weather(api_key, location)

        if weather_data:
            if 'message' in weather_data:
                messagebox.showerror("Error", f"Invalid location: {weather_data['message']}")
            else:
                self.show_weather_info(weather_data)

    def show_weather_info(self, weather_data):
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        rain_chance = weather_data.get('rain', {}).get('1h', 0)
        pressure = weather_data['main']['pressure']

        self.result_label.config(text=f'Temperature: {temperature}°C\n'
                                     f'Humidity: {humidity}%\n'
                                     f'Wind Speed: {wind_speed} km/h\n'
                                     f'Rain Chance: {rain_chance}%\n'
                                     f'Pressure: {pressure} hPa')

    def clear_data(self):
        self.result_label.config(text="")

if __name__ == "__main__":
    app = tk.Tk()
    weather_app = WeatherApp(app)
    app.mainloop()
