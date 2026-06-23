import numpy as np
import matplotlib.pyplot as plt

# On-site energies (eV) - approximate values
E_Li = -5.0   # Li 2s orbital energy
E_F = -15.0   # F 2p orbital energy

# Hopping integral (eV) - coupling between Li and F orbitals
t = -2.0

# Hamiltonian matrix
H = np.array([[E_Li, t],
              [t, E_F]])

# Solve eigenvalues (energy levels)
energies, _ = np.linalg.eigh(H)
E_bonding, E_antibonding = energies

print("Energy levels of LiF molecule (eV):")
print(f"Bonding: {E_bonding:.3f} eV")
print(f"Antibonding: {E_antibonding:.3f} eV")

# Prepare plot
plt.figure(figsize=(6, 4))

# Plot molecular energy levels
plt.hlines(E_bonding, xmin=0.5, xmax=1.5, colors='blue', label=f'Bonding: {E_bonding:.2f} eV', linewidth=2)
plt.hlines(E_antibonding, xmin=2.5, xmax=3.5, colors='red', label=f'Antibonding: {E_antibonding:.2f} eV', linewidth=2)

# Plot on-site energies
plt.hlines(E_Li, xmin=0, xmax=0.5, colors='green', label=f'Li on-site: {E_Li:.2f} eV', linewidth=2, linestyles='dashed')
plt.hlines(E_F, xmin=3.5, xmax=4, colors='purple', label=f'F on-site: {E_F:.2f} eV', linewidth=2, linestyles='dashed')

# Markers for clarity
plt.plot(1, E_bonding, 'bo')
plt.plot(3, E_antibonding, 'ro')
plt.plot(0.25, E_Li, 'go')
plt.plot(3.75, E_F, 'mo')

# Formatting plot
plt.xlim(-0.5, 4.5)
plt.ylim(E_F - 5, E_Li + 5)
plt.xticks([])
plt.ylabel('Energy (eV)')
plt.title('LiF Molecular Tight-Binding Energy Levels')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()