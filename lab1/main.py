from genetic import *
import tkinter as tk
import time


class GUI():
    def __init__(self, root):
        self.root=root
        self.entry = tk.Entry(root)
        self.start = False
        stvar=tk.StringVar()
        stvar.set("one")

        self.canvas=tk.Canvas(root, width=600, height=800, background='white')
        self.canvas.grid(row=0,column=1)

        frame = tk.Frame(self.root)
        frame.grid(row=0,column=0, sticky="n")

        self.points_amount = tk.IntVar()
        self.entry1 = tk.Entry(frame, textvariable=self.points_amount).grid(row = 1,column = 1,sticky = tk.E+ tk.W)

        self.population_size = tk.IntVar()
        self.entry2 = tk.Entry(frame, textvariable=self.population_size).grid(row = 2,column = 1, sticky = tk.E)

        Button1=tk.Button(frame,text="Start", command=self._start_handler).grid(row = 3,column = 1, sticky = "we")

    def _start_handler(self):
        perform(self)

    def draw_line(self, p1, p2):
        self.canvas.create_line(p1.x, p1.y, p2.x, p2.y,
                                fill="#05f")

    def draw_circle(self, p):
        self.canvas.create_oval(p.x, p.y, p.x+10, p.y+10,
                                fill="#05f")



def perform(app):
    population_size = app.population_size.get()
    points = create_points(app.points_amount.get())
    population = create_population(points, population_size)



    while fit_function(sorted(population)[0]) > 1000:
        app.canvas.delete("all")

        combs = selection(population, population_size)
        population = create_new_population(combs)
        s_p = sorted(population)

        for p in points:
            app.draw_circle(p)

        for i in range(len(s_p[0])-1):
            app.draw_line(s_p[0][i], s_p[0][i+1])

        app.root.update()
        time.sleep(0.1)




def main():
    root = tk.Tk()
    app = GUI(root)


    root.mainloop()




if __name__ == '__main__':
    main()
