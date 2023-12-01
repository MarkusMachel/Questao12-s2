import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
image = cv2.imread('moon.jpg')  # Substitua pelo caminho da sua imagem

# Somar os 3 canais e normalizar
sum_channels = np.sum(image, axis=2)
normalized = (255 * (sum_channels - sum_channels.min()) / (sum_channels.max() - sum_channels.min())).astype(float)
normalized /= 255.0  # Normalizar para o intervalo [0, 1]

# Aplicar as regras de aproximação
output_image = np.zeros_like(normalized)
output_image[normalized < 0.25] = 0
output_image[(0.25 <= normalized) & (normalized < 0.5)] = 0.25
output_image[(0.5 <= normalized) & (normalized < 0.75)] = 0.5
output_image[0.75 <= normalized] = 1

# Exibir a imagem resultante usando imshow do matplotlib
plt.imshow(output_image, cmap='gray')
plt.axis('off')
plt.show()

# Calcular a média dos pixels sobre toda a imagem
average_value = np.mean(output_image)
print(f"A média dos pixels sobre toda a imagem é: {average_value}")


