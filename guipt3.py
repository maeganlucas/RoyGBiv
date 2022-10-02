import customtkinter
import customtkinter as ctk
import tkinter as tk

# Create root window

ctk.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

windowX = 1150
windowY = 800
window_dim = str(windowX) + "x" + str(windowY)

root = ctk.CTk()
root.title("RoyGBiv")
root.geometry(window_dim)
root.columnconfigure(2, weight=1)
root.rowconfigure(2, weight=1)

frame_width = 525
frame_height = 325

# Widget functions


def slider1_callback(val):
    print("Slider1 detected:" + " " + str(val))


def slider2_callback(val):
    print("Slider2 detected:" + " " + str(val))


def slider3_callback(val):
    print("Slider3 detected:" + " " + str(val))


def radiobutton_event():
    print("Radio Button Selected:", rdbVAR.get())


def import_button_event():
    e_text = entry.get()
    print("Import Button Selected:" + " " + e_text)


def fs_button_event():
    print("Fullscreen Button Selected:")


def rs_button_event():
    print("Range Selection Button Selected:")


# Upper Left Frame
frame_UpL = ctk.CTkFrame(master=root, width=frame_width, height=frame_height, corner_radius=15)
frame_UpL.grid(row=0, column=0)

label1UpL = ctk.CTkLabel(master=frame_UpL,
                         text="Use the Following Color Sliders to Tune the Color Filter",
                         text_font=("Times New Roman", -20))
slider1UpL = ctk.CTkSlider(master=frame_UpL, from_=0, to=100, number_of_steps=1000, command=slider1_callback)
slider1UpL.set(0)
slider2UpL = ctk.CTkSlider(master=frame_UpL, from_=0, to=100, number_of_steps=1000, command=slider2_callback)
slider2UpL.set(0)
slider3UpL = ctk.CTkSlider(master=frame_UpL, from_=0, to=100, number_of_steps=1000, command=slider3_callback)
slider3UpL.set(0)

label1UpL.pack(pady=12, padx=10)
slider1UpL.pack(pady=12, padx=10)
slider2UpL.pack(pady=12, padx=10)
slider3UpL.pack(pady=12, padx=10)

# Upper Right Frame
frame_UpR = ctk.CTkFrame(master=root, width=frame_width, height=frame_height, corner_radius=15)
frame_UpR.grid(row=0, column=1)

label1UpR = ctk.CTkLabel(master=frame_UpR, text="Screen Filtering", text_font=("Times New Roman", -20))
FS_button = ctk.CTkButton(master=frame_UpR, text="Fullscreen Filter", corner_radius=8, command=fs_button_event)
RS_button = ctk.CTkButton(master=frame_UpR, text="Range Selection Filter", corner_radius=8, command=rs_button_event)

label1UpR.pack(pady=12, padx=10)
FS_button.pack(pady=12, padx=10)
RS_button.pack(pady=12, padx=10)

# Lower Left Frame
frame_LoL = ctk.CTkFrame(master=root, width=frame_width, height=frame_height, corner_radius=15)
frame_LoL.grid(row=1, column=0)

label1LoL = ctk.CTkLabel(master=frame_LoL, text="Import Photo to Filter", text_font=("Times New Roman", -20))
entryVAR = tk.StringVar(0)
entry = ctk.CTkEntry(master=frame_LoL, corner_radius=10, placeholder_text="directory:", textvariable=entryVAR)
button = ctk.CTkButton(master=frame_LoL, text="Confirm", corner_radius=8, command=import_button_event)

label1LoL.pack(pady=12, padx=10)
entry.pack(pady=12, padx=10)
button.pack(pady=12, padx=10)

# Lower Right Frame
frame_LoR = ctk.CTkFrame(master=root, width=frame_width, height=frame_height, corner_radius=15)
frame_LoR.grid(row=1, column=1)

rdbVAR = tk.IntVar(0)
radiobutton_1LoR = ctk.CTkRadioButton(master=frame_LoR, text="Choice1", command=radiobutton_event,
                                      variable=rdbVAR, value=1)
radiobutton_2LoR = ctk.CTkRadioButton(master=frame_LoR, text="Choice2", command=radiobutton_event,
                                      variable=rdbVAR, value=2)
radiobutton_3LoR = ctk.CTkRadioButton(master=frame_LoR, text="Choice3", command=radiobutton_event,
                                      variable=rdbVAR, value=3)
label1LoR = ctk.CTkLabel(master=frame_LoR,
                         text="Please Select The Desired Kind of Filter",
                         text_font=("Times New Roman", -20))
label1LoR.pack(pady=12, padx=10)
radiobutton_1LoR.pack(padx=12, pady=10)
radiobutton_2LoR.pack(padx=12, pady=10)
radiobutton_3LoR.pack(padx=12, pady=10)

root.mainloop()
