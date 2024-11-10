from sklearn.datasets import make_moons
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X, y = make_moons(n_samples=100, noise=0.2)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title('Generowane dane - make_moons')
plt.show()

X, y = make_moons(n_samples=100, noise=0.2)

iris = load_iris()
X_iris = iris.data
y_iris = iris.target

# podzial danych na zbior uczacy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Wybór liczby sąsiadów
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
accuracies = []
for k in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred))

optimal_k = accuracies.index(max(accuracies)) + 1
print(f"Optymalna liczba sąsiadów: {optimal_k}")

# wizualizacja
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
plt.title('Rzeczywisty podział klas')
plt.show()
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred)
plt.title('Podział klas na podstawie predykcji')
plt.show()
iris = load_iris()
X_iris = iris.data[:, :3]  # Trzy pierwsze cechy
y_iris = iris.target
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X_iris[:, 0], X_iris[:, 1], X_iris[:, 2], c=y_iris)
plt.title('3D Wizualizacja danych Iris')
plt.show()


