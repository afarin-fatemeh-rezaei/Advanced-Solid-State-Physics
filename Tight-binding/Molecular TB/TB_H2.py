import numpy as np
import matplotlib.pyplot as plt

# Parameters for H2
E_H = -13.6    # On-site energy for H 1s orbital (eV)
t_HH = -4.0    # Hopping integral between H atoms (eV)

# Hamiltonian matrix
H_H2 = np.array([[E_H, t_HH],
                 [t_HH, E_H]])

# Solve eigenvalues
energies_H2, _ = np.linalg.eigh(H_H2)
E_bonding_H2, E_antibonding_H2 = energies_H2

print("H2 Energy levels (eV):")
print(f"Bonding: {E_bonding_H2:.3f} eV")
print(f"Antibonding: {E_antibonding_H2:.3f} eV")

# Plot
plt.figure(figsize=(6,4))
plt.hlines(E_bonding_H2, xmin=0.5, xmax=1.5, colors='blue', label=f'Bonding: {E_bonding_H2:.2f} eV', linewidth=2)
plt.hlines(E_antibonding_H2, xmin=2.5, xmax=3.5, colors='red', label=f'Antibonding: {E_antibonding_H2:.2f} eV', linewidth=2)
plt.hlines(E_H, xmin=0, xmax=0.5, colors='green', label=f'H on-site: {E_H:.2f} eV', linewidth=2, linestyles='dashed')
plt.hlines(E_H, xmin=3.5, xmax=4, colors='purple', label=f'H on-site: {E_H:.2f} eV', linewidth=2, linestyles='dashed')
plt.plot(1, E_bonding_H2, 'bo')
plt.plot(3, E_antibonding_H2, 'ro')
plt.plot(0.25, E_H, 'go')
plt.plot(3.75, E_H, 'mo')
plt.xlim(-0.5, 4.5)
plt.ylim(E_H - 5, E_H + 5)
plt.xticks([])
plt.ylabel('Energy (eV)')
plt.title('H2 Molecular Tight-Binding Energy Levels')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()