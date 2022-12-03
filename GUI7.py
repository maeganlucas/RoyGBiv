import tkinter
import cv2
import customtkinter as ctk
import tkinter as tk
import numpy as np
from numpy import asarray
from PIL import Image, ImageTk
from tkinter import ttk, filedialog
import webcolors
from colorblind import colorblind
from webcolors import hex_to_rgb
import matplotlib.pyplot as plt
    # https://medium.com/codex/rgb-to-color-names-in-python-the-robust-way-ec4a9d97a01f
from scipy.spatial import KDTree
import PIL
from PIL import ImageGrab
    # https://stackoverflow.com/questions/42636933/get-rgb-value-from-screen-pixels-with-python
import pyscreenshot

red_count = 0
green_count = 0
blue_count = 0
black_count = 0
gray_count = 0
purple_count = 0
yellow_count = 0
orange_count = 0
white_count = 0
brown_count = 0
pink_count = 0
count_array = []
average_array = []
range_size = 0


class App(ctk.CTk):
    name = "RoyGBiv"
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def __init__(self, *args):
        super().__init__(*args)
        window_x = 1050
        window_y = 650
        window_dim = str(window_x) + "x" + str(window_y)

        self.title(App.name)
        self.geometry(window_dim)
        self.resizable(False, False)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(2, weight=1)
        self.protocol("Delete_Window", self.on_closing)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Define Filter Frame, Instruction Frame, and Button Frame
        self.filter_frame = ctk.CTkFrame(master=self, width=500, height=490, corner_radius=10)
        self.instruct_frame = ctk.CTkFrame(master=self, width=500, height=270, corner_radius=10)
        self.button_frame = ctk.CTkFrame(master=self, width=500, height=200, corner_radius=10)
        self.filter_frame.place(relx=0.25, rely=0.60, anchor=tk.CENTER)
        self.instruct_frame.place(relx=0.75, rely=0.43, anchor=tk.CENTER)
        self.button_frame.place(relx=0.75, rely=0.82, anchor=tk.CENTER)

        # Start Title
        title1 = ctk.CTkLabel(master=self, width=10, height=10, text="Welcome to RoyGBiv",
                              text_font=("STIXVariants", -55))
        title2 = ctk.CTkLabel(master=self, width=10, height=10, text="A Screen Color Filtering Software",
                              text_font=("STIXVariants", -20))
        title1.place(relx=0.5, rely=0.08, anchor=tk.CENTER)
        title2.place(relx=0.5, rely=0.16, anchor=tk.CENTER)

        # Filter Frame Title
        title_ff = ctk.CTkLabel(master=self.filter_frame, text="Select a Filter", text_font=("STIXVariants", -35))
        title_ff.place(relx=0.5, rely=0.075, anchor=tk.CENTER)

        # Instruction Frame
        title_if = ctk.CTkLabel(master=self.instruct_frame, text="How to Use Roy G. Biv",
                                text_font=("STIXVariants", -30))
        title_if.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Define Instructions
        ins1 = "1.) Determine whether you want to use a filtering option or detect color on your screen."
        ins1l = ctk.CTkLabel(master=self.instruct_frame, text=ins1, text_font=("STIXVariants", -13))
        ins1l.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        ins2 = "2.) For filtering, select your filter values in the 'Select a Filter' box to the left and click"
        ins2l = ctk.CTkLabel(master=self.instruct_frame, text=ins2, text_font=("STIXVariants", -13))
        ins2l.place(relx=0.49, rely=0.43, anchor=tk.CENTER)

        ins22 = "'Confirm'. If you want to save your filter, click the “Save Filter” button. If you already"
        ins22l = ctk.CTkLabel(master=self.instruct_frame, text=ins22, text_font=("STIXVariants", -13))
        ins22l.place(relx=0.51, rely=0.52, anchor=tk.CENTER)

        ins23 = "have a saved filter, please select your filter from the drop-down box."
        ins23l = ctk.CTkLabel(master=self.instruct_frame, text=ins23, text_font=("STIXVariants", -13))
        ins23l.place(relx=0.43, rely=0.6, anchor=tk.CENTER)

        ins3 = "3.) Next, select the button of your choice!"
        ins3l = ctk.CTkLabel(master=self.instruct_frame, text=ins3, text_font=("STIXVariants", -13))
        ins3l.place(relx=0.24, rely=0.75, anchor=tk.CENTER)

        ins4 = "4.) Watch Roy G. Biv do its magic!"
        ins4l = ctk.CTkLabel(master=self.instruct_frame, text=ins4, text_font=("STIXVariants", -13))
        ins4l.place(relx=0.20, rely=0.90, anchor=tk.CENTER)

        # Button Frame
        screen_fill_button = ctk.CTkButton(master=self.button_frame, width=110, height=75, corner_radius=15, hover=True,
                                           text="Filter Your Screen", command=self.screen_filtering, state=ctk.DISABLED,
                                           text_font=("STIXVariants", -20))
        photo_fill_button = ctk.CTkButton(master=self.button_frame, width=110, height=75, corner_radius=15, hover=True,
                                          text="Filter a Photo", command=self.photo_filtering, state=ctk.DISABLED,
                                          text_font=("STIXVariants", -20))
        detect_color_button = ctk.CTkButton(master=self.button_frame, width=110, height=75, corner_radius=15,
                                            hover=True, text="Detect Color", text_font=("STIXVariants", -20),
                                            state=ctk.NORMAL, command=self.detect_color)
        test_filter_button = ctk.CTkButton(master=self.button_frame, width=110, height=75, corner_radius=15,
                                           hover=True, text="Test Filter", command=self.test_filter, state=ctk.DISABLED,
                                           text_font=("STIXVariants", -20))
        screen_fill_button.place(relx=0.34, rely=0.25, anchor=tk.CENTER)
        photo_fill_button.place(relx=0.34, rely=0.70, anchor=tk.CENTER)
        test_filter_button.place(relx=0.72, rely=0.70, anchor=tk.CENTER)
        detect_color_button.place(relx=0.72, rely=0.25, anchor=tk.CENTER)

        # Custom Filter Label
        filter_frame_label1 = ctk.CTkLabel(master=self.filter_frame, width=10, height=10, text="Create Custom Filter:",
                                           text_font=("STIXVariants", -25))
        filter_frame_label1.place(relx=0.25, rely=0.2, anchor=tk.CENTER)

        # Filter Sliders Labels
        sl1 = ctk.CTkLabel(master=self.filter_frame, width=10, height=10, text="Deuteranopia",
                           text_font=("STIXVariants", -25))
        sl2 = ctk.CTkLabel(master=self.filter_frame, width=10, height=10, text="Protanopia",
                           text_font=("STIXVariants", -25))
        sl3 = ctk.CTkLabel(master=self.filter_frame, width=10, height=10, text="Tritanopia",
                           text_font=("STIXVariants", -25))
        sl1.place(relx=0.18, rely=0.32, anchor=tk.CENTER)
        sl2.place(relx=0.15, rely=0.47, anchor=tk.CENTER)
        sl3.place(relx=0.14, rely=0.62, anchor=tk.CENTER)

        # Filter Sliders
        def slider_action1(label_value1):
            screen_fill_button.configure(state=ctk.DISABLED)
            photo_fill_button.configure(state=ctk.DISABLED)
            test_filter_button.configure(state=ctk.DISABLED)
            self.t_slider.configure(state=ctk.DISABLED)
            label_value1 = round(self.d_slider.get(), 4)
            num_1.configure(text=str(label_value1))

        def slider_action2(label_value2):
            screen_fill_button.configure(state=ctk.DISABLED)
            photo_fill_button.configure(state=ctk.DISABLED)
            test_filter_button.configure(state=ctk.DISABLED)
            self.t_slider.configure(state=ctk.DISABLED)
            label_value2 = round(self.p_slider.get(), 4)
            num_2.configure(text=str(label_value2))

        def slider_action3(label_value):
            screen_fill_button.configure(state=ctk.DISABLED)
            photo_fill_button.configure(state=ctk.DISABLED)
            test_filter_button.configure(state=ctk.DISABLED)
            self.p_slider.configure(state=ctk.DISABLED)
            self.d_slider.configure(state=ctk.DISABLED)
            label_value3 = round(self.t_slider.get(), 4)
            num_3.configure(text=str(label_value3))

        self.d_slider = ctk.CTkSlider(master=self.filter_frame, width=250, height=25, from_=0, to=1,
                                      number_of_steps=1000,command=slider_action1)
        self.d_slider.set(0)
        self.p_slider = ctk.CTkSlider(master=self.filter_frame, width=250, height=25, from_=0, to=1,
                                      number_of_steps=1000, command=slider_action2)
        self.p_slider.set(0)
        self.t_slider = ctk.CTkSlider(master=self.filter_frame, width=250, height=25, from_=0, to=1,
                                      number_of_steps=1000, command=slider_action3)
        self.t_slider.set(0)
        self.d_slider.place(relx=0.61, rely=0.32, anchor=tk.CENTER)
        self.p_slider.place(relx=0.61, rely=0.47, anchor=tk.CENTER)
        self.t_slider.place(relx=0.61, rely=0.62, anchor=tk.CENTER)

        # Slider Value Labels
        num_1 = ctk.CTkLabel(master=self.filter_frame, width=10, height=10, text=str(0),
                             text_font=("STIXVariants", -25))
        num_2 = ctk.CTkLabel(master=self.filter_frame, width=10, height=10, text=str(0),
                             text_font=("STIXVariants", -25))
        num_3 = ctk.CTkLabel(master=self.filter_frame, width=10, height=10, text=str(0),
                             text_font=("STIXVariants", -25))
        num_1.place(relx=0.92, rely=0.32, anchor=tk.CENTER)
        num_2.place(relx=0.92, rely=0.47, anchor=tk.CENTER)
        num_3.place(relx=0.92, rely=0.62, anchor=tk.CENTER)

        # Saved Filter Selection

        def option(choice):
            # Updates Sliders & Labels When Saved Filter is selected
            choice = var.get()
            name = np.loadtxt("test saved filter.txt", usecols=0, dtype=str)
            val_index = np.where(name == choice)
            vals = np.loadtxt("test saved filter.txt", usecols=1, dtype=str)
            choice_vals_str = vals[val_index]
            choice_vals = choice_vals_str[0]
            vals = choice_vals.split(",")
            num_1.configure(text=vals[0])
            num_2.configure(text=vals[1])
            num_3.configure(text=vals[2])
            self.d_slider.set(float(vals[0]))
            self.p_slider.set(float(vals[1]))
            self.t_slider.set(float(vals[2]))

        saved_filters_names = np.loadtxt("test saved filter.txt", usecols=0, dtype=str)
        label2_fs = ctk.CTkLabel(master=self.filter_frame, width=100, height=25, text="Select a Saved Filter:",
                                 text_font=("STIXVariants", -25))
        var = tkinter.StringVar()
        filter_opt = ctk.CTkOptionMenu(master=self.filter_frame, width=205, height=35, variable=var,
                                       values=saved_filters_names, corner_radius=10, hover=True, command=option)
        filter_opt.place(relx=0.72, rely=0.75, anchor=tk.CENTER)
        label2_fs.place(relx=0.25, rely=0.75, anchor=tk.CENTER)

        # Save Filter Inputs
        def save():
            # saves filter name and values
            d = round(self.d_slider.get(), 4)
            p = round(self.p_slider.get(), 4)
            t = round(self.t_slider.get(), 4)
            num_1.configure(text=str(d))
            num_2.configure(text=str(p))
            num_3.configure(text=str(t))
            save_win = ctk.CTkToplevel()
            save_win.title("Save Current Filter")
            save_win.geometry("600x200")
            save_frame = ctk.CTkFrame(master=save_win, width=600, height=200, corner_radius=10)
            save_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            values = [round(self.d_slider.get(), 4), round(self.p_slider.get(), 4), round(self.t_slider.get(), 4)]
            str_values = "Saving values: " + str(values)
            val_label = ctk.CTkLabel(master=save_frame, width=400, height=75, text=str_values,
                                     text_font=("STIXVariants", -25))
            val_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
            name_label = ctk.CTkLabel(master=save_frame, width=400, height=75, text="Please enter name for this filter",
                                      text_font=("STIXVariants", -25))
            name_label.place(relx=0.30, rely=0.5, anchor=tk.CENTER)
            name_entry = ctk.CTkEntry(master=save_frame, placeholder_text="type name here", width=120)
            name_entry.place(relx=0.70, rely=0.5, anchor=tk.CENTER)

            def save_to_file():
                val_str = str(values).replace(' ', '')
                data_format1 = name_entry.get()
                data_format_name = data_format1.replace(' ', '')
                format_vals = val_str.replace('[', '').replace(']', '')
                data_format = data_format_name + " " + format_vals
                print(data_format)
                file = open("test saved filter.txt", "a")
                file.write("\n")
                file.write(data_format)
                file.close()
                name_label.configure(text="Filter saved successfully")
                save_win.destroy()

            sf_save = ctk.CTkButton(master=save_frame, width=65, height=35, borderwidth=0, corner_radius=10,
                                    hover=True, text="Confirm", text_font=("STIXVariants", -20), command=save_to_file)
            sf_save.place(relx=0.9, rely=0.5, anchor=tk.CENTER)

        # Confirm Filter inputs
        def confirm():
            # Zero out slider labels
            num_1.configure(text=str(0))
            num_2.configure(text=str(0))
            num_3.configure(text=str(0))
            print("Confirm Selected")
            # Get inputs
            d = round(self.d_slider.get(), 4)
            p = round(self.p_slider.get(), 4)
            t = round(self.t_slider.get(), 4)
            print("Inputted Slider Values:" +
                  ", d: " + str(d) +
                  ", p: " + str(p) +
                  ", t: " + str(t))
            # Set Slider Labels
            num_1.configure(text=str(d))
            num_2.configure(text=str(p))
            num_3.configure(text=str(t))
            screen_fill_button.configure(state=ctk.NORMAL)
            photo_fill_button.configure(state=ctk.NORMAL)
            test_filter_button.configure(state=ctk.NORMAL)

        # Sets all sliders to 0
        def reset():
            self.p_slider.set(0)
            self.d_slider.set(0)
            self.t_slider.set(0)
            self.p_slider.configure(state=ctk.NORMAL)
            self.d_slider.configure(state=ctk.NORMAL)
            self.t_slider.configure(state=ctk.NORMAL)

        ff_confirm = ctk.CTkButton(master=self.filter_frame, width=65, height=45, borderwidth=0, corner_radius=10,
                                   hover=True, text="Confirm", text_font=("STIXVariants", -25), command=confirm)
        ff_reset = ctk.CTkButton(master=self.filter_frame, width=65, height=45, borderwidth=0, corner_radius=10,
                                 hover=True, text="Reset Sliders", text_font=("STIXVariants", -25), command=reset)
        ff_save = ctk.CTkButton(master=self.filter_frame, width=65, height=45, borderwidth=0, corner_radius=10,
                                hover=True, text="Save Filter", text_font=("STIXVariants", -25), command=save)
        ff_save.place(relx=0.16, rely=0.9, anchor=tk.CENTER)
        ff_confirm.place(relx=0.83, rely=0.9, anchor=tk.CENTER)
        ff_reset.place(relx=0.51, rely=0.9, anchor=tk.CENTER)

    def start(self):
        self.mainloop()

    def on_closing(self, event=0):
        print("Closing Window")
        self.destroy()

    def screen_filtering(self):
        print("Screen Filtering Selected")
        window_x = 1050
        window_y = 650

        window_dim2 = str(window_x) + "x" + str(window_y)
        sf_win = ctk.CTk()
        sf_win.title("Screen Filtering")
        sf_win.geometry(window_dim2)

        sf_frame = ctk.CTkFrame(master=sf_win, width=window_x, height=window_y, corner_radius=15)
        sf_frame.grid(row=1, column=0)

        # Frame Label
        title_sf = ctk.CTkLabel(master=sf_frame, text="Screen Filtering", text_font=("Times New Roman", -35))

        # Buttons
        # Full Screen Selection Event
        def fs_button_event():
            fs_button.deselect()
            rs_button.state = tk.DISABLED
            # Screen Diagram Frame
            screen_frame = ctk.CTkFrame(master=sf_frame, width=950, height=500, corner_radius=10)
            screen_frame.configure(bg_color='grey', fg_color='grey')

            def colorCorrectionDP(protanopia, deutranopia):
                return np.array([[1 - deutranopia / 2, deutranopia / 2, 0], [protanopia / 2, 1 - protanopia / 2, 0],
                                    [protanopia / 4, deutranopia / 4, 1 - (protanopia + deutranopia) / 4]]).T

            # https://ixora.io/projects/colorblindness/color-blindness-simulation-research/used for matrix
            def Tritanopia(img):
                colorblind_img = colorblind.simulate_colorblindness(img, colorblind_type='t')
                defection = img - colorblind_img
                correction = np.array([[0, 0, 0], [0.7, 1, 0], [0.7, 0, 1]])
                Daltonization = np.tensordot(defection, correction, axes=([2], [1]))
                return img + Daltonization

            # Connect these values to the slider
            deutranopia = round(self.d_slider.get(), 4)
            protanopia = round(self.p_slider.get(), 4)
            tritanopia = round(self.t_slider.get(), 4)
            # NO CURRENT OPTION FOR A TRITANOPIA SLIDER / MUST BE MUTUALLY EXCLUSIVE FROM DUETRANOPIA AND PROTANOPIA

            imgCorrected = np.array(PIL.ImageGrab.grab()) / 255
            transform = colorCorrectionDP(protanopia=protanopia, deutranopia=deutranopia)
            img_correctedPD = np.uint8(np.dot(imgCorrected, transform) * 255)
            # Correcting Image for Deutranopia with diagnosed degree of 1.0 and saving the image to file.
            imgDaltonized = Tritanopia(PIL.ImageGrab.grab())
            cv2.imwrite("colorchangePD.jpg", img_correctedPD)
            cv2.imwrite("colorchangeT.jpg", imgDaltonized)

            if tritanopia > 0:
                # Display T image
                imgT = cv2.imread("colorchangeT.jpg")
                cv2.imshow("Tritanopia filtered photo", imgT)
            elif protanopia > 0 or deutranopia > 0:
                # Display PD Image
                cv2.imshow("Filtered Photo", img_correctedPD)
            elif protanopia == 0 and deutranopia == 0 and tritanopia == 0:
                img = PIL.ImageGrab.grab()
                img.save("unfilteredFSS.jpg")
                imgUFSS = cv2.imread("unfilteredFSS.jpg")
                cv2.imshow("Unfiltered Photo", imgUFSS)
            else:
                print("error line 357ish")

            screen_frame.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        # Range Selection Event
        def rs_button_event():
            # ------------------------------------- Connal's Code ------------------------------------------------------
            areaCorners = [[], []]
            rs_win = ctk.CTkToplevel(sf_win)
            rs_win.overrideredirect(True)
            rs_win.geometry("400x400")

            rs_win.attributes("-alpha", 0.5)

            def moveWindow(event):
                rs_win.geometry("+" + str(event.x_root) + "+" + str(event.y_root))

            def resize_left(event):
                if rs_win.current_width + rs_win.winfo_x() - event.x_root >= 250:
                    rs_win.geometry(str(rs_win.current_width + rs_win.winfo_x() - event.x_root) + "x" + str(
                        rs_win.current_height) + "+" + str(event.x_root) + "+" + str(rs_win.winfo_y()))
                    left_side.place(x=0, y=0)
                    top_side.configure(width=rs_win.current_width)
                    bottom_side.configure(width=rs_win.current_width)
                    right_side.place(x=rs_win.current_width - 10, y=0)

            def resize_right(event):
                if rs_win.current_width - rs_win.winfo_x() + event.x_root >= 250:
                    rs_win.geometry(str(event.x_root - rs_win.winfo_x()) + "x" + str(rs_win.current_height))
                    top_side.configure(width=rs_win.current_width)
                    bottom_side.configure(width=rs_win.current_width)
                    right_side.place(x=rs_win.current_width - 10, y=0)

            def resize_top(event):
                if rs_win.current_height + rs_win.winfo_y() - event.y_root >= 75:
                    rs_win.geometry(str(rs_win.current_width) + "x" + str(
                        rs_win.current_height + rs_win.winfo_y() - event.y_root) + "+" + str(
                        rs_win.winfo_x()) + "+" + str(event.y_root))
                    top_side.place(x=0, y=0)
                    left_side.configure(height=rs_win.current_height)
                    right_side.configure(height=rs_win.current_height)
                    bottom_side.place(x=0, y=rs_win.current_height - 10)

            def resize_bottom(event):
                if rs_win.current_height - rs_win.winfo_y() + event.y_root >= 75:
                    rs_win.geometry(str(rs_win.current_width) + "x" + str(event.y_root - rs_win.winfo_y()))
                    left_side.configure(height=rs_win.current_height)
                    right_side.configure(height=rs_win.current_height)
                    bottom_side.place(x=0, y=rs_win.current_height - 10)

            def resultButton():
                areaCorners = [[rs_win.winfo_x(), rs_win.winfo_y()],
                               [rs_win.winfo_x() + rs_win.current_width, rs_win.winfo_y() + rs_win.current_height]]
                print([[rs_win.winfo_x(), rs_win.winfo_y()],
                       [rs_win.winfo_x() + rs_win.current_width, rs_win.winfo_y() + rs_win.current_height]])
                diagram_frame = ctk.CTkFrame(master=screen_frame, width=(rs_win.winfo_x() + rs_win.current_width)*0.5,
                                             height=(rs_win.winfo_y() + rs_win.current_height)*0.5, fg_color='white',
                                             bg_color='white')
                diagram_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                pic_of_range = pyscreenshot.grab(bbox=(rs_win.winfo_x(), rs_win.winfo_y(),
                                                       rs_win.winfo_x() + rs_win.current_width,
                                                       rs_win.winfo_y() + rs_win.current_height))
                pic_of_range.save("range_selection_unfiltered.png")

                def colorCorrectionDP(protanopia, deutranopia):
                    return np.array([[1 - deutranopia / 2, deutranopia / 2, 0], [protanopia / 2, 1 - protanopia / 2, 0],
                                     [protanopia / 4, deutranopia / 4, 1 - (protanopia + deutranopia) / 4]]).T

                # https://ixora.io/projects/colorblindness/color-blindness-simulation-research/used for matrix
                def Tritanopia(img):
                    colorblind_img = colorblind.simulate_colorblindness(img, colorblind_type='t')
                    defection = img - colorblind_img
                    correction = np.array([[0, 0, 0], [0.7, 1, 0], [0.7, 0, 1]])
                    Daltonization = np.tensordot(defection, correction, axes=([2], [1]))
                    return img + Daltonization

                # Connect these values to the slider
                deutranopia = round(self.d_slider.get(), 4)
                protanopia = round(self.p_slider.get(), 4)
                tritanopia = round(self.t_slider.get(), 4)
                # NO CURRENT OPTION FOR A TRITANOPIA SLIDER / MUST BE MUTUALLY EXCLUSIVE FROM DUETRANOPIA AND PROTANOPIA

                imgCorrected = np.array(pic_of_range) / 255
                transform = colorCorrectionDP(protanopia=protanopia, deutranopia=deutranopia)
                img_correctedPD = np.uint8(np.dot(imgCorrected, transform) * 255)
                # Correcting Image for Deutranopia with diagnosed degree of 1.0 and saving the image to file.
                imgDaltonized = Tritanopia(pic_of_range)
                cv2.imwrite("colorchangePD.jpg", img_correctedPD)
                cv2.imwrite("colorchangeT.jpg", imgDaltonized)

                if tritanopia > 0:
                    # Display T image
                    imgT = cv2.imread("colorchangeT.jpg")
                    cv2.imshow("Tritanopia filtered photo", imgT)
                elif protanopia > 0 or deutranopia > 0:
                    # Display PD Image
                    cv2.imshow("PD Filtered Photo", img_correctedPD)
                elif protanopia == 0 and deutranopia == 0 and tritanopia == 0:
                    img = cv2.imread("range_selection_unfiltered.png")
                    cv2.imshow("Filtered Photo", img)
                else:
                    print("error line 458ish")

                rs_win.destroy()

            def escClose(event):
                rs_win.destroy()

            left_side = tkinter.Frame(master=rs_win, width=10, height=rs_win.current_height, cursor="sb_h_double_arrow")
            left_side.place(x=0, y=0)
            left_side.bind('<B1-Motion>', resize_left)

            right_side = tkinter.Frame(master=rs_win, width=10, height=rs_win.current_height,
                                       cursor="sb_h_double_arrow")
            right_side.place(x=rs_win.current_width - 10, y=0)
            right_side.bind('<B1-Motion>', resize_right)

            top_side = tkinter.Frame(master=rs_win, width=rs_win.current_width, height=10, cursor="sb_v_double_arrow")
            top_side.place(x=0, y=0)
            top_side.bind('<B1-Motion>', resize_top)

            bottom_side = tkinter.Frame(master=rs_win, width=rs_win.current_width, height=10,
                                        cursor="sb_v_double_arrow")
            bottom_side.place(x=0, y=rs_win.current_height - 10)
            bottom_side.bind('<B1-Motion>', resize_bottom)

            result_button = ctk.CTkButton(master=rs_win, width=20, height=20, text="Select Range",
                                          command=resultButton)
            result_button.place(x=20, y=0)

            move_button = tkinter.Frame(master=rs_win, bg="black", width=20, height=20, cursor="fleur")
            move_button.place(x=0, y=0)
            move_button.bind('<B1-Motion>', moveWindow)

            rs_win.bind("<Escape>", lambda event: escClose(event))

            rs_win.mainloop()

        fs_button = ctk.CTkRadioButton(master=sf_frame, text="Full screen Filter", corner_radius=6,
                                       command=fs_button_event)
        rs_button = ctk.CTkRadioButton(master=sf_frame, text="Range Selection Filter", corner_radius=6,
                                       command=rs_button_event)
        # Screen Diagram Frame
        screen_frame = ctk.CTkFrame(master=sf_frame, width=950, height=500, corner_radius=10)

        screen_frame.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        title_sf.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
        fs_button.place(relx=0.2, rely=0.12, anchor=tk.CENTER)
        rs_button.place(relx=0.8, rely=0.12, anchor=tk.CENTER)

        sf_win.mainloop()

    def photo_filtering(self):
        print("Photo Filtering Selected")
        window_x = 1050
        window_y = 650
        window_dim2 = str(window_x) + "x" + str(window_y)
        ph_win = ctk.CTkToplevel()
        ph_win.title("Filter a Photo")
        ph_win.geometry(window_dim2)
        # Create Frame
        ph_frame = ctk.CTkFrame(master=ph_win, width=window_x, height=window_y, corner_radius=15)
        ph_frame.grid(row=1, column=0)
        ph_frame = ctk.CTkFrame(master=ph_win, width=window_x, height=window_y, corner_radius=15)
        ph_frame.grid(row=1, column=0)

        def browse_file():
            print("Browsing: ")
            file_dir = filedialog.askopenfilename(initialdir="/", title="Select an Image",
                                                  filetypes=[("JPG files", ".jpg"), ("PNG files", ".png"),
                                                             ("jpeg files", ".jpeg")])
            print(file_dir)
            file_label.configure(text=file_dir)
            image1 = Image.open(file_dir)
            image1 = image1.resize((850, 400))
            test = ImageTk.PhotoImage(image1)
            test2 = asarray(image1)
            cv2.imwrite("userimg.jpg", test2)
            label_img = tkinter.Label(master=ph_frame, image=test)
            label_img.image = test
            image_frame.destroy()
            label_img.place(x=100, y=105)
            ph_win.lift()

        def filter_photo():
            print("Filter photo function")
            # Determines Color change for preset filter option
            deutranopia = round(self.d_slider.get(), 4) # unable to perceive red light
            protanopia = round(self.p_slider.get(), 4)  # unable to perceive green light
            tritanopia = round(self.t_slider.get(), 4)
            # NO CURRENT OPTION FOR A TRITANOPIA SLIDER / MUST BE MUTUALLY EXCLUSIVE FROM DUETRANOPIA AND PROTANOPIA
            print("Inputted Slider Values:" + ", d: " + str(deutranopia) + ", p: " + str(protanopia) +
                  ", t: " + str(tritanopia))

            # ------------------------------------------Matthews Code---------------------------------------------------

            def colorCorrectionDP(protanopia, deutranopia):
                return np.array([[1 - deutranopia / 2, deutranopia / 2, 0], [protanopia / 2, 1 - protanopia / 2, 0],
                                    [protanopia / 4, deutranopia / 4, 1 - (protanopia + deutranopia) / 4]]).T

            # https://ixora.io/projects/colorblindness/color-blindness-simulation-research/used for matrix
            def Tritanopia(img):
                colorblind_img = colorblind.simulate_colorblindness(img, colorblind_type='t')
                defection = img - colorblind_img
                correction = np.array([[0, 0, 0], [0.7, 1, 0], [0.7, 0, 1]])
                Daltonization = np.tensordot(defection, correction, axes=([2], [1]))
                return img + Daltonization

            user_img = Image.open("userimg.jpg")
            # imgCorrected = numpy.array(Image.open("example.jpg")) / 255
            imgCorrected = np.array(user_img) / 255
            transform = colorCorrectionDP(protanopia=protanopia, deutranopia=deutranopia)
            img_correctedPD = np.uint8(np.dot(imgCorrected, transform) * 255)
            # Correcting Image for Deutranopia with diagnosed degree of 1.0 and saving the image to file.
            imgDaltonized = Tritanopia(user_img)
            cv2.imwrite("colorchangePD.jpg", img_correctedPD)
            cv2.imwrite("colorchangeT.jpg", imgDaltonized)

            if tritanopia > 0:
                imgT = cv2.imread("colorchangeT.jpg")
                cv2.imshow("Tritanopia filtered photo", imgT)
            elif protanopia > 0 or deutranopia > 0:
                cv2.imshow("Filtered Photo", img_correctedPD)
            else:
                print("error line 540ish")

        filter_button = ctk.CTkButton(master=ph_frame, width=35, height=10, borderwidth=0, corner_radius=10,
                                      hover=True, text="Apply Filter", text_font=("Times New Roman", -25),
                                      command=filter_photo)
        label1_ph = ctk.CTkLabel(master=ph_frame, width=400, height=20, text="Browse File",
                                 text_font=("Times New Roman", -30))
        file_label = ctk.CTkLabel(master=ph_frame, width=400, height=20, text="File Name:",
                                  text_font=("Times New Roman", -20))
        file_browse_button = ctk.CTkButton(master=ph_frame, width=35, height=10, borderwidth=0, corner_radius=10,
                                           hover=True, text="Browse Files", text_font=("Times New Roman", -25),
                                           command=browse_file)
        image_frame = ctk.CTkFrame(master=ph_frame, fg_color='grey', width=850, height=400, corner_radius=0)

        val1 = round(self.d_slider.get(), 4)
        val2 = round(self.p_slider.get(), 4)
        val3 = round(self.t_slider.get(), 4)

        vals = "Filter Values: " + str(val1) + " , " + str(val2) + " , " + str(val3)

        # Slider Value Labels
        num = ctk.CTkLabel(master=ph_frame, width=10, height=10, text=vals,
                           text_font=("STIXVariants", -25))
        num.place(relx=0.25, rely=0.95, anchor=tk.CENTER)
        label1_ph.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        file_label.place(relx=0.60, rely=0.85, anchor=tk.CENTER)
        file_browse_button.place(relx=0.17, rely=0.85, anchor=tk.CENTER)
        filter_button.place(relx=0.65, rely=0.95, anchor=tk.CENTER)
        image_frame.place(relx=0.50, rely=0.50, anchor=tk.CENTER)

    def detect_color(self):
        window_x4 = 1050
        window_y4 = 650

        window_dim5 = str(window_x4) + "x" + str(window_y4)
        dc_win = ctk.CTkToplevel()
        dc_win.title("Select Filter")
        dc_win.geometry(window_dim5)
        # Main Frame
        dc_frame = ctk.CTkFrame(master=dc_win, width=window_x4, height=window_y4, corner_radius=15)
        dc_frame.grid(row=1, column=0)
        # Photo Frame
        photo_frame = ctk.CTkFrame(master=dc_frame, width=670, height=500, corner_radius=15)

        # Breakdown Frame
        breakdown_frame = ctk.CTkFrame(master=dc_frame, width=340, height=500, corner_radius=15)

        title1 = ctk.CTkLabel(master=dc_frame, width=10, height=10, text="Detect Color",
                              text_font=("Times New Roman", -55))

        label1 = ctk.CTkLabel(master=photo_frame, text="Use the following steps to breakdown the colors on a \n"
                                                       "small range on your screen. ",
                              text_font=("Times New Roman", -30))
        label2 = ctk.CTkLabel(master=photo_frame, text="1) Click the breakdown button and select a range",
                              text_font=("Times New Roman", -25))
        label3 = ctk.CTkLabel(master=photo_frame,
                                     text="2) Press the select range button and wait for breakdown to print",
                              text_font=("Times New Roman", -25))
        disc_label = ctk.CTkLabel(master=photo_frame,
                                  text= "*** Disclaimer: Do not click any RoyGBiv windows *** \n when breakdown"
                                        " is running (status: Running)", text_font=("Times New Roman", -25))

        pf_title = ctk.CTkLabel(master=breakdown_frame, text="Breakdown Printed Here",
                                text_font=("Times New Roman", -25))
        pf_status = ctk.CTkLabel(master=breakdown_frame, text="Status: Select a Range",
                                 text_font=("Times New Roman", -20))

        l_redC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_orangeC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_yellowC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_greenC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_blueC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_pinkC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_purpleC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_blackC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_whiteC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_brownC = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))

        l_red = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_orange = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_yellow = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_green = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_blue = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_pink = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_purple = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_black = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_white = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))
        l_brown = ctk.CTkLabel(master=breakdown_frame, text=" ", text_font=("Times New Roman", -16))

        label1.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        label2.place(relx=0.38, rely=0.3, anchor=tk.CENTER)
        label3.place(relx=0.49, rely=0.5, anchor=tk.CENTER)
        disc_label.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        pf_title.place(relx=0.5, rely=0.07, anchor=tk.CENTER)

        # Define Color Count Labels
        l_redC.place(relx=0.25, rely=0.3, anchor=tk.CENTER)
        l_orangeC.place(relx=0.25, rely=0.35, anchor=tk.CENTER)
        l_yellowC.place(relx=0.25, rely=0.4, anchor=tk.CENTER)
        l_greenC.place(relx=0.25, rely=0.45, anchor=tk.CENTER)
        l_blueC.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
        l_pinkC.place(relx=0.7, rely=0.3, anchor=tk.CENTER)
        l_purpleC.place(relx=0.7, rely=0.35, anchor=tk.CENTER)
        l_blackC.place(relx=0.7, rely=0.4, anchor=tk.CENTER)
        l_whiteC.place(relx=0.7, rely=0.45, anchor=tk.CENTER)
        l_brownC.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

        # Define Percent Labels
        l_red.place(relx=0.25, rely=0.6, anchor=tk.CENTER)
        l_orange.place(relx=0.25, rely=0.65, anchor=tk.CENTER)
        l_yellow.place(relx=0.25, rely=0.7, anchor=tk.CENTER)
        l_green.place(relx=0.25, rely=0.75, anchor=tk.CENTER)
        l_blue.place(relx=0.25, rely=0.8, anchor=tk.CENTER)
        l_pink.place(relx=0.7, rely=0.6, anchor=tk.CENTER)
        l_purple.place(relx=0.7, rely=0.65, anchor=tk.CENTER)
        l_black.place(relx=0.7, rely=0.7, anchor=tk.CENTER)
        l_white.place(relx=0.7, rely=0.75, anchor=tk.CENTER)
        l_brown.place(relx=0.7, rely=0.8, anchor=tk.CENTER)

        breakdown_frame.place(relx=0.82, rely=0.58, anchor=tk.CENTER)

        def breakdown():
            pf_status.configure(text="Status: \n Computing Breakdown.....Please Wait")
            # Color counter variables
            # ----------------------------------------------------------------------------------------------------------
            areaCorners = [[], []]
            rs_win = ctk.CTkToplevel()
            rs_win.overrideredirect(True)
            rs_win.geometry("400x400")

            rs_win.attributes("-alpha", 0.5)

            def moveWindow(event):
                rs_win.geometry("+" + str(event.x_root) + "+" + str(event.y_root))

            def resize_left(event):
                if rs_win.current_width + rs_win.winfo_x() - event.x_root >= 250:
                    rs_win.geometry(str(rs_win.current_width + rs_win.winfo_x() - event.x_root) + "x" + str(
                        rs_win.current_height) + "+" + str(event.x_root) + "+" + str(rs_win.winfo_y()))
                    left_side.place(x=0, y=0)
                    top_side.configure(width=rs_win.current_width)
                    bottom_side.configure(width=rs_win.current_width)
                    right_side.place(x=rs_win.current_width - 10, y=0)

            def resize_right(event):
                if rs_win.current_width - rs_win.winfo_x() + event.x_root >= 250:
                    rs_win.geometry(str(event.x_root - rs_win.winfo_x()) + "x" + str(rs_win.current_height))
                    top_side.configure(width=rs_win.current_width)
                    bottom_side.configure(width=rs_win.current_width)
                    right_side.place(x=rs_win.current_width - 10, y=0)

            def resize_top(event):
                if rs_win.current_height + rs_win.winfo_y() - event.y_root >= 75:
                    rs_win.geometry(str(rs_win.current_width) + "x" + str(
                        rs_win.current_height + rs_win.winfo_y() - event.y_root) + "+" + str(
                        rs_win.winfo_x()) + "+" + str(event.y_root))
                    top_side.place(x=0, y=0)
                    left_side.configure(height=rs_win.current_height)
                    right_side.configure(height=rs_win.current_height)
                    bottom_side.place(x=0, y=rs_win.current_height - 10)

            def resize_bottom(event):
                if rs_win.current_height - rs_win.winfo_y() + event.y_root >= 75:
                    rs_win.geometry(str(rs_win.current_width) + "x" + str(event.y_root - rs_win.winfo_y()))
                    left_side.configure(height=rs_win.current_height)
                    right_side.configure(height=rs_win.current_height)
                    bottom_side.place(x=0, y=rs_win.current_height - 10)

            def resultButton():
                global areaCorners
                areaCorners = [[rs_win.winfo_x(), rs_win.winfo_y()],
                               [rs_win.winfo_x() + rs_win.current_width, rs_win.winfo_y() + rs_win.current_height]]
                print([[rs_win.winfo_x(), rs_win.winfo_y()],
                       [rs_win.winfo_x() + rs_win.current_width, rs_win.winfo_y() + rs_win.current_height]])
                rs_win.destroy()

                # Detect color function definition
                def detect_color():
                    selectedRange = areaCorners
                    print(areaCorners)
                    # Determines the starting location of the range
                    startX = selectedRange[0][0]
                    startY = selectedRange[0][1]
                    # Determines the ending location of the range
                    endX = selectedRange[1][0]
                    endY = selectedRange[1][1]
                    # Determines the range of x of the selected range
                    xRange = endX - startX
                    # Determines the range of y of the selected range
                    yRange = endY - startY
                    # Determines how many pixels are in the selected range
                    global range_size
                    range_size = xRange * yRange
                    print(range_size)
                    # Gets the RGB values of each pixel in the range and sends it to be counted
                    for x in range(startX, endX):
                        for y in range(startY, endY):
                                rgb = PIL.ImageGrab.grab().load()[x, y]
                                name_database = webcolors.CSS3_HEX_TO_NAMES
                                names = []
                                rgb_values = []
                                for color_hex, color_name in name_database.items():
                                    names.append(color_name)
                                    rgb_values.append(hex_to_rgb(color_hex))

                                database_dt = KDTree(rgb_values)

                                distance, index = database_dt.query(rgb)
                                count_color(f'{names[index]}')

                # Count color function definition, takes variable named_color
                def count_color(named_color):
                    # Includes the global variables
                    global red_count
                    global green_count
                    global blue_count
                    global black_count
                    global gray_count
                    global purple_count
                    global yellow_count
                    global orange_count
                    global white_count
                    global brown_count
                    global pink_count
                    global count_array
                    # Shows the program is running...will be removed later
                    print("Running...")

                    # Determines what color to count the pixel towards
                    if named_color == "black":
                        black_count += 1
                    elif named_color == "silver":
                        gray_count += 1
                    elif named_color == "gray":
                        gray_count += 1
                    elif named_color == "white":
                        white_count += 1
                    elif named_color == "maroon":
                        red_count += 1
                    elif named_color == "red":
                        red_count += 1
                    elif named_color == "purple":
                        purple_count += 1
                    elif named_color == "fuchsia":
                        purple_count += 1
                    elif named_color == "green":
                        green_count += 1
                    elif named_color == "lime":
                        green_count += 1
                    elif named_color == "olive":
                        green_count += 1
                    elif named_color == "yellow":
                        yellow_count += 1
                    elif named_color == "navy":
                        blue_count += 1
                    elif named_color == "blue":
                        blue_count += 1
                    elif named_color == "teal":
                        blue_count += 1
                    elif named_color == "aqua":
                        blue_count += 1
                    elif named_color == "aliceblue":
                        blue_count += 1
                    elif named_color == "antiquewhite":
                        white_count += 1
                    elif named_color == "aquamarine":
                        blue_count += 1
                    elif named_color == "azure":
                        blue_count += 1
                    elif named_color == "beige":
                        white_count += 1
                    elif named_color == "bisque":
                        white_count += 1
                    elif named_color == "blanchealmond":
                        white_count += 1
                    elif named_color == "blueviolet":
                        purple_count += 1
                    elif named_color == "brown":
                        brown_count += 1
                    elif named_color == "burlywood":
                        brown_count += 1
                    elif named_color == "cadetblue":
                        blue_count += 1
                    elif named_color == "chartreuse":
                        green_count += 1
                    elif named_color == "chocolate":
                        brown_count += 1
                    elif named_color == "coral":
                        orange_count += 1
                    elif named_color == "cornflowerblue":
                        blue_count += 1
                    elif named_color == "cornsilk":
                        white_count += 1
                    elif named_color == "crimson":
                        red_count += 1
                    elif named_color == "cyan":
                        blue_count += 1
                    elif named_color == "darkblue":
                        blue_count += 1
                    elif named_color == "darkcyan":
                        blue_count += 1
                    elif named_color == "darkgoldenrod":
                        brown_count += 1
                    elif named_color == "darkgray":
                        gray_count += 1
                    elif named_color == "darkgreen":
                        green_count += 1
                    elif named_color == "darkkhaki":
                        yellow_count += 1
                    elif named_color == "darkmagenta":
                        purple_count += 1
                    elif named_color == "darkolivegreen":
                        green_count += 1
                    elif named_color == "darkorange":
                        orange_count += 1
                    elif named_color == "darkorchid":
                        purple_count += 1
                    elif named_color == "darkred":
                        red_count += 1
                    elif named_color == "darksalmon":
                        red_count += 1
                    elif named_color == "darkseagreen":
                        green_count += 1
                    elif named_color == "darkslateblue":
                        blue_count += 1
                    elif named_color == "darkslategray":
                        green_count += 1
                    elif named_color == "darkturquoise":
                        blue_count += 1
                    elif named_color == "darkviolet":
                        purple_count += 1
                    elif named_color == "deeppink":
                        pink_count += 1
                    elif named_color == "deepskyblue":
                        blue_count += 1
                    elif named_color == "dimgray":
                        gray_count += 1
                    elif named_color == "dodgerblue":
                        blue_count += 1
                    elif named_color == "firebrick":
                        red_count += 1
                    elif named_color == "floralwhite":
                        white_count += 1
                    elif named_color == "forestgreen":
                        green_count += 1
                    elif named_color == "gainsboro":
                        gray_count += 1
                    elif named_color == "ghostwhite":
                        white_count += 1
                    elif named_color == "gold":
                        yellow_count += 1
                    elif named_color == "goldenrod":
                        yellow_count += 1
                    elif named_color == "greenyellow":
                        green_count += 1
                    elif named_color == "honeydew":
                        green_count += 1
                    elif named_color == "hotpink":
                        pink_count += 1
                    elif named_color == "indianred":
                        red_count += 1
                    elif named_color == "indigo":
                        blue_count += 1
                    elif named_color == "ivory":
                        white_count += 1
                    elif named_color == "khaki":
                        yellow_count += 1
                    elif named_color == "lavender":
                        purple_count += 1
                    elif named_color == "lavenderblush":
                        pink_count += 1
                    elif named_color == "lawngreen":
                        green_count += 1
                    elif named_color == "lemonchiffon":
                        yellow_count += 1
                    elif named_color == "lightblue":
                        blue_count += 1
                    elif named_color == "lightcoral":
                        red_count += 1
                    elif named_color == "lightcyan":
                        blue_count += 1
                    elif named_color == "lightgoldenrodyellow":
                        yellow_count += 1
                    elif named_color == "lightgray":
                        gray_count += 1
                    elif named_color == "lightgreen":
                        green_count += 1
                    elif named_color == "lightpink":
                        pink_count += 1
                    elif named_color == "lightsalmon":
                        orange_count += 1
                    elif named_color == "lightseagreen":
                        green_count += 1
                    elif named_color == "lightskyblue":
                        blue_count += 1
                    elif named_color == "lightslategray":
                        gray_count += 1
                    elif named_color == "lightsteelblue":
                        blue_count += 1
                    elif named_color == "lightyellow":
                        yellow_count += 1
                    elif named_color == "limegreen":
                        green_count += 1
                    elif named_color == "linen":
                        white_count += 1
                    elif named_color == "magenta":
                        purple_count += 1
                    elif named_color == "mediumaquamarine":
                        green_count += 1
                    elif named_color == "mediumblue":
                        blue_count += 1
                    elif named_color == "mediumorchid":
                        purple_count += 1
                    elif named_color == "mediumpurple":
                        purple_count += 1
                    elif named_color == "mediumseagreen":
                        green_count += 1
                    elif named_color == "gainsboro":
                        gray_count += 1
                    elif named_color == "lemonchiffon":
                        yellow_count += 1
                    elif named_color == "mediumslateblue":
                        purple_count += 1
                    elif named_color == "mediumspringgreen":
                        green_count += 1
                    elif named_color == "mediumturqoise":
                        blue_count += 1
                    elif named_color == "mediumvioletred":
                        pink_count += 1
                    elif named_color == "midnightblue":
                        blue_count += 1
                    elif named_color == "mintcream":
                        white_count += 1
                    elif named_color == "mistyrose":
                        pink_count += 1
                    elif named_color == "moccasin":
                        yellow_count += 1
                    elif named_color == "navajowhite":
                        brown_count += 1
                    elif named_color == "oldlace":
                        white_count += 1
                    elif named_color == "olivedrab":
                        green_count += 1
                    elif named_color == "orangered":
                        orange_count += 1
                    elif named_color == "orchid":
                        purple_count += 1
                    elif named_color == "palegoldenrod":
                        yellow_count += 1
                    elif named_color == "palegreen":
                        green_count += 1
                    elif named_color == "paleturquoise":
                        blue_count += 1
                    elif named_color == "palevioletred":
                        pink_count += 1
                    elif named_color == "papayawhip":
                        yellow_count += 1
                    elif named_color == "peachpuff":
                        brown_count += 1
                    elif named_color == "peru":
                        brown_count += 1
                    elif named_color == "pink":
                        pink_count += 1
                    elif named_color == "rebeccapurple":
                        purple_count += 1
                    elif named_color == "rosybrown":
                        brown_count += 1
                    elif named_color == "royalblue":
                        blue_count += 1
                    elif named_color == "saddlebrown":
                        brown_count += 1
                    elif named_color == "salmon":
                        pink_count += 1
                    elif named_color == "sandybrown":
                        orange_count += 1
                    elif named_color == "seagreen":
                        green_count += 1
                    elif named_color == "seashell":
                        white_count += 1
                    elif named_color == "sienna":
                        brown_count += 1
                    elif named_color == "skyblue":
                        blue_count += 1
                    elif named_color == "slateblue":
                        blue_count += 1
                    elif named_color == "slategray":
                        gray_count += 1
                    elif named_color == "snow":
                        white_count += 1
                    elif named_color == "springgreen":
                        green_count += 1
                    elif named_color == "steelblue":
                        blue_count += 1
                    elif named_color == "tan":
                        brown_count += 1
                    elif named_color == "teal":
                        green_count += 1
                    elif named_color == "thistle":
                        purple_count += 1
                    elif named_color == "tomato":
                        red_count += 1
                    elif named_color == "turquoise":
                        blue_count += 1
                    elif named_color == "violet":
                        purple_count += 1
                    elif named_color == "wheat":
                        brown_count += 1
                    elif named_color == "whitesmoke":
                        white_count += 1
                    elif named_color == "yellowgreen":
                        green_count += 1

                # Print breakdown function definition
                def printBreakdown():
                    pf_status.configure(text="Breakdown Computed!: ")
                    # Includes the global variables
                    global red_count
                    global green_count
                    global blue_count
                    global black_count
                    global gray_count
                    global purple_count
                    global yellow_count
                    global orange_count
                    global white_count
                    global brown_count
                    global pink_count

                    count_array.append(("Red", red_count))
                    count_array.append(("Orange", orange_count))
                    count_array.append(("Yellow", yellow_count))
                    count_array.append(("Green", green_count))
                    count_array.append(("Blue", blue_count))
                    count_array.append(("Pink", pink_count))
                    count_array.append(("Purple", purple_count))
                    count_array.append(("Black", black_count))
                    count_array.append(("White", white_count))
                    count_array.append(("Brown", brown_count))

                    print("COLOR BREAKDOWN:")
                    print("Red Count: ", red_count)
                    print("Orange Count: ", orange_count)
                    print("Yellow Count: ", yellow_count)
                    print("Green Count: ", green_count)
                    print("Blue Count: ", blue_count)
                    print("Pink Count: ", pink_count)
                    print("Purple Count: ", purple_count)
                    print("Black Count: ", black_count)
                    print("White Count: ", white_count)
                    print("Brown Count: ", brown_count)

                    str1 = "Red Count: " + str(red_count)
                    str2 = "Orange Count: " + str(orange_count)
                    str3 = "Yellow Count: " + str(yellow_count)
                    str4 = "Green Count: " + str(green_count)
                    str5 = "Blue Count: " + str(blue_count)
                    str6 = "Pink Count: " + str(pink_count)
                    str7 = "Purple Count: " + str(purple_count)
                    str8 = "Black Count: " + str(black_count)
                    str9 = "White Count: " + str(white_count)
                    str10 = "Brown Count: " + str(brown_count)
                    # Prints the color breakdown
                    l_redC.configure(text=str1)
                    l_orangeC.configure(text=str2)
                    l_yellowC.configure(text=str3)
                    l_greenC.configure(text=str4)
                    l_blueC.configure(text=str5)
                    l_pinkC.configure(text=str6)
                    l_purpleC.configure(text=str7)
                    l_blackC.configure(text=str8)
                    l_whiteC.configure(text=str9)
                    l_brownC.configure(text=str10)

                # Average function definition, takes variable range_size
                def average(range_size):
                    # Includes global variables
                    global red_count
                    global yellow_count
                    global orange_count
                    global pink_count
                    global purple_count
                    global green_count
                    global white_count
                    global brown_count
                    global black_count
                    global average_array
                    # Determines the percent of each color in the selected range
                    red_average = round(((red_count / range_size) * 100), 2)
                    orange_average = round(((orange_count / range_size) * 100), 2)
                    yellow_average = round(((yellow_count / range_size) * 100), 2)
                    pink_average = round(((pink_count / range_size) * 100), 2)
                    white_average = round(((white_count / range_size) * 100), 2)
                    black_average = round(((black_count / range_size) * 100), 2)
                    blue_average = round(((blue_count / range_size) * 100), 2)
                    purple_average = round(((purple_count / range_size) * 100), 2)
                    brown_average = round(((brown_count / range_size) * 100), 2)
                    green_average = round(((green_count / range_size) * 100), 2)

                    average_array.append(("Red", red_average))
                    average_array.append(("Yellow", yellow_average))
                    average_array.append(("Pink", pink_average))
                    average_array.append(("White", white_average))
                    average_array.append(("Black", black_average))
                    average_array.append(("Blue", blue_average))
                    average_array.append(("Purple", purple_average))
                    average_array.append(("Brown", brown_average))
                    average_array.append(("Green", green_average))
                    average_array.append(("Orange", orange_average))

                    # Prints the percentages
                    print("\nCOLOR Percentage:")
                    print("Red: ", round(red_average, 2), "%")
                    print("Orange: ", round(orange_average, 2), "%")
                    print("Yellow: ", round(yellow_average, 2), "%")
                    print("Pink: ", round(pink_average, 2), "%")
                    print("White: ", round(white_average, 2), "%")
                    print("Black: ", round(black_average, 2), "%")
                    print("Blue: ", round(blue_average, 2), "%")
                    print("Purple: ", round(purple_average, 2), "%")
                    print("Brown: ", round(brown_average, 2), "%")
                    print("Green: ", round(green_average, 2), "%")

                    str1A = "Red Percent: " + str(red_average) + "%"
                    str2A = "Orange Percent: " + str(orange_average) + "%"
                    str3A = "Yellow Percent: " + str(yellow_average) + "%"
                    str4A = "Green Percent: " + str(green_average) + "%"
                    str5A = "Blue Percent: " + str(blue_average) + "%"
                    str6A = "Pink Percent: " + str(pink_average) + "%"
                    str7A = "Purple Percent: " + str(purple_average) + "%"
                    str8A = "Black Percent: " + str(black_average) + "%"
                    str9A = "White Percent: " + str(white_average) + "%"
                    str10A = "Brown Percent: " + str(brown_average) + "%"

                    l_red.configure(text=str1A)
                    l_orange.configure(text=str2A)
                    l_yellow.configure(text=str3A)
                    l_green.configure(text=str4A)
                    l_blue.configure(text=str5A)
                    l_pink.configure(text=str6A)
                    l_purple.configure(text=str7A)
                    l_black.configure(text=str8A)
                    l_white.configure(text=str9A)
                    l_brown.configure(text=str10A)

                detect_color()
                printBreakdown()
                average(range_size)

            def escClose(event):
                rs_win.destroy()

            left_side = tkinter.Frame(master=rs_win, width=10, height=rs_win.current_height, cursor="sb_h_double_arrow")
            left_side.place(x=0, y=0)
            left_side.bind('<B1-Motion>', resize_left)

            right_side = tkinter.Frame(master=rs_win, width=10, height=rs_win.current_height,
                                       cursor="sb_h_double_arrow")
            right_side.place(x=rs_win.current_width - 10, y=0)
            right_side.bind('<B1-Motion>', resize_right)

            top_side = tkinter.Frame(master=rs_win, width=rs_win.current_width, height=10, cursor="sb_v_double_arrow")
            top_side.place(x=0, y=0)
            top_side.bind('<B1-Motion>', resize_top)

            bottom_side = tkinter.Frame(master=rs_win, width=rs_win.current_width, height=10,
                                        cursor="sb_v_double_arrow")
            bottom_side.place(x=0, y=rs_win.current_height - 10)
            bottom_side.bind('<B1-Motion>', resize_bottom)

            result_button = ctk.CTkButton(master=rs_win, width=20, height=20, text="Select Range", command=resultButton)
            result_button.place(x=20, y=0)

            move_button = tkinter.Frame(master=rs_win, bg="black", width=20, height=20, cursor="fleur")
            move_button.place(x=0, y=0)
            move_button.bind('<B1-Motion>', moveWindow)

            rs_win.bind("<Escape>", lambda event: escClose(event))

            # ----------------------------------------------------------------------------------------------------------
            rs_win.mainloop()

        confirm_button = ctk.CTkButton(master=photo_frame, text="Breakdown", command=breakdown)
        confirm_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        title1.place(relx=0.5, rely=0.10, anchor=tk.CENTER)
        photo_frame.place(relx=0.33, rely=0.58, anchor=tk.CENTER)
        pf_status.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    def test_filter(self):
        print("Test Filter Selected")
        window_x4 = 1050
        window_y4 = 650

        tf_win = ctk.CTkToplevel(width=window_x4, height=window_y4)
        tf_win.title("Select Filter")

        tf_frame = ctk.CTkFrame(master=tf_win, width=window_x4, height=window_y4)
        tf_frame.grid(row=1, column=0)

        # Title Label
        title_fs = ctk.CTkLabel(master=tf_frame, text="Test Filters", text_font=("Times New Roman", -35))

        # Grab Image
        tf_win.iconbitmap('example.jpg')

        my_img = ImageTk.PhotoImage(Image.open("example.jpg"))
        lbl = tkinter.Label(master=tf_frame, image=my_img)

        # Confirm Button
        def apply():
            print("Confirm Selected")
            # Determines Color change for preset filter option
            deutranopia = round(self.d_slider.get(), 4)
            protanopia = round(self.p_slider.get(), 4)
            tritanopia = round(self.t_slider.get(), 4)
            print("Inputted Slider Values:" + ", d: " + str(deutranopia) + ", p: " + str(protanopia) +
                  ", t: " + str(tritanopia))
            # ------------------------------------------Matthews Code---------------------------------------------------

            def colorCorrectionDP(protanopia, deutranopia):
                return np.array([[1 - deutranopia / 2, deutranopia / 2, 0], [protanopia / 2, 1 - protanopia / 2, 0],
                                    [protanopia / 4, deutranopia / 4, 1 - (protanopia + deutranopia) / 4]]).T

            # https://ixora.io/projects/colorblindness/color-blindness-simulation-research/used for matrix
            def Tritanopia(img):
                colorblind_img = colorblind.simulate_colorblindness(img, colorblind_type='t')
                defection = img - colorblind_img
                correction = np.array([[0, 0, 0], [0.7, 1, 0], [0.7, 0, 1]])
                Daltonization = np.tensordot(defection, correction, axes=([2], [1]))
                return img + Daltonization

            img_corrected = np.array(Image.open("example.jpg")) / 255
            transform = colorCorrectionDP(protanopia=protanopia, deutranopia=deutranopia)
            img_correctedPD = np.uint8(np.dot(img_corrected, transform) * 255)
            # Correcting Image for Deutranopia with diagnosed degree of 1.0 and saving the image to file.
            imgDaltonized = Tritanopia(Image.open("example.jpg"))
            cv2.imwrite("colorchangePD.jpg", img_correctedPD)
            cv2.imwrite("colorchangeT.jpg", imgDaltonized)

            if tritanopia > 0:
                imgT = cv2.imread("colorchangeT.jpg")
                cv2.imshow("Tritanopia filtered photo", imgT)
                cv2.moveWindow("Tritanopia filtered photo", 500, 500)
            elif protanopia > 0 or deutranopia > 0:
                cv2.imshow("Filtered Photo", img_correctedPD)
                cv2.moveWindow("Filtered Photo", 500, 500)
            elif protanopia == 0 and deutranopia == 0 and tritanopia == 0:
                img = cv2.imread("example.jpg")
                cv2.imshow("Filtered Photo", img)
            else:
                print("error line 540ish")

        val1 = round(self.d_slider.get(), 4)
        val2 = round(self.p_slider.get(), 4)
        val3 = round(self.t_slider.get(), 4)

        vals = "Filter Values: " + str(val1) + " , " + str(val2) + " , " + str(val3)

        # Slider Value Labels
        num = ctk.CTkLabel(master=tf_frame, width=10, height=10, text=vals,
                           text_font=("STIXVariants", -25))
        num.place(relx=0.25, rely=0.85, anchor=tk.CENTER)

        sf_confirm = ctk.CTkButton(master=tf_frame, width=65, height=65, borderwidth=0, corner_radius=10, hover=True,
                                   text="Apply Filter", text_font=("Times New Roman", -25), command=apply)

        title_fs.place(relx=0.5, rely=0.08, anchor='center')
        lbl.place(relx=0.5, rely=0.43, anchor='center')

        sf_confirm.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        tf_win.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
