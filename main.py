import customtkinter as ctk

def convert_temperature():
    choice = Selected_value.get()
    if (choice == "C"):
        convert_to_celsius()
    else:
        convert_to_fahrenheit()

def convert_to_celsius():
    fahrenheit = float (temp_entry.get())
    celsius = (fahrenheit - 32) * 5/9
    celsius_text = f"{celsius:.2f}°C"
    lbl_result.configure(text=celsius_text,text_color="green",font=ctk.CTkFont(size=20, weight="bold"))

def convert_to_fahrenheit():
    celsius = float (temp_entry.get())
    fahrenheit = (celsius * 5/9) + 32
    fahrenheit_text = f"{fahrenheit:.2f}°F"
    lbl_result.configure(text=fahrenheit_text, text_color="green", font=ctk.CTkFont(size=20, weight="bold"))

window =ctk.CTk()


window.geometry("600x400")
window.title("Temperature Converter")
title_label = ctk.CTkLabel(window, text="Temperatura Converter",font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(30,20))

radio_frame = ctk.CTkFrame(window)
radio_frame.pack(fill="x", padx=50)

Selected_value = ctk.StringVar(value="C")

radio_FtoC =ctk.CTkRadioButton(radio_frame,text="Fahrenheit to Celsius", variable=Selected_value,value="C")
radio_FtoC.pack(side="left",padx=(80,10),pady=10)

radio_CtoF =ctk.CTkRadioButton(radio_frame,text="Celsius To Fahrenheit", variable=Selected_value,value="F")
radio_CtoF.pack(side="left",padx=(80,10),pady=10)

input_fram = ctk.CTkFrame(window)
input_fram.pack(fill="x", padx=50, pady=30)

temp_entry =ctk.CTkEntry(input_fram,placeholder_text="Enter Temperature....")
temp_entry.pack(side="left", padx=(80,10), pady=20)

convert_Button = ctk.CTkButton(input_fram, text= "Convert", command=convert_temperature)
convert_Button.pack(side="left", padx=10, pady=20)

result_fram = ctk.CTkFrame(window)
result_fram.pack(fill="x",padx=50)

lbl_result =ctk.CTkLabel(result_fram,text="")
lbl_result.pack()

window.mainloop()