import tkinter
import cv2
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import numpy
from PIL import Image, ImageTk

# Create root window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    name = "RoyGBiv"
    # On program Start

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

        # Display Starting Frame
        start_frame = ctk.CTkFrame(master=self, width=window_x, height=window_y, corner_radius=15)
        start_frame.grid(row=0, column=0)
        # Frame Title
        title1 = ctk.CTkLabel(master=start_frame, width=10, height=10, text="Welcome to RoyGBiv",
                              text_font=("Times New Roman", -55))
        title2 = ctk.CTkLabel(master=start_frame, width=10, height=10, text="A Screen Color Filtering Software",
                              text_font=("Times New Roman", -20))
        # Start Buttons
        screen_fill_button = ctk.CTkButton(master=start_frame, width=100, height=75, borderwidth=0, corner_radius=15,
                                           hover=True, text="Filter Your Screen", command=self.screen_filtering,
                                           text_font=("Times New Roman", -25))
        photo_fill_button = ctk.CTkButton(master=start_frame, width=100, height=75, borderwidth=0, corner_radius=15,
                                          hover=True, text="Filter a Photo", command=self.photo_filtering,
                                          text_font=("Times New Roman", -25))
        select_fill_button = ctk.CTkButton(master=start_frame, width=100, height=75, borderwidth=0, corner_radius=15,
                                           hover=True, text="Select Filter", text_font=("Times New Roman", -25),
                                           command=self.select_filter)
        detect_color_button = ctk.CTkButton(master=start_frame, width=100, height=75, borderwidth=0, corner_radius=15,
                                            hover=True, text="Detect Color", text_font=("Times New Roman", -25),
                                            command=self.detect_color)
        test_filter_button = ctk.CTkButton(master=start_frame, width=100, height=75, borderwidth=0, corner_radius=15,
                                           hover=True, text="Test Filter", command=self.test_filter,
                                           text_font=("Times New Roman", -25))

        screen_fill_button.place(relx=0.5, rely=0.58, anchor=tk.CENTER)
        photo_fill_button.place(relx=0.28, rely=0.42, anchor=tk.CENTER)
        test_filter_button.place(relx=0.28, rely=0.72, anchor=tk.CENTER)
        select_fill_button.place(relx=0.72, rely=0.42, anchor=tk.CENTER)
        detect_color_button.place(relx=0.72, rely=0.72, anchor=tk.CENTER)

        title1.place(relx=0.5, rely=0.13, anchor=tk.CENTER)
        title2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    def start(self):
        self.mainloop()
    # On closing

    def on_closing(self, event=0):
        print("Closing Window")
        self.destroy()

    # User Selects Filter
    def select_filter(self):
        print("Select Filter Selected")
        window_x = 1050
        window_y = 650

        window_dim2 = str(window_x) + "x" + str(window_y)
        fs_win = ctk.CTk()
        fs_win.title("Select Filter")
        fs_win.geometry(window_dim2)
        fs_win.resizable(False, False)

        fs_frame = ctk.CTkFrame(master=fs_win, width=window_x, height=window_y, corner_radius=15)
        fs_frame.grid(row=1, column=0)

        # Labels
        title_fs = ctk.CTkLabel(master=fs_frame, text="Select a Filter", text_font=("Times New Roman", -35))
        label1_fs = ctk.CTkLabel(master=fs_frame, width=100, height=25, text="Tune a Custom Color Filter:",
                                 text_font=("Times New Roman", -30))
        label2_fs = ctk.CTkLabel(master=fs_frame, width=100, height=25, text="Select a Preset Filter:",
                                 text_font=("Times New Roman", -30))

        label1_fs.place(relx=0.18, rely=0.2, anchor=tk.CENTER)

        # Select File Widgets
        select_filter_sf = ctk.CTkLabel(master=fs_frame, text="Select Filter: ", text_font=("Times New Roman", -35))

        filter_opt = ctk.CTkOptionMenu(master=fs_frame, width=55, height=35,
                                       values=["Saved Filter1", "Saved Filter2", "Saved Filter3",
                                               "Preset Filter1", "Preset Filter2", "Preset Filter3",
                                               "Custom Filter1", "Custom Filter2", "Custom Filter3"],
                                       corner_radius=12.5, hover=True)

        sf_set_filter_btn2 = ctk.CTkButton(master=fs_frame, width=55, height=20, borderwidth=0, corner_radius=10,
                                           hover=True, fg_color=("lightblue", "darkblue"), text="Set Filter",
                                           text_font=("Times New Roman", -25))

        # Color Sliders
        d_slider = ctk.CTkSlider(master=fs_frame, width=300, height=25, from_=0, to=1, number_of_steps=1000)
        d_slider.set(0)
        p_slider = ctk.CTkSlider(master=fs_frame, width=300, height=25, from_=0, to=1, number_of_steps=1000)
        p_slider.set(0)
        t_slider = ctk.CTkSlider(master=fs_frame, width=300, height=25, from_=0, to=1, number_of_steps=1000)
        t_slider.set(0)

        # Confirm Button
        def confirm():
            print("Confirm Selected")
            # Determines Color change for preset filter option
            d = round(d_slider.get(), 4)
            p = round(p_slider.get(), 4)
            t = round(t_slider.get(), 4)
            print("Inputted Slider Values:" +
                  ", d: " + str(d) +
                  ", p: " + str(p) +
                  ", t: " + str(t))
            # Set Slider Labels
            num_1 = ctk.CTkLabel(master=fs_frame, width=10, height=10, text=str(d),
                                 text_font=("Times New Roman", -30))
            num_2 = ctk.CTkLabel(master=fs_frame, width=10, height=10, text=str(p),
                                 text_font=("Times New Roman", -30))
            num_3 = ctk.CTkLabel(master=fs_frame, width=10, height=10, text=str(t),
                                 text_font=("Times New Roman", -30))
            num_1.place(relx=0.75, rely=0.31, anchor=tk.CENTER)
            num_2.place(relx=0.75, rely=0.43, anchor=tk.CENTER)
            num_3.place(relx=0.75, rely=0.55, anchor=tk.CENTER)

        sf_confirm = ctk.CTkButton(master=fs_frame, width=65, height=65, borderwidth=0, corner_radius=10, hover=True,
                                   text="Confirm", text_font=("Times New Roman", -25), command=confirm)

        # Slider Labels
        sl1 = ctk.CTkLabel(master=fs_frame, width=10, height=10, text="Deuteranopia",
                           text_font=("Times New Roman", -30))
        sl2 = ctk.CTkLabel(master=fs_frame, width=10, height=10, text="Protanopia",
                           text_font=("Times New Roman", -30))
        sl3 = ctk.CTkLabel(master=fs_frame, width=10, height=10, text="Tritanopia",
                           text_font=("Times New Roman", -30))

        label1_fs.place(relx=0.18, rely=0.2, anchor=tk.CENTER)
        label2_fs.place(relx=0.14, rely=0.70, anchor=tk.CENTER)
        title_fs.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        sf_confirm.place(relx=0.85, rely=0.43, anchor=tk.CENTER)

        sl1.place(relx=0.27, rely=0.31, anchor=tk.CENTER)
        sl2.place(relx=0.28, rely=0.43, anchor=tk.CENTER)
        sl3.place(relx=0.28, rely=0.55, anchor=tk.CENTER)

        filter_opt.place(relx=0.50, rely=0.8, anchor=tk.CENTER)
        select_filter_sf.place(relx=0.35, rely=0.8, anchor=tk.CENTER)
        sf_set_filter_btn2.place(relx=0.65, rely=0.8, anchor=tk.CENTER)

        d_slider.place(relx=0.5, rely=0.31, anchor=tk.CENTER)
        p_slider.place(relx=0.5, rely=0.43, anchor=tk.CENTER)
        t_slider.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        fs_win.mainloop()

    # User Selects Type of Screen Filtering
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
            rs_button.deselect()
            fs_button.state = tk.DISABLED
            # Create Range Selection window
            # Create range selection window
            rs_win = ctk.CTk()
            window_x3 = rs_win.winfo_screenwidth()
            window_y3 = rs_win.winfo_screenheight()

            window_dim4 = str(window_x3) + "x" + str(window_y3)
            rs_win.title("RoyGBiv")
            rs_win.geometry(window_dim4)
            rs_win.resizable(True, True)
            rs_win.state('zoomed')
            rs_win.attributes('-alpha', 0.7)

            # Range Selection Instructions Label
            rs_lb1 = ctk.CTkLabel(master=rs_win, width=10, height=10, text="Click and Drag to Select Screen Range",
                                  text_font=("Times New Roman", -30))
            rs_lb1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            rs_win.mainloop()

        fs_button = ctk.CTkRadioButton(master=sf_frame, text="Full screen Filter", corner_radius=6,
                                       command=fs_button_event)
        rs_button = ctk.CTkRadioButton(master=sf_frame, text="Range Selection Filter", corner_radius=6,
                                       command=rs_button_event)
        # Screen Diagram Frame
        screen_frame = ctk.CTkFrame(master=sf_frame, width=850, height=400, corner_radius=10)

        # command=pf_confirm_event2)

        screen_frame.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        title_sf.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        fs_button.place(relx=0.2, rely=0.2, anchor=tk.CENTER)
        rs_button.place(relx=0.8, rely=0.2, anchor=tk.CENTER)

        sf_win.mainloop()

    # User imports photo to filter
    def photo_filtering(self):
        print("Photo Filtering Selected")
        self.destroy()
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

            label_img = tkinter.Label(master=ph_frame, image=test)
            label_img.image = test
            image_frame.destroy()
            label_img.place(x=100, y=105)

        label1_ph = ctk.CTkLabel(master=ph_frame, width=400, height=20, text="Browse File",
                                 text_font=("Times New Roman", -30))
        file_label = ctk.CTkLabel(master=ph_frame, width=400, height=20, text="File Name:",
                                  text_font=("Times New Roman", -20))
        file_browse_button = ctk.CTkButton(master=ph_frame, width=35, height=10, borderwidth=0, corner_radius=10,
                                           hover=True, text="Browse Files", text_font=("Times New Roman", -25),
                                           command=browse_file)
        image_frame = ctk.CTkFrame(master=ph_frame, fg_color='grey', width=850, height=400, corner_radius=0)

        label1_ph.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        file_label.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
        file_browse_button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)
        image_frame.place(relx=0.50, rely=0.50, anchor=tk.CENTER)

        ph_win.mainloop()

    # Color is detected
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

    # Test Image and Filter are Demonstrated
    def test_filter(self):
        print("Test Filter Selected")
        window_x4 = 1050
        window_y4 = 650

        tf_win = tk.Toplevel(width=window_x4, height=window_y4, bg='dark grey')
        tf_win.title("Select Filter")
        tf_win.resizable(False, False)

        tf_frame = ctk.CTkFrame(master=tf_win, width=window_x4, height=window_y4, corner_radius=15)
        tf_frame.grid(row=1, column=0)

        # Title Label
        title_fs = ctk.CTkLabel(master=tf_frame, text="Test Filters", text_font=("Times New Roman", -35))

        # Grab Image
        tf_win.iconbitmap('example.jpg')

        my_img = ImageTk.PhotoImage(Image.open("example.jpg"))
        lbl = tkinter.Label(master=tf_frame, image=my_img)

        # Color Sliders
        d_slider = ctk.CTkSlider(master=tf_frame, width=300, height=25, from_=0, to=1, number_of_steps=1000)
        d_slider.set(0)
        p_slider = ctk.CTkSlider(master=tf_frame, width=300, height=25, from_=0, to=1, number_of_steps=1000)
        p_slider.set(0)
        t_slider = ctk.CTkSlider(master=tf_frame, width=300, height=25, from_=0, to=1, number_of_steps=1000)
        t_slider.set(0)

        # Slider Labels
        sl1 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text="Deuteranopia",
                           text_font=("Times New Roman", -30))
        sl2 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text="Protanopia",
                           text_font=("Times New Roman", -30))
        sl3 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text="Tritanopia",
                           text_font=("Times New Roman", -30))

        # Confirm Button
        def confirm():
            print("Confirm Selected")
            # Determines Color change for preset filter option
            deutranopia = round(d_slider.get(), 4)
            protanopia = round(p_slider.get(), 4)
            tritanopia = round(t_slider.get(), 4)
            print("Inputted Slider Values:" + ", d: " + str(deutranopia) + ", p: " + str(protanopia) +
                  ", t: " + str(tritanopia))

            # Set Slider Labels
            num_1 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text=str(deutranopia),
                                 text_font=("Times New Roman", -30))
            num_2 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text=str(protanopia),
                                 text_font=("Times New Roman", -30))
            num_3 = ctk.CTkLabel(master=tf_frame, width=10, height=10, text=str(tritanopia),
                                 text_font=("Times New Roman", -30))
            num_1.place(relx=0.75, rely=0.77, anchor=tk.CENTER)
            num_2.place(relx=0.75, rely=0.84, anchor=tk.CENTER)
            num_3.place(relx=0.75, rely=0.91, anchor=tk.CENTER)
            # ------------------------------------------Matthews Code---------------------------------------------------

            def colorCorrectionDP(protanopia, deutranopia):
                return numpy.array([[1 - deutranopia / 2, deutranopia / 2, 0], [protanopia / 2, 1 - protanopia / 2, 0],
                                    [protanopia / 4, deutranopia / 4, 1 - (protanopia + deutranopia) / 4]]).T

            def daltonizationT():
                return

            img_corrected = numpy.array(Image.open("example.jpg")) / 255
            transform = colorCorrectionDP(protanopia=protanopia, deutranopia=deutranopia)
            img_corrected = numpy.uint8(numpy.dot(img_corrected, transform) * 255)
            cv2.imwrite("colorchange.jpg", img_corrected)

            new_img = ImageTk.PhotoImage(Image.open("colorchange.jpg"))
            cv2.imshow('Filtered Test Img', img_corrected)

        sf_confirm = ctk.CTkButton(master=tf_frame, width=65, height=65, borderwidth=0, corner_radius=10, hover=True,
                                   text="Confirm", text_font=("Times New Roman", -25), command=confirm)

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
