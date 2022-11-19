import tkinter
import cv2
import customtkinter as ctk
import tkinter as tk
import numpy
from PIL import Image, ImageTk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    name = "RoyGBiv"

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

        screen_fill_button.place(relx=0.50, rely=0.27, anchor=tk.CENTER)
        photo_fill_button.place(relx=0.50, rely=0.42, anchor=tk.CENTER)
        select_fill_button.place(relx=0.50, rely=0.57, anchor=tk.CENTER)
        detect_color_button.place(relx=0.50, rely=0.72, anchor=tk.CENTER)
        test_filter_button.place(relx=0.50, rely=0.87, anchor=tk.CENTER)

        title1.place(relx=0.5, rely=0.10, anchor=tk.CENTER)
        title2.place(relx=0.5, rely=0.18, anchor=tk.CENTER)

    def start(self):
        self.mainloop()

    def on_closing(self, event=0):
        print("Closing Window")
        self.destroy()

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
            # ------------------------------------- Connal's Code -------------------------------------------------------
            areaCorners = [[], []]
            rs_win = ctk.CTk()
            rs_win.overrideredirect(True)
            rs_win.resizable(True, True)
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
        screen_frame = ctk.CTkFrame(master=sf_frame, width=850, height=400, corner_radius=10)

        # command=pf_confirm_event2)

        screen_frame.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        title_sf.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        fs_button.place(relx=0.2, rely=0.2, anchor=tk.CENTER)
        rs_button.place(relx=0.8, rely=0.2, anchor=tk.CENTER)

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
        def apply():
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
