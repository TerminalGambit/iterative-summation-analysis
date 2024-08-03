import random
import tkinter as tk

SIZE = 5
RANGE_TUPLE = (1, 10)

matrix = [
    [0 for _ in range(SIZE)] for _ in range(SIZE)
]

def initialize_matrix(mode="normal"):
    global matrix
    matrix[0][0] = random.randint(*RANGE_TUPLE)
    matrix[0][1] = random.randint(*RANGE_TUPLE)
    matrix[1][0] = random.randint(*RANGE_TUPLE)
    matrix[1][1] = random.randint(*RANGE_TUPLE)
    if mode == "debug":
        for i in range(SIZE):
            for j in range(SIZE):
                print(f"Matrix[{i}][{j}]: {matrix[i][j]}")
    else:
        print("Matrix initialized successfully!")

def matrix_printer(given_matrix):
    nums = 6
    for i in range(len(given_matrix)):
        print("-" * len(given_matrix[i]) * nums)
        for j in range(len(given_matrix[i])):
            cell_display = str(given_matrix[i][j]).center(5)
            print("|", end="")
            print(cell_display, end="")
        print("|")
    print("-" * len(given_matrix[0]) * nums)
    print()

def progress():
    global matrix
    # Update rows
    for i in range(SIZE):
        for j in range(SIZE):
            if matrix[i][j] == 0:
                matrix[i][j] = sum(matrix[i][:j])
                break  # Move to the next row after updating

    # Update columns
    for j in range(SIZE):
        for i in range(SIZE):
            if matrix[i][j] == 0:
                matrix[i][j] = sum(row[j] for row in matrix[:i])
                break  # Move to the next column after updating

class Grid:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Matrix")
        self.window.geometry("700x700")
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.draw_grid()
        self.button = tk.Button(self.window, text="Next", command=self.next, width=20, height=2)
        self.button.pack()
        self.button1 = tk.Button(self.window, text="Exit", command=self.exiting, width=20, height=2)
        self.button1.pack()
        self.isFirst = True  # Ensure this is properly initialized here
        self.window.mainloop()

    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(SIZE):
            self.canvas.create_line(0, i * 100, 500, i * 100)
            self.canvas.create_line(i * 100, 0, i * 100, 500)
        for i in range(SIZE):
            for j in range(SIZE):
                x = i * 100
                y = j * 100
                self.canvas.create_text(x + 50, y + 50, text=matrix[i][j], font=("Helvetica", 20))

    def next(self):
        if self.isFirst:
            initialize_matrix()
            self.isFirst = False  # Update the state after initialization
        else:
            progress()
        self.draw_grid()

    def exiting(self):
        self.window.destroy()


if __name__ == "__main__":
    Grid()
