## **LAB #0**
### **Installation of Quantum ESPRESSO**

# Quantum ESPRESSO Installation Guide via WSL

## Overview
This guide provides step-by-step instructions to install Quantum ESPRESSO on Windows using Windows Subsystem for Linux (WSL) with Ubuntu.

## Prerequisites
- Windows 10 version 2004 or higher (Build 19041 or higher) OR Windows 11
- Administrator privileges
- Stable internet connection
- At least 20GB free disk space

## Step 1: Install WSL (Windows Subsystem for Linux)

### 1.1 Enable WSL Feature
Open PowerShell **as Administrator** and run:
```
wsl --install 
```

### 1.2 Restart Your Computer
Restart Windows to complete the WSL installation.

### 1.3 Set WSL Version
Open PowerShell and set WSL 2 as default:
```
wsl --set-default-version 2
```

### 1.4 Install Ubuntu
Open Microsoft Store, search for "Ubuntu", and install the latest LTS version (22.04 or newer). Alternatively, install from PowerShell:
```
wsl --install -d Ubuntu
```
Launch Ubuntu from Start Menu. 
Create a username and password when prompted

## Step 2: Update and Upgrade Ubuntu
Open Ubuntu terminal and run:
```
sudo apt update && sudo apt upgrade -y
```

## Step 3: Install Essential Dependencies
### 3.1 Install Build Tools and Compilers
```
sudo apt install -y build-essential cmake cmake-curses-gui
```
### 3.2 Install Fortran Compiler (gfortran)
```
sudo apt install build-essential gfortran liblapack-dev libblas-dev libfftw3-dev libopenmpi-dev wget openmpi-bin libfftw3-mpi-dev libscalapack-mpi-dev libopenblas-dev libelpa-dev git curl unzip gnuplot 
```
## Step 4: Download Quantum ESPRESSO
### 4.1 Create Installation Directory
```
mkdir -p ~/quantum-espresso
cd ~/quantum-espresso
```

## 4.2 Download Source Code
Download the latest version from the official website:
```
# Download Quantum ESPRESSO (replace with latest version)
wget https://www.quantum-espresso.org/rdm-download/8/v7-2/63bf22d8e65ee903f18500994cd32737/qe-7.2-ReleasePack.tar.gz

# Extract the archive
tar -xzvf qe-7.2-ReleasePack.tar.gz
cd qe-7.2
```
Note: Check [webpage](https://www.quantum-espresso.org/ ) for the latest version.

## Step 5: Configure and Compile Quantum ESPRESSO
### 5.1 Configure the Build
```
# Configure for MPI with scalapack and FFTW3
./configure
```
Or optional
```
./configure MPIF90=mpif90 --with-scalapack=yes --with-fftw3=yes
```
If configuration fails, try with more specific options:
```
./configure MPIF90=mpif90 --with-scalapack=yes --with-fftw3=yes --with-openblas=yes
```
### 5.2 Compile the Code
```
make all
```
For faster compilation on multi-core systems:
```
make -j$(nproc) all
```
### 5.3 Check Installation
```
cd bin
ls -la *.x
```
## Step 6: Set Up Environment Variables
Add to ~/.bashrc
```
echo '# Quantum ESPRESSO Path' >> ~/.bashrc
echo 'export PATH=$PATH:$HOME/quantum-espresso/qe-7.2/bin' >> ~/.bashrc
echo 'export ESPRESSO_PSEUDO=$HOME/quantum-espresso/pseudo' >> ~/.bashrc
```
Reload bashrc
```
source ~/.bashrc
```

## Verification Commands
# Check gfortran
```
gfortran --version
```
# Check MPI
```
mpif90 --version
which mpirun
```
# Check Quantum ESPRESSO
```
which pw.x
```

















