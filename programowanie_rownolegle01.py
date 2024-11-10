import threading
import numpy as np
import matplotlib.pyplot as plt

from main import thread_guard

mazeSize = 90  # Rozmiar labiryntu
maze = np.zeros((mazeSize, mazeSize))
threadId = 1

# Inicjalizacja blokad dla każdego pola w labiryncie
locks = np.array([[threading.Lock() for _ in range(mazeSize)] for _ in range(mazeSize)])
guard = threading.Lock()  # Globalna blokada do synchronizacji

# Funkcja inicjalizująca labirynt z różnymi układami ścian
def initMaze():
    for i in range(mazeSize):
        for j in range(mazeSize):
            if i % 5 == 0 and j % 4 == 0:
                maze[i, j] = -1

def initMazeEx0():
    for i in range(mazeSize):
        for j in range(mazeSize):
            if i % 10 == 0 and j % 5 == 0:
                maze[i, j] = -1

def initMazeEx1():
    for i in range(mazeSize):
        for j in range(mazeSize):
            if i % 5 == 0 and j % 2 == 0:
                maze[i, j] = -1

# Funkcja sprawdzająca, czy pole jest dostępne (czy to droga)
def isPlaceFree(x, y):
    locks[x, y].acquire()
    value = maze[x, y]
    locks[x, y].release()
    return value == 0

# Funkcja aktualizująca labirynt w danym punkcie
def updateMazePlace(x, y, value):
    guard.acquire()  # Synchronizacja
    maze[x, y] = value
    guard.release()

# Funkcja odpowiadająca za przechodzenie przez labirynt
def traverseMaze(x, y, threadId):
    threads = list()  # Lista wątków
    while True:
        t0 = threading.Thread(target=updateMazePlace, args=(x, y, 1))  # Pierwszy wątek
        threads.append(t0)
        t0.start()

        possibleMoves = 0
        newX, newY = x, y

        # Sprawdzenie możliwych ruchów w labiryncie
        if possibleMoves == 0:
            # Czekamy na zakończenie wszystkich wątków
            for thread in threads:
                thread.join()
            threads.clear()  # Czyszczenie listy wątków
            break

        if newX < mazeSize and isPlaceFree(x + 1, y):
            possibleMoves += 1
            newX += 1
            t1 = threading.Thread(target=traverseMaze, args=(newX, y, 1))
            threads.append(t1)
            t1.start()
            updateMazePlace(newX, y, 1)

        if newX > 0 and isPlaceFree(x - 1, y):
            possibleMoves += 1
            newX -= 1
            t2 = threading.Thread(target=traverseMaze, args=(newX, y, 2))
            threads.append(t2)
            t2.start()
            updateMazePlace(newX, y, 2)

        if newY < mazeSize and isPlaceFree(x, y + 1):
            possibleMoves += 1
            newY += 1
            t3 = threading.Thread(target=traverseMaze, args=(x, newY, 3))
            threads.append(t3)
            t3.start()
            updateMazePlace(x, newY, 3)

        if newY > 0 and isPlaceFree(x, y - 1):
            possibleMoves += 1
            newY -= 1
            t4 = threading.Thread(target=traverseMaze, args=(x, newY, 4))
            threads.append(t4)
            t4.start()
            updateMazePlace(x, newY, 4)

        # Jeśli dostępne ruchy, uruchamiamy wątek
        if possibleMoves > 0:
            thread_guard.acquire()
            threadId += 1
            thread_guard.release()

            t = threading.Thread(target=traverseMaze, args=(x - 1, y, 6))
            threads.append(t)
            t.start()
            updateMazePlace(x - 1, y, 6)

# Funkcja zmieniająca rozmiar labiryntu
def new_maze_size(new_size):
    global maze, locks, mazeSize
    mazeSize = new_size
    maze = np.zeros((mazeSize, mazeSize))
    locks = np.array([[threading.Lock() for _ in range(mazeSize)] for _ in range(mazeSize)])
    initMaze()

# Inicjalizacja labiryntu i przejście przez niego
initMaze()
traverseMaze(1, 0, 1)

# Wizualizacja labiryntu
plt.rcParams['figure.figsize'] = (4, 4)
plt.imshow(maze, cmap="tab20")
plt.title("90x90 maze")
plt.show()

# Zmiana rozmiaru labiryntu i wizualizacja
new_maze_size(50)
plt.imshow(maze, cmap="winter")
plt.title("50x50 maze")
plt.show()

new_maze_size(200)
plt.imshow(maze, cmap="gray_r")
plt.title("200x200 maze")
plt.show()

# Nowe układy labiryntu
new_maze_size(100)
initMazeEx0()
plt.imshow(maze, cmap="cool")
plt.title("Example maze 1")
plt.show()

initMazeEx1()
plt.imshow(maze, cmap="cool")
plt.title("Example maze 2")
plt.show()
