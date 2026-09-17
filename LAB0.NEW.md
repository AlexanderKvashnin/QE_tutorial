# Installing Quantum ESPRESSO via WSL on Windows

A step-by-step guide to install **Quantum ESPRESSO (QE)** on Windows using the
**Windows Subsystem for Linux (WSL)** with Ubuntu. This is the recommended
approach for students who want to run plane-wave DFT calculations (pw.x, ph.x,
etc.) on a Windows laptop without leaving the Windows ecosystem.

After completing this guide, you will have a working `pw.x` executable and a
`pseudo/` folder ready for pseudopotentials.

---

## Table of Contents

1. Overview
2. Prerequisites
3. Step 1 — Install WSL
4. Step 2 — Update and Upgrade Ubuntu
5. Step 3 — Install Essential Dependencies
6. Step 4 — Download Quantum ESPRESSO
7. Step 5 — Configure and Compile QE
8. Step 6 — Set Up Environment Variables
9. Verification
10. Troubleshooting
11. Summary Cheat-Sheet

---

## 1. Overview

Quantum ESPRESSO is a suite of open-source codes for **electronic-structure
calculations** and **materials modeling** at the nanoscale. Its main engine,
`pw.x`, performs plane-wave pseudopotential DFT calculations. Because QE is
distributed only as source code and depends on optimized numerical libraries
(BLAS, LAPACK, FFTW, ScaLAPACK), it must be **compiled from source**.

On Windows, the cleanest way to do this is to use **WSL** — a real Linux
kernel running inside Windows — so that the same build instructions used on a
Linux cluster apply unchanged.

> **Why compile from source?** QE's performance depends strongly on the
> underlying math libraries. A version compiled against optimized BLAS/FFTW
> can be several times faster than a generic package from `apt`.

---

## 2. Prerequisites

- Windows 10 version 2004 (Build 19041) or higher, **or** Windows 11
- Administrator privileges
- Stable internet connection
- At least **20 GB** of free disk space (the compiled binaries plus the
  `pseudo/` folder can be large)

---

## 3. Step 1 — Install WSL

### 3.1 Enable the WSL Feature

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

This single command enables the required Windows features, installs WSL 2, and
downloads a default Ubuntu distribution.

### 3.2 Restart Your Computer

Restart Windows to complete the WSL installation.

### 3.3 Set WSL Version

After the restart, open PowerShell again (no admin needed) and set WSL 2 as
the default:

```powershell
wsl --set-default-version 2
```

### 3.4 Install Ubuntu

Either install from the Microsoft Store (search for **"Ubuntu"** and pick the
latest LTS — 22.04 or newer), or run:

```powershell
wsl --install -d Ubuntu
```

Launch **Ubuntu** from the Start Menu. When prompted, create a **username** and
**password** for your Linux account. These are separate from your Windows
credentials.

> **Tip:** The password is not shown while typing. This is normal for Linux.

---

## 4. Step 2 — Update and Upgrade Ubuntu

Open the Ubuntu terminal (Start Menu → "Ubuntu") and update the package lists:

```bash
sudo apt update && sudo apt upgrade -y
```

The `-y` flag automatically answers "yes" to all prompts — safe for a fresh
system.

---

## 5. Step 3 — Install Essential Dependencies

### 5.1 Install Build Tools and CMake

```bash
sudo apt install -y build-essential cmake cmake-curses-gui
```

| Package              | Purpose                                                  |
|----------------------|----------------------------------------------------------|
| `build-essential`    | `gcc`, `g++`, `make`, and other standard build tools     |
| `cmake`              | Build system (used by some QE versions and tools)        |
| `cmake-curses-gui`   | Interactive CMake front-end (`ccmake`)                   |

### 5.2 Install Fortran Compiler and Numerical Libraries

