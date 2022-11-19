import customtkinter
import tkinter


areaCorners = [[], []]
root = customtkinter.CTk()
root.overrideredirect(True)
root.resizable(True, True)
root.geometry("400x400")

root.attributes("-alpha", 0.5)

def moveWindow(event):
    root.geometry("+" + str(event.x_root) + "+" + str(event.y_root))


def resize_left(event):
    if root.current_width + root.winfo_x() - event.x_root >= 250:
        root.geometry(str(root.current_width + root.winfo_x() - event.x_root) + "x" + str(root.current_height) + "+" + str(event.x_root) + "+" + str(root.winfo_y()))
        left_side.place(x=0, y=0)
        top_side.configure(width=root.current_width)
        bottom_side.configure(width=root.current_width)
        right_side.place(x=root.current_width - 10, y=0)


def resize_right(event):
    if root.current_width - root.winfo_x() + event.x_root >= 250:
        root.geometry(str(event.x_root - root.winfo_x()) + "x" + str(root.current_height))
        top_side.configure(width=root.current_width)
        bottom_side.configure(width=root.current_width)
        right_side.place(x=root.current_width - 10, y=0)


def resize_top(event):
    if root.current_height + root.winfo_y() - event.y_root >= 75:
        root.geometry(str(root.current_width) + "x" + str(root.current_height + root.winfo_y() - event.y_root) + "+" + str(root.winfo_x()) + "+" + str(event.y_root))
        top_side.place(x=0, y=0)
        left_side.configure(height=root.current_height)
        right_side.configure(height=root.current_height)
        bottom_side.place(x=0, y=root.current_height - 10)


def resize_bottom(event):
    if root.current_height - root.winfo_y() + event.y_root >= 75:
        root.geometry(str(root.current_width) + "x" + str(event.y_root - root.winfo_y()))
        left_side.configure(height=root.current_height)
        right_side.configure(height=root.current_height)
        bottom_side.place(x=0, y=root.current_height - 10)


def resultButton():
    areaCorners = [[root.winfo_x(), root.winfo_y()], [root.winfo_x() + root.current_width, root.winfo_y() + root.current_height]]
    print([[root.winfo_x(), root.winfo_y()], [root.winfo_x() + root.current_width, root.winfo_y() + root.current_height]])
    root.destroy()


def escClose(event):
    root.destroy()


left_side = tkinter.Frame(master=root, width=10, height=root.current_height, cursor="sb_h_double_arrow")
left_side.place(x=0, y=0)
left_side.bind('<B1-Motion>', resize_left)

right_side = tkinter.Frame(master=root, width=10, height=root.current_height, cursor="sb_h_double_arrow")
right_side.place(x=root.current_width - 10, y=0)
right_side.bind('<B1-Motion>', resize_right)

top_side = tkinter.Frame(master=root, width=root.current_width, height=10, cursor="sb_v_double_arrow")
top_side.place(x=0, y=0)
top_side.bind('<B1-Motion>', resize_top)

bottom_side = tkinter.Frame(master=root, width=root.current_width, height=10, cursor="sb_v_double_arrow")
bottom_side.place(x=0, y=root.current_height - 10)
bottom_side.bind('<B1-Motion>', resize_bottom)

result_button = customtkinter.CTkButton(master=root, width=20, height=20, text="Select Range", command=resultButton)
result_button.place(x=20, y=0)


move_button = tkinter.Frame(master=root, bg="black", width=20, height=20, cursor="fleur")
move_button.place(x=0, y=0)
move_button.bind('<B1-Motion>', moveWindow)

root.bind("<Escape>", lambda event: escClose(event))

root.mainloop()
