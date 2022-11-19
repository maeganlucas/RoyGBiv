import customtkinter
import tkinter


areaCorners = [[], []]
rs_win = customtkinter.CTk()
rs_win.overrideredirect(True)
rs_win.resizable(True, True)
rs_win.geometry("400x400")

rs_win.attributes("-alpha", 0.5)

def moveWindow(event):
    rs_win.geometry("+" + str(event.x_root) + "+" + str(event.y_root))


def resize_left(event):
    if rs_win.current_width + rs_win.winfo_x() - event.x_root >= 250:
        rs_win.geometry(str(rs_win.current_width + rs_win.winfo_x() - event.x_root) + "x" + str(rs_win.current_height) + "+" + str(event.x_root) + "+" + str(rs_win.winfo_y()))
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
        rs_win.geometry(str(rs_win.current_width) + "x" + str(rs_win.current_height + rs_win.winfo_y() - event.y_root) + "+" + str(rs_win.winfo_x()) + "+" + str(event.y_root))
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
    areaCorners = [[rs_win.winfo_x(), rs_win.winfo_y()], [rs_win.winfo_x() + rs_win.current_width, rs_win.winfo_y() + rs_win.current_height]]
    print([[rs_win.winfo_x(), rs_win.winfo_y()], [rs_win.winfo_x() + rs_win.current_width, rs_win.winfo_y() + rs_win.current_height]])
    rs_win.destroy()


def escClose(event):
    rs_win.destroy()


left_side = tkinter.Frame(master=rs_win, width=10, height=rs_win.current_height, cursor="sb_h_double_arrow")
left_side.place(x=0, y=0)
left_side.bind('<B1-Motion>', resize_left)

right_side = tkinter.Frame(master=rs_win, width=10, height=rs_win.current_height, cursor="sb_h_double_arrow")
right_side.place(x=rs_win.current_width - 10, y=0)
right_side.bind('<B1-Motion>', resize_right)

top_side = tkinter.Frame(master=rs_win, width=rs_win.current_width, height=10, cursor="sb_v_double_arrow")
top_side.place(x=0, y=0)
top_side.bind('<B1-Motion>', resize_top)

bottom_side = tkinter.Frame(master=rs_win, width=rs_win.current_width, height=10, cursor="sb_v_double_arrow")
bottom_side.place(x=0, y=rs_win.current_height - 10)
bottom_side.bind('<B1-Motion>', resize_bottom)

result_button = customtkinter.CTkButton(master=rs_win, width=20, height=20, text="Select Range", command=resultButton)
result_button.place(x=20, y=0)


move_button = tkinter.Frame(master=rs_win, bg="black", width=20, height=20, cursor="fleur")
move_button.place(x=0, y=0)
move_button.bind('<B1-Motion>', moveWindow)

rs_win.bind("<Escape>", lambda event: escClose(event))

rs_win.mainloop()