```bash
sudo apt install build-essential gfortran \
                 liblapack-dev libblas-dev \
                 libfftw3-dev libfftw3-mpi-dev \
                 libopenmpi-dev openmpi-bin \
                 libscalapack-mpi-dev libopenblas-dev \
                 libelpa-dev \
                 wget git curl unzip gnuplot
```

What each group of packages provides:

| Package group                              | Purpose                                                |
|--------------------------------------------|--------------------------------------------------------|
| `gfortran`                                 | Fortran compiler — QE is written in Fortran            |
| `liblapack-dev`, `libblas-dev`             | Linear algebra routines (LAPACK, BLAS)                 |
| `libfftw3-dev`, `libfftw3-mpi-dev`         | Fast Fourier Transforms (critical for plane-wave DFT)  |
| `libopenmpi-dev`, `openmpi-bin`            | MPI implementation for parallel execution              |
| `libscalapack-mpi-dev`                     | ScaLAPACK — parallel linear algebra                    |
| `libopenblas-dev`                          | Highly optimized BLAS implementation                   |
| `libelpa-dev`                              | ELPA — parallel eigensolver used by QE for large systems |
| `wget`, `git`, `curl`, `unzip`             | Tools for downloading and extracting sources           |
| `gnuplot`                                  | Plotting tool used by some QE post-processing scripts  |

---

## 6. Step 4 — Download Quantum ESPRESSO

### 6.1 Create Installation Directory

```bash
mkdir -p ~/quantum-espresso
cd ~/quantum-espresso
```

### 6.2 Download Source Code

Download a recent release from the official website:

```bash
wget https://www.quantum-espresso.org/rdm-download/8/v7-2/63bf22d8e65ee903f18500994cd32737/qe-7.2-ReleasePack.tar.gz
```

Extract the archive and enter the source directory:

```bash
tar -xzvf qe-7.2-ReleasePack.tar.gz
cd qe-7.2
```

