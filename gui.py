from tkinter import W, Button, Entry, IntVar, Label, LabelFrame, OptionMenu, Radiobutton, Tk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import functions as f

def generate_entries():
    list = frame2.grid_slaves()
    for l in list:
        l.destroy()
    n = om_n.get()
    try:
        m = int(e_m.get())
    except Exception:
        messagebox.showerror(title='Error', message='Must be an integer')
    else:
        if m < 2:
            messagebox.showerror(title='Error', message='Must be >= 2')
        else:
            for i in range(m):
                for j in range(n):
                    Entry(frame2, width=5).grid(row=i, column=j)
            for i in range(m):
                Label(frame2, text='|').grid(row=i, column=n+1)
                Entry(frame2, width=5).grid(row=i, column=n+2)

def run_alg():
    list = frame4.grid_slaves()
    for l in list:
        l.destroy()
    n = om_n.get()
    m = int(e_m.get())
    val = []
    children_widgets = frame3.winfo_children()
    for child_widget in children_widgets:
        if child_widget.winfo_class() == 'Entry':
            val.append(child_widget.get())
    val1 = []
    children_widgets = frame2.winfo_children()
    for child_widget in children_widgets:
        if child_widget.winfo_class() == 'Entry':
            val1.append(child_widget.get())
    val1 = np.array(val1)
    A = np.reshape(val1[:n*m], (m, n))
    b = np.reshape(val1[n*m:], (m))
    try:
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)
    except Exception:
        messagebox.showerror(
            title='Error', message='Matrix elements must be numbers')
    else:
        try:
            N = int(val[0])
        except Exception:
            messagebox.showerror(
                title='Error', message='Iterations must be a positive integer')
        else:
            if r.get() == 0:
                messagebox.showerror(
                    title='Error', message='Select an algorithm')
            else:
                if r.get() == 1:
                    xs, t = f.cyclic_kaczmarz(A, b, m, n, N)
                elif r.get() == 2:
                    xs, t = f.randomized_kaczmarz(A, b, m, n, N)
                elif r.get() == 3:
                    xs, t = f.Cimmino(A, b, m, n, N)
                if n == 2:
                    plot(A, b, m, n, xs)
                Label(frame4, text='Time: ', font='Helvetica 12').grid(
                    row=0, column=0)
                Label(frame4, text=str(t), font='Helvetica 10 bold').grid(
                    row=0, column=1)
                Label(frame4, text='Solution ',
                      font='Helvetica 12').grid(row=1, column=0)
                Label(frame4, text=str(xs[N]), font='Helvetica 10 bold').grid(
                    row=1, column=1)

def plot(A, b, m, n, xs):
    fig = Figure(figsize=(8, 8))
    a = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().grid(row=0, column=1, pady=10, padx=10, rowspan=4)
    dim = 3
    a.set_xlim((-dim, dim))
    a.set_ylim((-dim, dim))
    a.plot([-dim, dim], [0, 0], color='C0')
    a.plot([0, 0], [-dim, dim], color='C0')
    for i in range(m):
        x = np.linspace(-dim, dim)
        if A[i, 1] == 0:
            y = (b[i]-A[i, 0]*x)
        else:
            y = (b[i]-A[i, 0]*x)/A[i, 1]
        a.plot(x, y, color='C2')
    for j in range(len(xs)):
        a.scatter(xs[j, 0], xs[j, 1], marker='.', color='black')
        canvas.draw()
        canvas.get_tk_widget().update()

root = Tk()
root.title('Kaczmarz & Cimmino Methods')
root.geometry("1200x820")

frame1 = LabelFrame(root, text='')
frame1.grid(row=0, column=0, pady=5, padx=10)
frame2 = LabelFrame(root, text='')
frame2.grid(row=1, column=0, pady=5, padx=10)
frame3 = LabelFrame(root, text='')
frame3.grid(row=2, column=0, pady=5, padx=10)
frame4 = LabelFrame(root, text='', width=250, height=100)
frame4.grid(row=3, column=0, pady=5, padx=10)

Label(frame1, text='A:', font='Helvetica 12').grid(row=0, column=0)

e_m = Entry(frame1, width=3)
e_m.grid(row=0, column=1)

Label(frame1, text=' x ').grid(row=0, column=2)

om_n = IntVar()
om_n.set(2)
n_drop = OptionMenu(frame1, om_n, 2, 3)
n_drop.grid(row=0, column=3)

btn_im = Button(frame1, text='Input matrix', command=generate_entries)
btn_im.grid(row=1, column=0, columnspan=4, pady=10)

r = IntVar()
Radiobutton(frame3, text='Cyclic Kaczmarz', variable=r, value=1,
            font='Helvetica 12').grid(row=0, column=0, sticky=W)
Radiobutton(frame3, text='Randomized Kaczmarz', variable=r, value=2,
            font='Helvetica 12').grid(row=1, column=0, sticky=W)
Radiobutton(frame3, text='Cimmino', variable=r, value=3,
            font='Helvetica 12').grid(row=5, column=0, sticky=W)
Label(frame3, text='Iterations: ', font='Helvetica 12').grid(
    row=6, column=0, sticky=W)
e_iter = Entry(frame3, width=10).grid(row=6, column=1)
btn_start = Button(frame3, text='Start', command=run_alg)
btn_start.grid(row=7, column=0, pady=10)

root.mainloop()