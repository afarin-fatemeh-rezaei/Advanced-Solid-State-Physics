# Graphene Tight-Binding Analysis

**Computational study of the electronic band structure of graphene using the tight-binding model**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Methodology](#methodology)
  - [Tight-Binding Model](#tight-binding-model)
  - [Lattice Structure](#lattice-structure)
  - [Brillouin Zone Path](#brillouin-zone-path)
- [Code Structure](#code-structure)
  - [Lattice Parameters](#lattice-parameters)
  - [Hopping Parameter](#hopping-parameter)
  - [Hamiltonian and Eigenvalues](#hamiltonian-and-eigenvalues)
  - [Band Structure Calculation](#band-structure-calculation)
- [Results](#results)
  - [Band Structure](#band-structure)
  - [Dirac Points](#dirac-points)
- [Physical Properties](#physical-properties)
  - [Electrical Properties](#electrical-properties)
  - [Optical Properties](#optical-properties)
  - [Thermal Properties](#thermal-properties)
  - [Limitations of the Model](#limitations-of-the-model)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)
- [References](#references)
- [Acknowledgments](#acknowledgments)

---

## 📖 Overview

This project was completed as part of an **Advanced Solid State** course. The goal was to implement a **tight-binding model** for graphene and analyze its electronic band structure, revealing the characteristic **Dirac cones** and the **zero-band-gap semimetal** behavior.

Graphene, a single layer of carbon atoms arranged in a honeycomb lattice, is a fascinating material with unique electronic properties. Its band structure, described by the tight-binding model, shows linear dispersion near the **K** and **K'** points, giving rise to **massless Dirac fermions** with exceptional mobility.

---

## 🧪 Methodology

### Tight-Binding Model

The tight-binding Hamiltonian for graphene can be written as:

\[
H = -t \sum_{\langle i,j \rangle} (a_i^\dagger b_j + b_j^\dagger a_i)
\]

where:
- \( t = 2.7 \, \text{eV} \) is the nearest-neighbor hopping parameter
- \( a_i^\dagger \) and \( b_j \) are creation/annihilation operators on the two sublattices (A and B)

The **2×2 Hamiltonian** in reciprocal space becomes:

\[
H(\mathbf{k}) = \begin{pmatrix}
0 & f(\mathbf{k}) \\
f^*(\mathbf{k}) & 0
\end{pmatrix}
\]

where the off-diagonal element is:

\[
f(\mathbf{k}) = -t \sum_{n=1}^3 e^{i \mathbf{k} \cdot \boldsymbol{\delta}_n}
\]

The eigenvalues (band energies) are:

\[
E_{\pm}(\mathbf{k}) = \pm |f(\mathbf{k})|
\]

giving the **valence band** (\(E_-\)) and **conduction band** (\(E_+\)).

### Lattice Structure

Graphene's honeycomb lattice has a **two-atom basis** with the following **nearest-neighbor vectors** (in units of lattice constant \(a\)):

\[
\boldsymbol{\delta}_1 = \begin{pmatrix} 0 \\ -a/\sqrt{3} \end{pmatrix}, \quad
\boldsymbol{\delta}_2 = \begin{pmatrix} a/2 \\ a/(2\sqrt{3}) \end{pmatrix}, \quad
\boldsymbol{\delta}_3 = \begin{pmatrix} -a/2 \\ a/(2\sqrt{3}) \end{pmatrix}
\]

The **reciprocal lattice vectors** are:

\[
\mathbf{b}_1 = \frac{2\pi}{a} \begin{pmatrix} 1 \\ -1/\sqrt{3} \end{pmatrix}, \quad
\mathbf{b}_2 = \frac{2\pi}{a} \begin{pmatrix} 0 \\ 2/\sqrt{3} \end{pmatrix}
\]

### Brillouin Zone Path

The band structure is computed along the high-symmetry path:

\[
\Gamma \rightarrow K \rightarrow M \rightarrow \Gamma
\]

| Point | Coordinates |
|-------|-------------|
| Γ | (0, 0) |
| K | (b₁ + 2b₂)/3 |
| M | b₁/2 |

---

## 💻 Code Structure

### Lattice Parameters

```python
import numpy as np
import matplotlib.pyplot as plt

a = 1.0  # Lattice constant (arbitrary units)

# Nearest-neighbor vectors
delta = np.array([
    [0, -a/np.sqrt(3)],
    [a/2, a/(2*np.sqrt(3))],
    [-a/2, a/(2*np.sqrt(3))]
])
```

### Hopping Parameter

```python
t = 2.7  # eV

def f_k(k):
    """Calculate the off-diagonal element f(k)."""
    return -t * np.sum(np.exp(1j * np.dot(delta, k)))
```

### Hamiltonian and Eigenvalues

For each k-point, the eigenvalues are computed directly from the Hamiltonian:

```python
fk = f_k(k)
E_plus = np.abs(fk)   # Conduction band
E_minus = -np.abs(fk) # Valence band
```

### Band Structure Calculation

The k-path is generated with 100 points per segment:

```python
path_GK = np.linspace(Gamma, K, num_points)
path_KM = np.linspace(K, M, num_points)
path_MG = np.linspace(M, Gamma, num_points)
k_path = np.vstack((path_GK, path_KM, path_MG))
```

---

## 📊 Results

### Band Structure

The calculated band structure shows:

1. **Two bands**: Conduction band (positive energies) and valence band (negative energies)
2. **Dirac points**: The bands touch at the **K** and **K'** points
3. **Linear dispersion**: Near the Dirac points, the energy dispersion is linear:
   \[
   E(\mathbf{k}) \approx \pm \hbar v_F |\mathbf{k} - \mathbf{K}|
   \]
   where \(v_F \approx 10^6 \, \text{m/s}\) is the Fermi velocity
4. **Zero band gap**: There is no energy gap between the valence and conduction bands

<center><b>Figure 1:</b> Graphene tight-binding band structure showing Dirac cones at the K point</center>

### Dirac Points

At the **K** point, \(f(\mathbf{K}) = 0\), leading to:

\[
E_+(\mathbf{K}) = E_-(\mathbf{K}) = 0
\]

The Fermi level lies exactly at the Dirac point, making graphene a **zero-gap semiconductor** (or **semimetal**).

---

## 🔬 Physical Properties

### Electrical Properties

1. **High Conductivity**: Electrons near the Dirac point behave as **massless Dirac fermions** with exceptionally high mobility (~200,000 cm²/V·s).

2. **Ambipolar Transport**: By shifting the Fermi level via gating or doping, both **electrons** (n-type) and **holes** (p-type) can act as charge carriers.

3. **Minimum Conductivity**: Even at zero carrier density, graphene exhibits a minimum conductivity of approximately \(4e^2/h\) per channel.

4. **Quantum Hall Effect**: At low temperatures, graphene shows an anomalous **half-integer quantum Hall effect**, which is a direct consequence of the linear dispersion and Berry phase.

### Optical Properties

1. **Transparency**: Graphene absorbs only ~**2.3%** of visible light per layer, making it nearly transparent (universal optical conductivity).

2. **Broadband Absorption**: The linear bands enable absorption across a wide range of photon energies.

3. **No Characteristic Color**: The lack of a band gap means no specific color is associated with graphene.

### Thermal Properties

1. **Exceptional Thermal Conductivity**: Strong covalent bonds and delocalized electrons allow graphene to conduct heat extremely efficiently (~5000 W/m·K).

2. **Electron-Phonon Coupling**: The band structure hints at strong coupling between electrons and phonons, important for thermal transport.

### Limitations of the Model

While the tight-binding model reveals much, it does NOT directly provide:

1. **Electron-electron interactions** (correlations, excitonic effects)
2. **Phonon spectra** (lattice vibrations)
3. **Effects of impurities, strain, or substrate interactions**
4. **Many-body phenomena** such as superconductivity
5. **Magnetic properties** (requires spin-orbit coupling or Hubbard models)
6. **Temperature-dependent effects** (requires finite-temperature extensions)

---

## 📦 Dependencies

| Library | Purpose |
|---------|---------|
| **NumPy** | Numerical calculations and array operations |
| **Matplotlib** | Plotting the band structure |
| **Python 3.x** | Programming language |

### Installation

```bash
pip install numpy matplotlib
```

---

## 🚀 How to Run

### Step 1: Save the Script

Save the Python code as `TB_Graphene.py`.

### Step 2: Run the Script

```bash
python TB_Graphene.py
```

### Step 3: Expected Output

- A plot window will appear showing the graphene band structure.
- The plot shows:
  - **Valence band** (blue line)
  - **Conduction band** (orange line)
  - **High-symmetry points**: Γ, K, M
  - **Dirac point** at K where bands touch

### Step 4: Modify Parameters (Optional)

To explore different scenarios, you can modify:
- `t` (hopping parameter) to change the band width
- `num_points` to adjust resolution
- Add **strain** by modifying the `delta` vectors
- Include **next-nearest-neighbor hopping** by adding a second term

---

## 📚 References

1. **Castro Neto, A. H., Guinea, F., Peres, N. M. R., Novoselov, K. S., & Geim, A. K.** (2009). "The electronic properties of graphene." *Reviews of Modern Physics*, 81(1), 109-162.

2. **Kittel, C.** (2004). *Introduction to Solid State Physics*, 8th Edition. Wiley.

3. **Wallace, P. R.** (1947). "The Band Theory of Graphite." *Physical Review*, 71(9), 622-634.

4. **Novoselov, K. S., Geim, A. K., Morozov, S. V., Jiang, D., Zhang, Y., Dubonos, S. V., ... & Firsov, A. A.** (2004). "Electric Field Effect in Atomically Thin Carbon Films." *Science*, 306(5696), 666-669.

5. **Saito, R., Dresselhaus, G., & Dresselhaus, M. S.** (1998). *Physical Properties of Carbon Nanotubes*. Imperial College Press.

---

## 🙏 Acknowledgments

This project was completed as part of an **Advanced Solid State** course, focusing on the computational implementation of tight-binding models and their application to understanding real materials.

---

**Happy Coding!** ⚛️✨