> **Note:** Check the [official QE website](https://www.quantum-espresso.org/)
> for the latest version. Replace `qe-7.2` in all subsequent commands with the
> version you downloaded.

---

## 7. Step 5 — Configure and Compile QE

### 7.1 Configure the Build

The simplest command — QE auto-detects most libraries:

```bash
./configure
```

Or, more explicitly, forcing MPI, ScaLAPACK, and FFTW3:

```bash
./configure MPIF90=mpif90 --with-scalapack=yes --with-fftw3=yes
```

If configuration fails, add OpenBLAS explicitly:

```bash
./configure MPIF90=mpif90 --with-scalapack=yes --with-fftw3=yes --with-openblas=yes
```

At the end of the configuration, QE prints a **summary** of what was detected.
Make sure MPI, FFTW, ScaLAPACK, and BLAS are all marked as found.

### 7.2 Compile the Code

```bash
make all
```

For faster compilation on multi-core systems:

```bash
make -j$(nproc) all
```

`$(nproc)` automatically inserts the number of available CPU cores.

> **Compilation time:** On a modern laptop, `make all` takes roughly 10–40
> minutes. It is normal for the terminal to produce a lot of output — that is
> the Fortran compiler working, not an error.

### 7.3 Check the Installation

Navigate to the `bin` directory and list the produced executables:

```bash
cd bin
ls -la *.x
```

You should see files such as:

- `pw.x` — main plane-wave DFT code
- `ph.x` — phonon calculation
- `pp.x` — post-processing
- `dos.x` — density of states
- `projwfc.x` — projected wavefunctions / PDOS
- `cp.x` — Car–Parrinello molecular dynamics

---

## 8. Step 6 — Set Up Environment Variables

To use `pw.x` from any directory, add QE's `bin` folder to your `PATH`, and
define `ESPRESSO_PSEUDO` — the default location for pseudopotential files.

Append to `~/.bashrc`:

```bash
echo '# Quantum ESPRESSO Path' >> ~/.bashrc
echo 'export PATH=$PATH:$HOME/quantum-espresso/qe-7.2/bin' >> ~/.bashrc
echo 'export ESPRESSO_PSEUDO=$HOME/quantum-espresso/pseudo' >> ~/.bashrc
```

Create the pseudo directory:

```bash
mkdir -p ~/quantum-espresso/pseudo
```

Reload the shell configuration:

```bash
source ~/.bashrc
```

From now on, `pw.x` will be available in every new terminal session.

---

## 9. Verification

Check the Fortran compiler:

```bash
gfortran --version
```

Check MPI:

```bash
mpif90 --version
which mpirun
```

Check Quantum ESPRESSO:

```bash
which pw.x
```

If `which pw.x` prints a path ending in `bin/pw.x`, the installation is
complete and ready to use. A quick end-to-end test is to run any of the
examples shipped with QE:

```bash
cd ~/quantum-espresso/qe-7.2/test-suite
make run-tests-pw-serial
```

---

## 10. Troubleshooting

| Symptom                                          | Cause / Fix                                                        |
|--------------------------------------------------|--------------------------------------------------------------------|
| `wsl --install` fails                            | Enable virtualization in BIOS; update Windows to build 19041+.     |
| `./configure` cannot find BLAS/LAPACK/FFTW       | Install the `-dev` packages listed in Step 3.                      |
| `make` fails with "cannot find -lscalapack"      | Reinstall `libscalapack-mpi-dev`.                                  |
| `make` runs out of memory                        | Use `make -j2` instead of `make -j$(nproc)`.                       |
| `pw.x: command not found`                        | Re-run `source ~/.bashrc`, or check the `PATH` in Step 6.          |
| Very slow runs                                   | Run in parallel: `mpirun -np 4 pw.x -in input.in > output.out`.    |
| Pseudopotentials not found                       | Check that `$ESPRESSO_PSEUDO` points to the folder with the `.UPF` files. |

Official references:

- [Quantum ESPRESSO website](https://www.quantum-espresso.org/)
- [QE User Guide](https://www.quantum-espresso.org/Doc/user_guide/)
- [QE pseudopotential library](https://www.quantum-espresso.org/pseudopotentials/)
- [Microsoft WSL documentation](https://learn.microsoft.com/windows/wsl/)

---

## 11. Summary Cheat-Sheet

For quick copy-paste from scratch:

```bash
# 1. Install WSL (in PowerShell as Administrator)
#    wsl --install
#    wsl --set-default-version 2
#    wsl --install -d Ubuntu

# 2. Update Ubuntu
sudo apt update && sudo apt upgrade -y

# 3. Install dependencies
sudo apt install -y build-essential cmake cmake-curses-gui gfortran \
                    liblapack-dev libblas-dev libfftw3-dev libfftw3-mpi-dev \
                    libopenmpi-dev openmpi-bin libscalapack-mpi-dev \
                    libopenblas-dev libelpa-dev wget git curl unzip gnuplot

# 4. Download QE
mkdir -p ~/quantum-espresso && cd ~/quantum-espresso
wget https://www.quantum-espresso.org/rdm-download/8/v7-2/63bf22d8e65ee903f18500994cd32737/qe-7.2-ReleasePack.tar.gz
tar -xzvf qe-7.2-ReleasePack.tar.gz
cd qe-7.2

# 5. Configure and compile
./configure MPIF90=mpif90 --with-scalapack=yes --with-fftw3=yes
make -j$(nproc) all

# 6. Environment
echo 'export PATH=$PATH:$HOME/quantum-espresso/qe-7.2/bin' >> ~/.bashrc
echo 'export ESPRESSO_PSEUDO=$HOME/quantum-espresso/pseudo' >> ~/.bashrc
mkdir -p ~/quantum-espresso/pseudo
source ~/.bashrc

# 7. Verify
which pw.x
```

That's it — you now have Quantum ESPRESSO installed inside WSL, ready to run
DFT calculations.
