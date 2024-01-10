import tkinter as tk

def handle_poi_selection():
    # Obsługa zaznaczania punktów POI
    print("Selected POI:", selected_poi.get())

def read_wsn():
    # Obsługa przycisku "read wns"
    #sensor_range_value = entry_sensor_range.get()
    #active_sensor_value = active_sensor_var.get()
    #print("Sensor Range:", sensor_range_value)
    print("Active Sensor:")
def read_wsn_on_off():
    # Obsługa przycisku "read wns on off"
    active_sensor_value=active_sensor_var.get()
    print("Sensor Range:", active_sensor_value)

# Tworzenie głównego okna
root = tk.Tk()
root.title("Okno z Canvas, Radiobuttons, Text Input i Checkbox")

# Ustawienia okna
root.geometry("800x400")

# Podział pionowy
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Kontrolki po lewej stronie
label_poi = tk.Label(frame_left, text="Points of interest (POI)")
label_poi.pack()

# Zmienna do przechowywania zaznaczonego POI
selected_poi = tk.StringVar()

# Radiobuttons
radiobutton_poi36 = tk.Radiobutton(frame_left, text="POI 36", variable=selected_poi, value=36, command=handle_poi_selection)
radiobutton_poi121 = tk.Radiobutton(frame_left, text="POI 121", variable=selected_poi, value=121, command=handle_poi_selection)
radiobutton_poi441 = tk.Radiobutton(frame_left, text="POI 441", variable=selected_poi, value=441, command=handle_poi_selection)
radiobutton_poi121.select()
radiobutton_poi36.pack(anchor=tk.W)
radiobutton_poi121.pack(anchor=tk.W)
radiobutton_poi441.pack(anchor=tk.W)

# Napis "sensor parameters"
label_sensor_params = tk.Label(frame_left, text="Sensor parameters")
label_sensor_params.pack()

# Przycisk "read wns"
button_read_wsn = tk.Button(frame_left, text="Read WSN", command=read_wsn)
button_read_wsn.pack()


# Napis "sensor range"
label_sensor_range = tk.Label(frame_left, text="Sensor range")
label_sensor_range.pack()

# Pole input "sensor range"
entry_sensor_range_value = tk.Entry(frame_left)
entry_sensor_range_value.pack()

# Napis "Active Sensor"
label_active_sensor = tk.Label(frame_left, text="Active Sensor")
label_active_sensor.pack()

# Checkbox "Active sensor"
active_sensor_var = tk.BooleanVar()
checkbox_active_sensor = tk.Checkbutton(frame_left, text="determisticalli", variable=active_sensor_var)
checkbox_active_sensor.pack()

button_read_wsn_on_off = tk.Button(frame_left, text="Read WSN ON/OFF", command=read_wsn_on_off)
button_read_wsn_on_off.pack()

label_sensor_probability = tk.Label(frame_left,text="sensor probability initial on")
label_sensor_probability.pack()




# Canvas po prawej stronie
canvas = tk.Canvas(frame_right, bg="gray")
canvas.pack(fill=tk.BOTH, expand=True)


# Rozpoczęcie głównej pętli programu
root.mainloop()
