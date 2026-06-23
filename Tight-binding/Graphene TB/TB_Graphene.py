import numpy as np
import matplotlib.pyplot as plt

# Lattice constant (arbitrary units)
a = 1.0

# Nearest neighbor vectors δ_n (in units of a)
delta = np.array([
    [0, -a/np.sqrt(3)],
    [a/2, a/(2*np.sqrt(3))],
    [-a/2, a/(2*np.sqrt(3))]
])

# Reciprocal lattice vectors (for reference)
b1 = (2*np.pi/a) * np.array([1, -1/np.sqrt(3)])
b2 = (2*np.pi/a) * np.array([0, 2/np.sqrt(3)])

# High symmetry points in reciprocal space
Gamma = np.array([0, 0])
K = (b1 + 2*b2) / 3
M = b1 / 2

# Nearest-neighbor hopping parameter (eV)
t = 2.7

def f_k(k):
    """Calculate the off-diagonal element f(k) of the graphene Hamiltonian."""
    return -t * np.sum(np.exp(1j * np.dot(delta, k)))

# Generate k-points along the path Gamma -> K -> M -> Gamma
num_points = 100
path_GK = np.linspace(Gamma, K, num_points)
path_KM = np.linspace(K, M, num_points)
path_MG = np.linspace(M, Gamma, num_points)
k_path = np.vstack((path_GK, path_KM, path_MG))

# Calculate energies along the k-path
energies = []
for k in k_path:
    fk = f_k(k)
    E_plus = np.abs(fk)
    E_minus = -np.abs(fk)
    energies.append([E_minus, E_plus])
energies = np.array(energies).T

# Distance along k-path for plotting
distances = np.concatenate([
    np.linspace(0, 1, num_points),
    np.linspace(1, 2, num_points),
    np.linspace(2, 3, num_points)
])

# High-symmetry points labels and positions
labels = ['$\\Gamma$', 'K', 'M', '$\\Gamma$']
label_positions = [0, 1, 2, 3]

# Plot the band structure
plt.figure(figsize=(8, 6))
plt.plot(distances, energies[0], label='Valence band')
plt.plot(distances, energies[1], label='Conduction band')
plt.xticks(label_positions, labels)
plt.xlabel('Wavevector')
plt.ylabel('Energy (eV)')
plt.title('Graphene Tight-Binding Band Structure')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()