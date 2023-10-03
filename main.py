# ========================= Libraries ========================= #
from tkinter import Tk, Button, Entry, Label
from tkinter.font import Font
from calculator import *
# ========================= Variables ========================= #
bg_color = '#121212'
fg_color = 'white'
font=('Consolas', 16)
# ========================= Functions ========================= #
def rectangle_calculate():
    try:
        width = int(rectangle_width.get())
        height = int(rectangle_height.get())

        if width and height:
            rectangle_error.config(text='') # clear error text.
            # calculat and show result
            env, area = calculate_rectangle(width, height)
            rectangle_area.config(text=f'area : {area}')
            rectangle_env.config(text=f'env  : {env}')
        else:
            rectangle_area.config(text=f'')
            rectangle_env.config(text=f'')
            rectangle_error.config(text='ERROR !')
    except:
        rectangle_area.config(text=f'')
        rectangle_env.config(text=f'')
        rectangle_error.config(text='ERROR !')


def circle_calculate():
    try:
        radius = int(circle_radius.get())
        
        if radius:
            circle_error.config(text='') # clear error text
            # calculat and show result
            env, area = calculate_circle(radius)
            circle_area.config(text=f'area : {area}')
            circle_env.config(text=f'env  : {env}')
        else:
            circle_area.config(text='')
            circle_env.config(text='')
            circle_error.config(text='ERROR !')
    except:
        circle_env.config(text='')
        circle_area.config(text='')
        circle_error.config(text='ERROR !')


def parall_calculate():
    try:
        width = int(parall_width.get())
        height = int(parall_height.get())
        h = int(parall_h.get())

        if width and height and h:
            parall_error.config(text='') # clear error text.
            # calculat and show result
            env, area = calculate_parall(width, height, h)
            parall_area.config(text=f'area : {area}')
            parall_env.config(text=f'env  : {env}')
        else:
            parall_env.config(text='')
            parall_area.config(text='')
            parall_error.config(text='ERROR !')
    except:
        parall_env.config(text='')
        parall_area.config(text='')
        parall_error.config(text='ERROR !')
# ========================= Main body ========================= #


if __name__ == "__main__":
    tk = Tk()
    tk.config(bg=bg_color)
    tk.resizable(0,0)
    tk.title('Calculator')
    tk.geometry("900x400")

    # Rectangle #
    rectangle_title = Label(tk, text='Rectangle', font=font, bg=bg_color, fg=fg_color)
    rectangle_title.place(relx=.11, rely=.2)

    rectangle_width_label = Label(tk, text='Width:', font=('consolas', 12), bg=bg_color, fg=fg_color)
    rectangle_width_label.place(relx=.03, rely=.3)

    rectangle_height_label = Label(tk, text='Height:', font=('consolas', 12), bg=bg_color, fg=fg_color)
    rectangle_height_label.place(relx=.025, rely=.4)

    rectangle_width = Entry(tk, bg=bg_color, fg=fg_color, font=font, width=10)
    rectangle_width.place(relx=.1, rely=0.3)

    rectangle_height = Entry(tk, bg=bg_color, fg=fg_color, font=font, width=10)
    rectangle_height.place(relx=.1, rely=0.4)

    rectangle_btn = Button(tk, text='Calculate', command=rectangle_calculate, font=font, bg=bg_color, fg=fg_color, padx=6)
    rectangle_btn.place(relx=.1, rely=0.5)

    rectangle_area = Label(tk, text='', bg=bg_color, fg='green', font=font)
    rectangle_area.place(relx=.1, rely=.7)

    rectangle_env = Label(tk, text='', bg=bg_color, fg='green', font=font)
    rectangle_env.place(relx=.1, rely=.8)

    rectangle_error = Label(tk, text='', bg=bg_color, fg='red', font=font)
    rectangle_error.place(relx=.12, rely=.75)

    # Circle #
    circle_title = Label(tk, text='Circle', font=font, bg=bg_color, fg=fg_color)
    circle_title.place(relx=.4, rely=.2)

    circle_radius_label = Label(tk, text='Radius:', font=('consolas', 12), bg=bg_color, fg=fg_color)
    circle_radius_label.place(relx=.3, rely=.3)

    circle_radius = Entry(tk, bg=bg_color, fg=fg_color, font=font, width=10)
    circle_radius.place(relx=.38, rely=0.3)

    circle_btn = Button(tk, text='Calculate', command=circle_calculate, font=font, bg=bg_color, fg=fg_color, padx=6)
    circle_btn.place(relx=.38, rely=0.5)

    circle_area = Label(tk, text='', bg=bg_color, fg='green', font=font)
    circle_area.place(relx=.38, rely=.7)

    circle_env = Label(tk, text='', bg=bg_color, fg='green', font=font)
    circle_env.place(relx=.38, rely=.8)

    circle_error = Label(tk, text='', bg=bg_color, fg='red', font=font)
    circle_error.place(relx=.41, rely=.75)

    # Parallelogram #
    parall_title = Label(tk, text='Parall', font=font, bg=bg_color, fg=fg_color)
    parall_title.place(relx=.65, rely=.2)

    parall_width_label = Label(tk, text='Width:', font=('consolas', 12), bg=bg_color, fg=fg_color)
    parall_width_label.place(relx=.54, rely=.3)

    parall_height_label = Label(tk, text='Height:', font=('consolas', 12), bg=bg_color, fg=fg_color)
    parall_height_label.place(relx=.53, rely=.4)

    parall_h_label = Label(tk, text='H :', font=('consolas', 14), bg=bg_color, fg=fg_color)
    parall_h_label.place(relx=.56, rely=.5)

    parall_width = Entry(tk, bg=bg_color, fg=fg_color, font=font, width=10)
    parall_width.place(relx=.62, rely=0.3)

    parall_height = Entry(tk, bg=bg_color, fg=fg_color, font=font, width=10)
    parall_height.place(relx=.62, rely=0.4)

    parall_h = Entry(tk, bg=bg_color, fg=fg_color, font=font, width=10)
    parall_h.place(relx=.62, rely=0.5)

    parall_btn = Button(tk, text='Calculate', command=parall_calculate, font=font, bg=bg_color, fg=fg_color, padx=6)
    parall_btn.place(relx=.62, rely=0.6)

    parall_area = Label(tk, text='', bg=bg_color, fg='green', font=font)
    parall_area.place(relx=.63, rely=.75)

    parall_env = Label(tk, text='', bg=bg_color, fg='green', font=font)
    parall_env.place(relx=.63, rely=.85)

    parall_error = Label(tk, text='', bg=bg_color, fg='red', font=font)
    parall_error.place(relx=.65, rely=.79)
    tk.mainloop()