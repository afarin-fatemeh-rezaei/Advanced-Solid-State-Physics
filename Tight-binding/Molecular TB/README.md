# Molecular Tight-Binding Analysis: LiF, H₂, N₂

**Computational study of molecular orbital formation using the tight-binding (LCAO) method**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Methodology](#methodology)
  - [Tight-Binding Model](#tight-binding-model)
  - [Hamiltonian and Eigenvalues](#hamiltonian-and-eigenvalues)
- [Code Structure](#code-structure)
  - [H₂](#h₂)
  - [N₂](#n₂)
  - [LiF](#lif)
- [Results](#results)
  - [Energy Level Diagrams](#energy-level-diagrams)
  - [Summary Table](#summary-table)
- [Physical Interpretation](#physical-interpretation)
  - [Homo-nuclear vs. Hetero-nuclear Molecules](#homo-nuclear-vs-hetero-nuclear-molecules)
  - [The Hopping Integral](#the-hopping-integral)
  - [Bonding and Antibonding Orbitals](#bonding-and-antibonding-orbitals)
- [Limitations of the Model](#limitations-of-the-model)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)
- [References](#references)
- [Acknowledgments](#acknowledgments)

---

## 📖 Overview

This project was completed as part of an **Advanced Solid State** course. The goal was to implement the **tight-binding (LCAO)** method for small molecules, analyzing how atomic orbitals combine to form molecular orbitals.

Three molecules were studied:

| Molecule | Type | Orbitals Involved | Bond Character |
|----------|------|-------------------|----------------|
| **H₂** | Homo-nuclear diatomic | 1s + 1s | Covalent |
| **N₂** | Homo-nuclear diatomic | 2p + 2p | Covalent (triple bond) |
| **LiF** | Hetero-nuclear diatomic | 2s + 2p | Ionic |

The calculations reveal the formation of **bonding** and **antibonding** molecular orbitals, with energy splittings determined by the **hopping integral (t)**.

---

## 🧪 Methodology

### Tight-Binding Model

The tight-binding (or Linear Combination of Atomic Orbitals, LCAO) method approximates molecular orbitals as linear combinations of atomic orbitals. For a diatomic molecule with one orbital per atom, the wavefunction is:

\[
|\psi\rangle = c_A |\phi_A\rangle + c_B |\phi_B\rangle
\]

### Hamiltonian and Eigenvalues

The **2×2 Hamiltonian** in the basis of atomic orbitals is:

\[
\mathbf{H} = \begin{pmatrix}
E_A & t \\
t & E_B
\end{pmatrix}
\]

where:
- \(E_A\) = On-site energy of atom A (atomic orbital energy)
- \(E_B\) = On-site energy of atom B
- \(t\) = Hopping integral (interaction strength between orbitals)

The eigenvalues (molecular orbital energies) are:

\[
E_{\pm} = \frac{E_A + E_B}{2} \pm \sqrt{\left(\frac{E_A - E_B}{2}\right)^2 + t^2}
\]

The eigenvectors give the coefficients \(c_A\) and \(c_B\), determining the character of each molecular orbital.

---

## 💻 Code Structure

All three codes follow the same logical structure, mirroring the tight-binding calculation on paper:

### H₂

**Homo-nuclear diatomic** with identical atoms.

```python
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
```

### N₂

**Homo-nuclear diatomic** with larger on-site energy and smaller hopping.

```python
# Parameters for N2
E_N = -15.0    # On-site energy for N 2p orbital (eV)
t_NN = -3.0    # Hopping integral between N atoms (eV)

# Hamiltonian matrix
H_N2 = np.array([[E_N, t_NN],
                 [t_NN, E_N]])
```

### LiF

**Hetero-nuclear diatomic** with different on-site energies and smaller hopping.

```python
# On-site energies (eV) - approximate values
E_Li = -5.0   # Li 2s orbital energy
E_F = -15.0   # F 2p orbital energy

# Hopping integral (eV) - coupling between Li and F orbitals
t = -2.0

# Hamiltonian matrix
H = np.array([[E_Li, t],
              [t, E_F]])
```

---

## 📊 Results

### Energy Level Diagrams

#### H₂

**Molecular Orbital Diagram:**

```
Energy (eV)
    |
    |     -9.60 eV (Antibonding σ*)
    |
    |
    |  ---- -13.60 eV (Atomic H 1s)
    |
    |  ---- -13.60 eV (Atomic H 1s)
    |
    |    -17.60 eV (Bonding σ)
```

**Energy Levels:**
- **Bonding (σ)**: -17.60 eV
- **Antibonding (σ*)**: -9.60 eV
- **Splitting**: 8.00 eV = 2|t|

#### N₂

**Energy Levels:**
- **Bonding (σ)**: -18.00 eV
- **Antibonding (σ*)**: -12.00 eV
- **Splitting**: 6.00 eV = 2|t|

#### LiF

**Energy Levels:**
- **Bonding (mostly F character)**: -15.39 eV
- **Antibonding (mostly Li character)**: -4.61 eV

**Ionic Character**: The bonding orbital is close to the F on-site energy, indicating the electron density is primarily on the F atom.

---

### Summary Table

| Molecule | On-site Energies (eV) | t (eV) | Bonding (eV) | Antibonding (eV) | ΔE (eV) |
|----------|----------------------|--------|--------------|------------------|---------|
| **H₂** | -13.6, -13.6 | -4.0 | -17.6 | -9.6 | 8.0 |
| **N₂** | -15.0, -15.0 | -3.0 | -18.0 | -12.0 | 6.0 |
| **LiF** | -5.0 (Li), -15.0 (F) | -2.0 | -15.39 | -4.61 | 10.78 |

---

## 🔬 Physical Interpretation

### Homo-nuclear vs. Hetero-nuclear Molecules

**Homo-nuclear (H₂, N₂):**
- On-site energies are equal (\(E_A = E_B\))
- Molecular orbitals are **symmetric** and **antisymmetric**
- Bonding and antibonding are **equally split** around the atomic level
- \(E_{\pm} = E_0 \pm |t|\)

**Hetero-nuclear (LiF):**
- On-site energies are different (\(E_A \neq E_B\))
- Bonding orbital has **more character** from the lower-energy atomic orbital (F)
- Antibonding orbital has **more character** from the higher-energy atomic orbital (Li)
- The larger the energy difference, the more **ionic** the bond

### The Hopping Integral

The **hopping integral (t)** quantifies the interaction strength between orbitals:

\[
t = \langle \phi_A | \hat{H} | \phi_B \rangle
\]

**Physical meaning:**
- Determines the **energy splitting** between bonding and antibonding orbitals
- For homonuclear molecules, splitting = \(2|t|\)
- **Larger |t|** → stronger interaction → larger splitting → stronger bond
- **Sign convention**: Negative \(t\) stabilizes the bonding orbital

**Values used in this work:**

| Molecule | t (eV) | Reason |
|----------|--------|--------|
| LiF | -2.0 | Weak overlap between Li 2s and F 2p |
| H₂ | -4.0 | Strong overlap between H 1s orbitals |
| N₂ | -3.0 | Intermediate overlap of N 2p orbitals |

### Bonding and Antibonding Orbitals

**Bonding Orbital (E₋):**
- Constructive interference between atomic orbitals
- **Stabilized** (lower energy)
- Electron density concentrated between atoms
- **Forms the bond**

**Antibonding Orbital (E₊):**
- Destructive interference between atomic orbitals
- **Destabilized** (higher energy)
- Electron density concentrated outside the bond
- **Weakens or breaks the bond**

---

## ⚠️ Limitations of the Model

This simple tight-binding model has several important limitations:

1. **No electron-electron repulsion**: Does not account for Coulomb repulsion between electrons
2. **No multi-electron effects**: Describes only single-electron states
3. **No bond length prediction**: Cannot predict equilibrium bond lengths
4. **No vibrational frequencies**: Requires inclusion of nuclear motion
5. **No excited states**: Only describes the ground-state orbital splitting
6. **No correlation effects**: Cannot describe excitonic states or charge-transfer excitations
7. **Single orbital per atom**: Real molecules have multiple orbitals that interact
8. **No geometry optimization**: Bond angles and distances are not calculated

For accurate predictions, one would need to use more advanced methods:
- **Hartree-Fock** (includes electron exchange)
- **Density Functional Theory (DFT)** (includes electron correlation)
- **Configuration Interaction (CI)** (accounts for excited states)
- **Post-Hartree-Fock methods** (MP2, CCSD, etc.)

---

## 📦 Dependencies

| Library | Purpose |
|---------|---------|
| **NumPy** | Numerical calculations and matrix diagonalization |
| **Matplotlib** | Plotting energy level diagrams |
| **Python 3.x** | Programming language |

### Installation

```bash
pip install numpy matplotlib
```

---

## 🚀 How to Run

### Step 1: Run Individual Scripts

```bash
python TB_H2.py
python TB_N2.py
python TB_LiF.py
```

### Step 2: Expected Output

Each script will:
1. Print the calculated bonding and antibonding energies
2. Display a plot of the molecular orbital energy levels

**Example Output (H₂):**
```
H2 Energy levels (eV):
Bonding: -17.600 eV
Antibonding: -9.600 eV
```

### Step 3: Modify Parameters (Optional)

To explore different scenarios, you can:
- Change the on-site energies (\(E_A\), \(E_B\))
- Vary the hopping integral (\(t\))
- Add additional orbitals (extend to 3×3 or larger matrices)

---

## 📚 References

1. **Ashcroft, N. W. & Mermin, N. D.** (1976). *Solid State Physics*. Brooks Cole.

2. **Kittel, C.** (2004). *Introduction to Solid State Physics*, 8th Edition. Wiley.

3. **Harrison, W. A.** (1980). *Electronic Structure and the Properties of Solids*. Dover Publications.

4. **Hoffmann, R.** (1988). "Tight-Binding in Chemistry." *Angewandte Chemie International Edition*, 27(4), 511-530.

5. **Atkins, P. & Friedman, R.** (2010). *Molecular Quantum Mechanics*, 5th Edition. Oxford University Press.

---

## 🙏 Acknowledgments

This project was completed as part of an **Advanced Solid State** course, focusing on the computational implementation of tight-binding models for molecular systems.

---

**Happy Computing!** ⚛️🔬
