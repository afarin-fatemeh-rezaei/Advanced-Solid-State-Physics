# Advanced Solid State Course Repository

**Computational solid-state physics and crystallography: Tight-binding models and crystallographic structure analysis**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Projects](#projects)
  - [1. Crystallographic Information Files (CIF)](#1-crystallographic-information-files-cif)
  - [2. Tight-Binding Calculations](#2-tight-binding-calculations)
    - [Graphene Band Structure](#graphene-band-structure)
    - [Molecular Orbital Calculations](#molecular-orbital-calculations)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)
- [Course Concepts](#course-concepts)
- [References](#references)
- [Acknowledgments](#acknowledgments)

---

## 📖 Overview

This repository contains coursework and computational projects from an **Advanced Solid State** course. The work is organized into two main areas:

1. **Crystallography** – Crystal structure analysis using CIF files and visualization tools
2. **Tight-Binding Theory** – Computational implementation of tight-binding models for materials and molecules

Together, these projects explore the electronic structure of materials at multiple scales:
- **Macroscopic**: Crystal symmetry, space groups, and atomic arrangements (CIF files)
- **Mesoscopic**: Band structure and electronic properties (graphene tight-binding)
- **Microscopic**: Molecular orbitals and chemical bonding (molecular tight-binding)

---

## 📁 Repository Structure

```
Advanced_Solid_State/
│
├── cif/                                    # Crystallographic Information Files
│   ├── chrysoberyl.cif                     # Al₁.₉₈Cr₀.₀₂BeO₄ (orthorhombic, Pnma)
│   ├── quartz.cif                          # SiO₂ (trigonal, P3₂21)
│   ├── tremolite.cif                       # Ca₂Na₀.₁Mg₅Si₈O₂₂F₀.₃₃(OH)₁.₆₇ (monoclinic, C2/m)
│   └── README.md                           # CIF project documentation
│
├── tight_binding/                          # Tight-binding calculations
│   │
│   ├── graphene/                           # Graphene band structure
│   │   ├── TB_Graphene.py                  # Python implementation
│   │   ├── Graphene TB Analysis.pdf        # Written analysis
│   │   └── README.md                       # Graphene project documentation
│   │
│   └── molecular/                          # Molecular orbital calculations
│       ├── TB_H2.py                        # Hydrogen molecule (H₂)
│       ├── TB_N2.py                        # Nitrogen molecule (N₂)
│       ├── TB_LiF.py                       # Lithium fluoride (LiF)
│       ├── Molecular TB Analysis.pdf       # Written analysis
│       └── README.md                       # Molecular project documentation
│
└── README.md                               # This file
```

---

## 🔬 Projects

### 1. Crystallographic Information Files (CIF)

**Objective**: Provide and analyze crystallographic data for three mineral structures, illustrating key concepts in solid-state chemistry.

| Mineral | Formula | Space Group | Key Feature |
|---------|---------|-------------|-------------|
| **Chrysoberyl** | Al₁.₉₈Cr₀.₀₂BeO₄ | *Pnma* | Cr³⁺ substitution on Al site |
| **Quartz** | SiO₂ | *P3₂21* | Trigonal polymorph, chiral structure |
| **Tremolite** | Ca₂Na₀.₁Mg₅Si₈O₂₂F₀.₃₃(OH)₁.₆₇ | *C2/m* | Amphibole group, complex solid solution |

**Key Concepts**:
- Solid solutions and isomorphous substitution (Chrysoberyl, Tremolite)
- Chiral symmetry and polytypism (Quartz)
- Site occupancy and disorder (Tremolite)
- Anisotropic displacement parameters (all structures)
- Polyhedral connectivity (all structures)

**How to Use**:
1. Open `.cif` files in visualization software (VESTA, Mercury, CrystalMaker)
2. Inspect 3D structures, bond lengths, and coordination polyhedra
3. Analyze site occupancy and thermal displacement parameters
4. Export images for reports or presentations

**Documentation**: See `cif/README.md` for detailed structure descriptions and analysis.

---

### 2. Tight-Binding Calculations

#### Graphene Band Structure

**Objective**: Compute and analyze the electronic band structure of graphene using the tight-binding model.

**Key Results**:
- **Dirac points**: Bands touch at K and K' points
- **Zero band gap**: Graphene is a semimetal (zero-gap semiconductor)
- **Linear dispersion**: Massless Dirac fermions near Dirac points
- **Fermi velocity**: \(v_F \approx 10^6 \, \text{m/s}\)
- **Ambipolar transport**: Both electrons and holes can act as charge carriers

**Physical Properties Deduced**:
- High electrical conductivity and mobility
- Minimum conductivity (\(4e^2/h\))
- Optical transparency (~2.3% absorption per layer)
- Exceptional thermal conductivity

**Limitations of the Model**:
- No electron-electron interactions
- No phonon spectra
- No impurity or strain effects
- No many-body phenomena

**How to Run**:
```bash
cd tight_binding/graphene
python TB_Graphene.py
```

**Documentation**: See `tight_binding/graphene/README.md` for detailed methodology and analysis.

---

#### Molecular Orbital Calculations

**Objective**: Implement the tight-binding (LCAO) method for small molecules and analyze molecular orbital formation.

| Molecule | Type | On-site (eV) | t (eV) | Bonding (eV) | Antibonding (eV) |
|----------|------|--------------|--------|--------------|------------------|
| **H₂** | Homo-nuclear | -13.6, -13.6 | -4.0 | -17.6 | -9.6 |
| **N₂** | Homo-nuclear | -15.0, -15.0 | -3.0 | -18.0 | -12.0 |
| **LiF** | Hetero-nuclear | -5.0 (Li), -15.0 (F) | -2.0 | -15.39 | -4.61 |

**Key Concepts**:
- Bonding vs. antibonding orbitals
- Homo-nuclear vs. hetero-nuclear molecules
- The hopping integral (t) and its physical meaning
- Ionic vs. covalent bonding character
- Energy splitting and bond strength

**Physical Interpretation**:
- **Homo-nuclear (H₂, N₂)**: Equal on-site energies, symmetric splitting
- **Hetero-nuclear (LiF)**: Unequal on-site energies, orbital character mixed
- **Large |t|**: Strong interaction, large splitting, stronger bond
- **Small |t|**: Weak interaction, small splitting, weaker bond

**How to Run**:
```bash
cd tight_binding/molecular
python TB_H2.py    # H₂ energy levels
python TB_N2.py    # N₂ energy levels
python TB_LiF.py   # LiF energy levels
```

**Documentation**: See `tight_binding/molecular/README.md` for detailed methodology and analysis.

---

## 📦 Dependencies

### General
- Python 3.x
- NumPy
- Matplotlib

### CIF Visualization (Optional)
- VESTA (free)
- Mercury (free for academic use)
- CrystalMaker (commercial)
- Diamond (commercial)
- Python + pymatgen (open-source)

### Installation

```bash
# Python dependencies
pip install numpy matplotlib

# Optional: pymatgen for CIF analysis
pip install pymatgen
```

---

## 🚀 How to Run

### Run All Python Scripts

```bash
# Graphene band structure
cd tight_binding/graphene
python TB_Graphene.py

# Molecular calculations
cd ../molecular
python TB_H2.py
python TB_N2.py
python TB_LiF.py
```

### View CIF Files

1. Download **VESTA** from [https://jp-minerals.org/vesta/](https://jp-minerals.org/vesta/)
2. Open the `.cif` files in `cif/` directory
3. Explore 3D structures, measure distances, and analyze bonding

### Expected Outputs

**Graphene**: A plot showing the band structure with Dirac cones at the K point.

**Molecular**: Plots showing molecular orbital energy levels with:
- Atomic on-site energies (dashed lines)
- Molecular bonding and antibonding levels (solid lines)
- Energy splitting values

---

## 📚 Course Concepts

### Crystallography
- Space groups and symmetry operations
- Crystal systems and Bravais lattices
- Site occupancy and disorder
- Anisotropic displacement parameters
- Solid solutions and substitution
- Polyhedral connectivity and framework structures

### Electronic Structure
- Tight-binding method (LCAO)
- Band structure and density of states
- Dirac cones and massless Dirac fermions
- Molecular orbital theory
- Bonding vs. antibonding orbitals
- Hopping integral and interaction strength

### Materials Properties
- Semimetals vs. semiconductors vs. metals
- Ionic vs. covalent bonding
- Electrical conductivity and mobility
- Optical transparency
- Thermal conductivity

---

## 📖 References

### General Solid State
1. **Ashcroft, N. W. & Mermin, N. D.** (1976). *Solid State Physics*. Brooks Cole.
2. **Kittel, C.** (2004). *Introduction to Solid State Physics*, 8th Edition. Wiley.

### Graphene
3. **Castro Neto, A. H. et al.** (2009). "The electronic properties of graphene." *Reviews of Modern Physics*, 81(1), 109-162.
4. **Wallace, P. R.** (1947). "The Band Theory of Graphite." *Physical Review*, 71(9), 622-634.

### Molecular Tight-Binding
5. **Harrison, W. A.** (1980). *Electronic Structure and the Properties of Solids*. Dover.
6. **Hoffmann, R.** (1988). "Tight-Binding in Chemistry." *Angewandte Chemie*, 27(4), 511-530.

### Crystallography
7. **Deer, W. A., Howie, R. A., & Zussman, J.** (1992). *An Introduction to the Rock-Forming Minerals*, 2nd ed. Longman.
8. **International Tables for Crystallography, Vol. A**: Space-group symmetry.

---

## 🙏 Acknowledgments

These projects were completed as part of an **Advanced Solid State** course, exploring the intersection of computational methods and solid-state theory. Special thanks to the course instructors for guidance and materials.

---

**Happy Exploring!** ⚛️💎🔬
