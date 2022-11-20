import tkinter
import cv2
import customtkinter as ctk
import tkinter as tk
import numpy as np
from PIL import Image, ImageTk


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

        instructions = ctk.CTkLabel(master=self.instruct_frame, text="Place Instructions here",
                                    text_font=("STIXVariants", -15))
        instructions.place(relx=0.2, rely=0.25, anchor=tk.CENTER)

        # Button Frame
        screen_fill_button = ctk.CTkButton(master=self.button_frame, width=110, height=75, corner_radius=15, hover=True,
                                           text="Filter Your Screen", command=self.screen_filtering,
                                           text_font=("STIXVariants", -20))
        photo_fill_button = ctk.CTkButton(master=self.button_frame, width=110, height=75, corner_radius=15, hover=True,
                                          text="Filter a Photo", command=self.photo_filtering,
                                          text_font=("STIXVariants", -20))
        detect_color_button = ctk.CTkButton(master=self.button_frame, width=110, height=75, corner_radius=15,
                                            hover=True, text="Detect Color", text_font=("STIXVariants", -20),
                                            command=self.detect_color)
        test_filter_button = ctk.CTkButton(master=self.button_frame, width=110, height=75, corner_radius=15,
                                           hover=True, text="Test Filter", command=self.test_filter,
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
            label_value1 = round(d_slider.get(), 4)
            num_1.configure(text=str(label_value1))

        def slider_action2(label_value2):
            label_value2 = round(p_slider.get(), 4)
            num_2.configure(text=str(label_value2))

        def slider_action3(label_value):
            label_value3 = round(t_slider.get(), 4)
            num_3.configure(text=str(label_value3))

        d_slider = ctk.CTkSlider(master=self.filter_frame, width=250, height=25, from_=0, to=1, number_of_steps=1000,
                                 command=slider_action1)
        d_slider.set(0)
        p_slider = ctk.CTkSlider(master=self.filter_frame, width=250, height=25, from_=0, to=1, number_of_steps=1000,
                                 command=slider_action2)
        p_slider.set(0)
        t_slider = ctk.CTkSlider(master=self.filter_frame, width=250, height=25, from_=0, to=1, number_of_steps=1000,
                                 command=slider_action3)
        t_slider.set(0)
        d_slider.place(relx=0.61, rely=0.32, anchor=tk.CENTER)
        p_slider.place(relx=0.61, rely=0.47, anchor=tk.CENTER)
        t_slider.place(relx=0.61, rely=0.62, anchor=tk.CENTER)

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
            d_slider.set(float(vals[0]))
            p_slider.set(float(vals[1]))
            t_slider.set(float(vals[2]))

        saved_filters_names = np.loadtxt("test saved filter.txt", usecols=0, dtype=str)
        label2_fs = ctk.CTkLabel(master=self.filter_frame, width=100, height=25, text="Select a Saved Filter:",
                                 text_font=("STIXVariants", -25))
        var = tkinter.StringVar()
        filter_opt = ctk.CTkOptionMenu(master=self.filter_frame, width=205, height=35, variable=var,
                                       values=saved_filters_names, corner_radius=10, hover=True, command=option)
        filter_opt.place(relx=0.72, rely=0.75, anchor=tk.CENTER)
        label2_fs.place(relx=0.25, rely=0.75, anchor=tk.CENTER)

        def save():
            # saves filter name and values
            d = round(d_slider.get(), 4)
            p = round(p_slider.get(), 4)
            t = round(t_slider.get(), 4)
            num_1.configure(text=str(d))
            num_2.configure(text=str(p))
            num_3.configure(text=str(t))
            save_win = ctk.CTk()
            save_win.title("Save Current Filter")
            save_win.geometry("600x200")
            save_win.resizable(False, False)
            save_frame = ctk.CTkFrame(master=save_win, width=600, height=200, corner_radius=10)
            save_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            values = [round(d_slider.get(), 4), round(p_slider.get(), 4), round(t_slider.get(), 4)]
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
                data_format1 = name_entry.get() + " " + val_str
                data_format = data_format1.replace('[', '').replace(']', '')
                file = open("test saved filter.txt", "a")
                file.write("\n")
                file.write(data_format)
                file.close()
                name_label.configure(text="Filter saved successfully")

            sf_save = ctk.CTkButton(master=save_frame, width=65, height=35, borderwidth=0, corner_radius=10,
                                    hover=True, text="Confirm", text_font=("STIXVariants", -20), command=save_to_file)
            sf_save.place(relx=0.9, rely=0.5, anchor=tk.CENTER)
            save_win.mainloop()

        ff_save = ctk.CTkButton(master=self.filter_frame, width=65, height=45, borderwidth=0, corner_radius=10,
                                hover=True, text="Save Filter", text_font=("STIXVariants", -25), command=save)
        ff_save.place(relx=0.2, rely=0.9, anchor=tk.CENTER)

        # Confirm Filter inputs
        def confirm():
            # Zero out slider labels
            num_1.configure(text=str(0))
            num_2.configure(text=str(0))
            num_3.configure(text=str(0))
            print("Confirm Selected")
            # Get inputs
            d = round(d_slider.get(), 4)
            p = round(p_slider.get(), 4)
            t = round(t_slider.get(), 4)
            print("Inputted Slider Values:" +
                  ", d: " + str(d) +
                  ", p: " + str(p) +
                  ", t: " + str(t))
            # Set Slider Labels
            num_1.configure(text=str(d))
            num_2.configure(text=str(p))
            num_3.configure(text=str(t))

        ff_confirm = ctk.CTkButton(master=self.filter_frame, width=65, height=45, borderwidth=0, corner_radius=10,
                                   hover=True, text="Confirm", text_font=("STIXVariants", -25), command=confirm)
        ff_confirm.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

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
        sf_win.resizable(False, False)

        sf_frame = ctk.CTkFrame(master=sf_win, width=window_x, height=window_y, corner_radius=15)
        sf_frame.grid(row=1, column=0)

        # Frame Label
        title_sf = ctk.CTkLabel(master=sf_frame, text="Screen Filtering", text_font=("Times New Roman", -35))

        # Buttons
        # Full Screen Selection Event
        def fs_button_event():
            fs_button.deselect()
            screen_frame.configure(bg_color='grey', fg_color='grey')
            rs_button.state = tk.DISABLED
            # Create Full Screen Filter Window
            rs_win = ctk.CTk()
            window_x2 = rs_win.winfo_screenwidth()
            window_y2 = rs_win.winfo_screenheight()

            window_dim3 = str(window_x2) + "x" + str(window_y2)
            rs_win.title("RoyGBiv")
            rs_win.geometry(window_dim3)
            rs_win.resizable(True, True)
            rs_win.state('zoomed')
            rs_win.attributes('-alpha', 0.7)

            # Range Selection Instructions Label
            rs_lb1 = ctk.CTkLabel(master=rs_win, width=10, height=10, text="Filter Placed Here",
                                  text_font=("Times New Roman", -30))
            rs_lb1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            rs_win.mainloop()

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
        ph_win = ctk.CTk()
        ph_win.title("Filter a Photo")
        ph_win.geometry(window_dim2)
        ph_win.resizable(False, False)
        # Create Frame
        ph_frame = ctk.CTkFrame(master=ph_win, width=window_x, height=window_y, corner_radius=15)
        ph_frame.grid(row=1, column=0)
        # Label Frame
        label1_ph = ctk.CTkLabel(master=ph_frame, text="Import Photo", text_font=("Times New Roman", -35))
        # Image Frame
        img_frame = ctk.CTkFrame(master=ph_frame, width=850, height=400, corner_radius=0)

        # Entry Label
        label2_ph = ctk.CTkLabel(master=ph_frame, text="Select Photo:", text_font=("Times New Roman", -30))

        # File Entry Box
        def import_photo():
            print("Importing: " + file_name.get())

        file_name = ctk.CTkEntry(master=ph_frame, placeholder_text="Select File:", width=400, height=40,
                                 corner_radius=10)
        file_confirm_button = ctk.CTkButton(master=ph_frame, width=35, height=10, borderwidth=0, corner_radius=10,
                                            hover=True, text="Confirm", text_font=("Times New Roman", -25),
                                            command=import_photo)
        file_confirm_button.place(relx=0.80, rely=0.9, anchor=tk.CENTER)
        file_name.place(relx=0.53, rely=0.90, anchor=tk.CENTER)
        label2_ph.place(relx=0.25, rely=0.90, anchor=tk.CENTER)
        img_frame.place(relx=0.50, rely=0.50, anchor=tk.CENTER)
        label1_ph.place(relx=0.50, rely=0.10, anchor=tk.CENTER)
        ph_win.mainloop()
        return file_name

    def detect_color(self):
        print("Select Filter Selected")
        window_x4 = 1050
        window_y4 = 650

        window_dim5 = str(window_x4) + "x" + str(window_y4)
        dc_win = ctk.CTk()
        dc_win.title("Select Filter")
        dc_win.geometry(window_dim5)
        dc_win.resizable(False, False)
        # Main Frame
        dc_frame = ctk.CTkFrame(master=dc_win, width=window_x4, height=window_y4, corner_radius=15)
        dc_frame.grid(row=1, column=0)
        # Photo Frame
        photo_frame = ctk.CTkFrame(master=dc_frame, width=750, height=425, corner_radius=15)
        # Apply Filter Radio Button

        filter_opt = ctk.CTkOptionMenu(master=dc_frame, width=55, height=35,
                                       values=["Saved Filter1", "Saved Filter2", "Saved Filter3",
                                               "Preset Filter1", "Preset Filter2", "Preset Filter3",
                                               "Custom Filter1", "Custom Filter2", "Custom Filter3"],
                                       corner_radius=12.5, hover=True)

        def dc_apply_filter():
            print("Apply Filter to Test img")
            apply_button.deselect()

        apply_button = ctk.CTkRadioButton(master=dc_frame, width=25, height=25, text="Apply Filter", corner_radius=6,
                                          command=dc_apply_filter, text_font=("Times New Roman", -20))

        title1 = ctk.CTkLabel(master=dc_frame, width=10, height=10, text="Detect Color",
                              text_font=("Times New Roman", -55))

        filter_opt.place(relx=0.45, rely=0.9, anchor=tk.CENTER)
        apply_button.place(relx=0.6, rely=0.9, anchor=tk.CENTER)
        title1.place(relx=0.5, rely=0.10, anchor=tk.CENTER)
        photo_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        dc_win.mainloop()

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

        # Filter Sliders
        def slider_action1(label_value1):
            label_value1 = round(d_slider.get(), 4)
            num_1.configure(text=str(label_value1))

        def slider_action2(label_value2):
            label_value2 = round(p_slider.get(), 4)
            num_2.configure(text=str(label_value2))

        def slider_action3(label_value):
            label_value3 = round(t_slider.get(), 4)
            num_3.configure(text=str(label_value3))

        d_slider = ctk.CTkSlider(master=tf_win, width=250, height=25, from_=0, to=1, number_of_steps=1000,
                                 command=slider_action1)
        d_slider.set(0)
        p_slider = ctk.CTkSlider(master=tf_win, width=250, height=25, from_=0, to=1, number_of_steps=1000,
                                 command=slider_action2)
        p_slider.set(0)
        t_slider = ctk.CTkSlider(master=tf_win, width=250, height=25, from_=0, to=1, number_of_steps=1000,
                                 command=slider_action3)
        t_slider.set(0)

        # Slider Labels
        sl1 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text="Deuteranopia",
                           text_font=("STIXVariants", -30))
        sl2 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text="Protanopia",
                           text_font=("STIXVariants", -30))
        sl3 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text="Tritanopia",
                           text_font=("STIXVariants", -30))
        num_1 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text=str(0),
                             text_font=("STIXVariants", -25))
        num_2 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text=str(0),
                             text_font=("STIXVariants", -25))
        num_3 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text=str(0),
                             text_font=("STIXVariants", -25))
        num_1.place(relx=0.68, rely=0.77, anchor=tk.CENTER)
        num_2.place(relx=0.68, rely=0.84, anchor=tk.CENTER)
        num_3.place(relx=0.68, rely=0.91, anchor=tk.CENTER)

        # Confirm Button
        def apply():
            print("Confirm Selected")
            # Determines Color change for preset filter option
            deutranopia = round(d_slider.get(), 4)
            protanopia = round(p_slider.get(), 4)
            tritanopia = round(t_slider.get(), 4)
            print("Inputted Slider Values:" + ", d: " + str(deutranopia) + ", p: " + str(protanopia) +
                  ", t: " + str(tritanopia))
            # ------------------------------------------Matthews Code---------------------------------------------------

            def colorCorrectionDP(protanopia, deutranopia):
                return np.array([[1 - deutranopia / 2, deutranopia / 2, 0], [protanopia / 2, 1 - protanopia / 2, 0],
                                    [protanopia / 4, deutranopia / 4, 1 - (protanopia + deutranopia) / 4]]).T

            def daltonizationT():
                return

            img_corrected = np.array(Image.open("example.jpg")) / 255
            transform = colorCorrectionDP(protanopia=protanopia, deutranopia=deutranopia)
            img_corrected = np.uint8(np.dot(img_corrected, transform) * 255)
            cv2.imwrite("colorchange.jpg", img_corrected)

            new_img = ImageTk.PhotoImage(Image.open("colorchange.jpg"))
            cv2.imshow('Filtered Test Img', img_corrected)

        sf_confirm = ctk.CTkButton(master=tf_frame, width=65, height=65, borderwidth=0, corner_radius=10, hover=True,
                                   text="Confirm", text_font=("Times New Roman", -25), command=apply)

        title_fs.place(relx=0.5, rely=0.08, anchor='center')
        lbl.place(relx=0.5, rely=0.43, anchor='center')

        sl1.place(relx=0.27, rely=0.77, anchor=tk.CENTER)
        sl2.place(relx=0.28, rely=0.84, anchor=tk.CENTER)
        sl3.place(relx=0.28, rely=0.91, anchor=tk.CENTER)
        sf_confirm.place(relx=0.85, rely=0.84, anchor=tk.CENTER)

        d_slider.place(relx=0.5, rely=0.77, anchor=tk.CENTER)
        p_slider.place(relx=0.5, rely=0.84, anchor=tk.CENTER)
        t_slider.place(relx=0.5, rely=0.91, anchor=tk.CENTER)

        tf_win.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
