
import threading ##zaimportowanie biblioteki threading, ten moduł konstruuje interfejsy wątków
from matplotlib import pyplot as plt ##biblioteka umożliwia tworzenie wykresu
import numpy as np ## umożliwia operacje na macierzach, tablicach

mazeSize = int(100)
maze = np.zeros((mazeSize, mazeSize))
threadId = int(1)

locks = np.array([[threading.Lock() for j in range(mazeSize)] for i in range(mazeSize)])
guard = threading.Lock()
thread_guard = threading.Lock()

# - 1 wall, 0 - road
def initMaze(): ## inicjalizacja ścian labiryntu, funkcja z dokumentacji, -1 wall i 0 road
    for i in range(mazeSize):
        for j in range(mazeSize):
            if i % 5 == 0 and j % 4 == 0:
                maze[i, j] = -1

def initMazeEx1():
    for i in range(mazeSize):
        for j in range(mazeSize):
            if i % 10 == 0 and j % 9 == 0:
                maze[i, j] = -1
def initMazeEx2():
    for i in range(mazeSize):
        for j in range(mazeSize):
            if i % 3 == 0 and j % 4 == 0:
                maze[i, j] = -1
def initMazeEx3():
    for i in range(mazeSize):
        for j in range(mazeSize):
            if i % 33 == 0 and j % 6 == 0:
                maze[i, j] = -1

def isPlaceFree(x, y): ## sprawdzenie dostępnych pól
    locks[x, y].acquire()
    value = maze[x, y]
    locks[x, y].release()
    return value == 0

def updateMazePlace(x, y, value): ## aktualizacja pola
    guard.acquire()
    maze[x, y] = value
    guard.release()

def traverseMaze(x, y, threadId): ## przechodzenie krok po kroku w labiryncie

    threads = list()  ## lista z wątkami
    while True:
        # aktualizacja pola labiryntu
        t1 = threading.Thread(target=updateMazePlace, args=(x, y, 1))
        threads.append(t1)
        t1.start()
        possibleMoves = 0
        newX, newY = x, y
        # sprawdzenie możliwych do przejścia kierunków
        if possibleMoves == 0:
            # połączenie wątków
            for thread in threads:
                thread.join()
            # wyczyszczenie listy wątków
            threads.clear()
            break
            # default down direction
            if (newX or newY) < mazeSize:
                if isPlaceFree(x + 1, y):
                    possibleMoves += 1
                    newX += 1
                    t2 = threading.Thread(target=traverseMaze, args=(newX, y, 2))
                    threads.append(t2)
                    t2.start()
                    updateMazePlace(newX, y, 2)

            # other directions
            if (newX or newY) < mazeSize:
                # up
                if isPlaceFree(x - 1, y):
                    possibleMoves += 1
                    newX -= 1
                    t3 = threading.Thread(target=traverseMaze, args=(newX, y, 3))
                    threads.append(t3)
                    t3.start()
                    updateMazePlace(newX, y, 3)
                    # right
                elif isPlaceFree(x, y + 1):
                    possibleMoves += 1
                    newY += 1
                    t4 = threading.Thread(target=traverseMaze, args=(x, newY, 4))
                    threads.append(t4)
                    t4.start()
                    updateMazePlace(x, newY, 4)
                    # left
                elif isPlaceFree(x, y - 1):
                    possibleMoves += 1
                    newY -= 1
                    t5 = threading.Thread(target=traverseMaze, args=(x, newY, 5))
                    threads.append(t5)
                    t5.start()
                    updateMazePlace(x, newY, 5)
                    if possibleMoves > 0:
                        thread_guard.acquire()
                        threadId += 1
                        thread_guard.release()

                        t = threading.Thread(target=traverseMaze,
                                             args=(x - 1, y, 6))
                        threads.append(t)
                        t.start()
                        updateMazePlace(x - 1, y, 6)
                    else:
                        possibleMoves += 1
                        newX -= 1

def change_maze_size(new_size):
    # access and change variables directly
    global mazeSize
    global maze
    global locks
    mazeSize = new_size
    maze = np.zeros((mazeSize, mazeSize))
    locks = np.array([[threading.Lock() for j in range(mazeSize)] for i in range(mazeSize)])
    initMaze()

# inicjalizacja labiryntu
initMaze()
traverseMaze(0, 0, 1)
# wizualizacja labiryntu
plt.rcParams['figure.figsize'] = (8, 8)
plt.imshow(maze, cmap="cool")
plt.title("100x100 maze")
plt.show()

change_maze_size(50)
plt.imshow(maze, cmap="cool")
plt.title("50x50 maze")
plt.show()

change_maze_size(200)
plt.imshow(maze, cmap="cool")
plt.title("200x200 maze")
plt.show()

# nowe układy labiryntu
change_maze_size(100)
initMazeEx1()
plt.imshow(maze, cmap="cool")
plt.title("Example maze 1")
plt.show()

initMazeEx2()
plt.imshow(maze, cmap="cool")
plt.title("Example maze 2")
plt.show()

initMazeEx3()
plt.imshow(maze, cmap="cool")
plt.title("Example maze 3")
plt.show()
