import numpy as np
import matplotlib.pyplot as plt

# --- 1. Definindo a forma original (um quadrado) ---
# Os vértices são (0,0), (1,0), (1,1), (0,1).
# Repetimos o primeiro ponto no final para fechar a forma ao plotar.
quadrado_original = np.array([
    [0, 1, 1, 0, 0],  # Coordenadas X
    [0, 0, 1, 1, 0]   # Coordenadas Y
])

# --- 2. Definindo a Matriz de Cisalhamento em X ---
# Fator de cisalhamento. Experimente mudar este valor (ex: 2, -1, 0.5)
k = 1.5

# Matriz de cisalhamento na direção de x
# C_x = [[1, k], [0, 1]]
C_x = np.array([
    [1, k],
    [0, 1]
])

print(f"Aplicando cisalhamento com fator k = {k}")
print("Matriz de Cisalhamento:\n", C_x)

# --- 3. Aplicando a transformação ---
# Multiplicamos a matriz de cisalhamento por cada ponto do quadrado
quadrado_cisalhado = C_x @ quadrado_original

# --- 4. Visualizando o resultado ---
plt.figure(figsize=(10, 6))

# Plotando o quadrado original
plt.plot(quadrado_original[0, :], quadrado_original[1, :], 'b--', label='Quadrado Original')

# Plotando a forma cisalhada (paralelogramo)
plt.plot(quadrado_cisalhado[0, :], quadrado_cisalhado[1, :], 'g-', label=f'Forma Cisalhada (k={k})')

# Adicionando anotações para clareza
# Vértices originais
orig_points = quadrado_original[:, :4].T # Transpõe para iterar sobre os pontos
for i, (x, y) in enumerate(orig_points):
    plt.text(x - 0.1, y - 0.1, f'({x},{y})', color='blue')

# Vértices novos
new_points = quadrado_cisalhado[:, :4].T
for i, (x, y) in enumerate(new_points):
    plt.text(x + 0.1, y, f'({x:.1f},{y})', color='green')


# Configurações do gráfico
plt.title('Cisalhamento na Direção de X')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid(True)
plt.axis('equal') # Essencial para ver a transformação sem distorção
plt.legend()
plt.show()