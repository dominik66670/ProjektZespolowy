# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import tkinter as tk
from tkinter import filedialog

from items import Sensor
from items import POI

def handle_poi_selection():
    # Obsługa zaznaczania punktów POI
    print_POIs(800,800)

def read_wsn():
    # Obsługa przycisku "read wns"
    #sensor_range_value = entry_sensor_range.get()
    #active_sensor_value = active_sensor_var.get()
    #print("Sensor Range:", sensor_range_value)
    print("Active Sensor:")
def read_wsn_on_off():
    # Obsługa przycisku "read wns on off"
    active_sensor_value = active_sensor_var.get()
    print("Sensor Range:", active_sensor_value)
    
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines.pop(0)
    krotki = []
    for i in lines:
        dane = i.split(' ')
        krotki.append((float(dane[0]),float(dane[1])))
    print(krotki)
def browse_file():
    file_path = filedialog.askopenfilename(initialdir="DATA/",title="Wybierz plik")
    if file_path:
        # Wyświetl ścieżkę do wybranego pliku
        # Odczytaj zawartość pliku
        read_file(file_path)

def print_POIs(x,y):
    canvas.delete("all")
    count = selected_poi.get()
    countsqrt = math.sqrt(count)
    countsqrt = round(countsqrt)
    ix = x / (countsqrt + 1)
    ix = round(ix)
    iy = y / (countsqrt + 1)
    iy = round(iy)
    tempix = ix
    for i in range(0,countsqrt,1):
        tempiy = iy
        for j in range(0,countsqrt,1):
            canvas.create_oval(tempix, tempiy, tempix + 2, tempiy + 2, outline="#000000",fill="#FFFF00")
            tempiy += iy
        tempix += ix
# Tworzenie głównego okna
root = tk.Tk()
root.title("Okno z Canvas, Radiobuttons, Text Input i Checkbox")

# Ustawienia okna
root.geometry("1200x800")

# Podział pionowy
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Kontrolki po lewej stronie
label_poi = tk.Label(frame_left, text="Points of interest (POI)")
label_poi.pack(anchor=tk.W)

# Zmienna do przechowywania zaznaczonego POI
selected_poi = tk.IntVar()

# Radiobuttons
radiobutton_poi36 = tk.Radiobutton(frame_left, text=36, variable=selected_poi, value=36, command=handle_poi_selection)
radiobutton_poi121 = tk.Radiobutton(frame_left, text=121, variable=selected_poi, value=121, command=handle_poi_selection)
radiobutton_poi441 = tk.Radiobutton(frame_left, text=441, variable=selected_poi, value=441, command=handle_poi_selection)
radiobutton_poi121.select()
radiobutton_poi36.pack(anchor=tk.W)
radiobutton_poi121.pack(anchor=tk.W)
radiobutton_poi441.pack(anchor=tk.W)

# Napis "sensor parameters"
label_sensor_params = tk.Label(frame_left, text="Sensor parameters")
label_sensor_params.pack(anchor=tk.W)

# Przycisk "read wns"
button_read_wsn = tk.Button(frame_left, text="Read WSN", command=browse_file)
button_read_wsn.pack(anchor=tk.W)


# Napis "sensor range"
label_sensor_range = tk.Label(frame_left, text="Sensor range")
label_sensor_range.pack(anchor=tk.W)

# Pole input "sensor range"
entry_sensor_range_value = tk.Entry(frame_left)
entry_sensor_range_value.pack(anchor=tk.W)

# Napis "Active Sensor"
label_active_sensor = tk.Label(frame_left, text="Active Sensor")
label_active_sensor.pack(anchor=tk.W)

# Checkbox "Active sensor"
active_sensor_var = tk.BooleanVar()
checkbox_active_sensor = tk.Checkbutton(frame_left, text="determisticalli", variable=active_sensor_var)
checkbox_active_sensor.pack(anchor=tk.W)

button_read_wsn_on_off = tk.Button(frame_left, text="Read WSN ON/OFF", command=read_wsn_on_off)
button_read_wsn_on_off.pack(anchor=tk.W)
#------------------------------------------------------------------------------------------------------------------
label_sensor_probability = tk.Label(frame_left,text="sensor probability initial on")
label_sensor_probability.pack(anchor=tk.W)


button_show_wns = tk.Button(frame_left, text="Show WSN", command=read_wsn_on_off)
button_show_wns.pack(anchor=tk.W)

q_button_frame = tk.Frame(frame_left)
q_button_frame.pack(anchor=tk.W)

button_calc_single_q = tk.Button(q_button_frame, text="calc single q", command=read_wsn_on_off)
button_calc_single_q.pack(side=tk.LEFT, padx=5)

button_calc_all_q = tk.Button(q_button_frame, text="calc all q", command=read_wsn_on_off)
button_calc_all_q.pack(side=tk.LEFT, padx=5)

button_find_wsn_graph = tk.Button(frame_left, text="find WSN graph", command=read_wsn_on_off)
button_find_wsn_graph.pack(anchor=tk.W)

button_calc_sensor_id = tk.Button(frame_left, text="calc sensor id", command=read_wsn_on_off)
button_calc_sensor_id.pack(anchor=tk.W)

last_frame = tk.Frame(frame_left)
last_frame.pack(anchor=tk.W)

label_algorithm_parameters = tk.Label(last_frame,text="algorithm parameters ->")
label_algorithm_parameters.pack(side=tk.LEFT, padx=5)

button_next_page = tk.Button(last_frame, text="Next page", command=read_wsn_on_off)
button_next_page.pack(side=tk.LEFT, padx=5)


# Canvas po prawej stronie
canvas = tk.Canvas(frame_right, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)


# Rozpoczęcie głównej pętli programu
root.mainloop()