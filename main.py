from tkinter import *

root = Tk()
root.title("Pythonicway Minesweep")
button1 = Button(root, text='Новачок', width=25, height=5, bg='green', fg='black', font='times new roman 14')
button2 = Button(root, text='Любитель', width=25, height=5, bg='green', fg='black', font='times new roman 14')
button3 = Button(root, text='Професіонал', width=25, height=5, bg='green', fg='black', font='times new roman 14')
button1.pack()
button2.pack()
button3.pack()
button1 = Button(root1)
# новачок
grid_size1 = 9
square_size1 = 9
mines_num1 = 10
root1 = Tk()
root1.title("")
a = Canvas(root1, width1=grid_size1 * square_size1, height1=grid_size1 * square_size1)
a.pack()
for i in range(grid_size1):
    for j in range(grid_size1):
        a.create_rectangle1(i * square_size1, j * square_size1, i * square_size1 + square_size1,
                            j * square_size1 + square_size1, fill='gray')
root1.mainloop()
# любитель
grid_size2 = 16
square_size2 = 16
mines_num2 = 40
root2 = Tk()
root2.title("")
b = Canvas(root2, width2=grid_size2 * square_size2, height2=grid_size2 * square_size2)
b.pack()
for i in range(grid_size2):
    for j in range(grid_size2):
        b.create_rectangle2(i * square_size2, j * square_size2, i * square_size2 + square_size2,
                            j * square_size2 + square_size2, fill='gray')
root2.mainloop()
# професіонал
grid_size3 = 16
square_size3 = 30
mines_num3 = 90
root3 = Tk()
root3.title("")
c = Canvas(root3, width3=grid_size3 * square_size3, height3=grid_size3 * square_size3)
c.pack()
for i in range(grid_size3):
    for j in range(grid_size3):
        c.create_rectangle3(i * square_size3, j * square_size3, i * square_size3 + square_size3,
                            j * square_size3 + square_size3, fill='gray')
root3.mainloop()
