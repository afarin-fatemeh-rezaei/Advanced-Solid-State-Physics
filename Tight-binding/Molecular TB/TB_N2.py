import numpy as np
import matplotlib.pyplot as plt

# Parameters for N2
E_N = -15.0    # On-site energy for N 2p orbital (eV)
t_NN = -3.0    # Hopping integral between N atoms (eV)

# Hamiltonian matrix
H_N2 = np.array([[E_N, t_NN],
                 [t_NN, E_N]])

# Solve eigenvalues
energies_N2, _ = np.linalg.eigh(H_N2)
E_bonding_N2, E_antibonding_N2 = energies_N2

print("N2 Energy levels (eV):")
print(f"Bonding: {E_bonding_N2:.3f} eV")
print(f"Antibonding: {E_antibonding_N2:.3f} eV")

# Plot
plt.figure(figsize=(6,4))
plt.hlines(E_bonding_N2, xmin=0.5, xmax=1.5, colors='blue', label=f'Bonding: {E_bonding_N2:.2f} eV', linewidth=2)
plt.hlines(E_antibonding_N2, xmin=2.5, xmax=3.5, colors='red', label=f'Antibonding: {E_antibonding_N2:.2f} eV', linewidth=2)
plt.hlines(E_N, xmin=0, xmax=0.5, colors='green', label=f'N on-site: {E_N:.2f} eV', linewidth=2, linestyles='dashed')
plt.hlines(E_N, xmin=3.5, xmax=4, colors='purple', label=f'N on-site: {E_N:.2f} eV', linewidth=2, linestyles='dashed')
plt.plot(1, E_bonding_N2, 'bo')
plt.plot(3, E_antibonding_N2, 'ro')
plt.plot(0.25, E_N, 'go')
plt.plot(3.75, E_N, 'mo')
plt.xlim(-0.5, 4.5)
plt.ylim(E_N - 5, E_N + 5)
plt.xticks([])
plt.ylabel('Energy (eV)')
plt.title('N2 Molecular Tight-Binding Energy Levels')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()