import requests
import tkinter as tk
from tkinter import ttk, messagebox
def fetch_url(city,country):
  url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
  try:
    response = requests.get(url)
    info = response.json()
    if 'data' in info:
      timings = info["data"]["timings"]
      return timings
    else:
      return None
  except Exception as e:
    return 'unexpected error', e
def gui_fetch_url():
  city = city_entry.get()
  country = country_entry.get()
  if city and country:
     adhan = fetch_url(city, country)
     for name, time in adhan.items():
        list_box.insert(tk.END, name, time)
  else:
      messagebox.showerror('Error', 'insert something!')

# city = input('put your city please: ')
# country = input('put your country please: ')
# if city and country:
#     adhan = fetch_url(city, country)
# #   print(adhan)
# #or
#     for name, time in adhan.items():
#        print(name,time)
# else:
#    print('insert something!')

app = tk.Tk()
app.title('prayer times') 
frame = ttk.Frame(app, padding='20')
frame.grid(row =0, column =0,pady=5)

city_label = ttk.Label(frame, text="City: ")
city_label.grid(row=0, column =0, pady=5)

city_entry = ttk.Entry(frame, width = 20)
city_entry.grid(row=0, column=1,pady=5)


country_label = ttk.Label(frame, text="Country: ")
country_label.grid(row=1, column =0,pady=5)

country_entry = ttk.Entry(frame, width = 20)
country_entry.grid(row=1, column=1, pady=5)

fetch_button = ttk.Button(frame, text='Get Prayer Time', width=29, command=gui_fetch_url)
fetch_button.grid(row=2, column=0, pady=5, columnspan=2)

list_box = tk.Listbox(frame, height=10, width=30)
list_box.grid(row=3, column=0, columnspan=2, pady=5)

app.mainloop()