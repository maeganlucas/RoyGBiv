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
    old_left = root.winfo_x()
    root.geometry("+" + str(event.x_root) + "+" + str(root.winfo_y()))
    root.geometry(str(root.current_width + old_left - event.x_root) + "x" + str(root.current_height))
    left_side.place(x=0, y=0)
    right_side.place(x=root.current_width - 10, y=0)


def resize_right(event):
    root.geometry(str(event.x_root) + "x" + str(root.current_height))
    right_side.place(x=root.current_width - 10, y=0)


def resize_top(event):
    old_top = root.winfo_y()
    root.geometry("+" + str(root.winfo_x()) + "+" + str(event.y_root))
    root.geometry(str(root.current_width) + "x" + str(root.current_height + old_top - event.y_root))
    top_side.place(x=0, y=0)
    bottom_side.place(x=0, y=root.current_height - 10)


def resize_bottom(event):
    root.geometry(str(root.current_width) + "x" + str(event.y_root))
    bottom_side.place(x=0, y=root.current_height - 10)


def resultButton():
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
