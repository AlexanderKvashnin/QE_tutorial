# CMAS
QE tutorial for Skoltech course on Computational Methods in Atomistic Simulations (CMAS) 

## **LAB #1**
### **Structure relaxation with QE**
There are two types of calculations for structural optimization in `Quantum ESPRESSO`:

(1) **relax**    : where only the atomic positions are allowed to relax

(2) **vc-relax** : which allows to relax both the atomic positions and lattice. 

Input file for relaxation is located in `1.OPT` folder. 
To run the calculations type the command (QE should be installed on you machine)
```
pw.x < input.1.opt > output.opt
```
After a while you will find `output.opt` file in the folder.

## **Useful code**
To get the energy values from the `output.opt` just type 
```
grep ! output.opt
```
The output is the following 
```
!    total energy              =     -99.34993586 Ry
!    total energy              =     -99.34992504 Ry
!    total energy              =     -99.34996266 Ry
!    total energy              =     -99.34996271 Ry
!    total energy              =     -99.34993847 Ry
```
You can easily checke how fast energy converges with respect to relaxation time.
All required information about the structure is summarized in the output file
Similar command to get lattice parameters is
```
grep -A3 CELL_PARAMETERS output.opt | tail -3
```
which gives you the following information 
```
   3.570331383   0.000000000   0.000000000
   0.000000000   3.570331383   0.000000000
   0.000000000   0.000000000   3.570557570
```

Try to write you one-line script to get the atomic positions

## **HOMEWORK**
(一). Choose the structure of semiconductore (covalent material) from the materials project database (_https://next-gen.materialsproject.org/_)

(二). Perform convergence test w.r.t. k-points mesh (`K_POINTS`), cutoff energy (`ecutwfc`).

(三). Plot the dependence of the lattice constants and energy on the accuracy paramters. 

(四). Chose optimal paramters for further calculations and explain your choise. 

## **Advanced HOMEWORK**
(六). Use `relax` keyword in the input in order to calculate Equation of states (EOS), e.g. `E(V)` dependence.

(七). Calculate bulk modulus of your structure using EOS. 

## **LAB #2**
### **Electronic density of states**
Before we can run the Density of States (DOS) calculation, we need to

(一). Perform fixed-ion self consistent filed (**scf**) calculation with denser k-point grid.

(二). Fix the parameters (`ecutwfc` etc.) and run non-self consistent field (**nscf**) calculation with denser k-point grid.

Input files for this simulation is located in `2.DOS` folder. 
We use the lattice constant value that we obtained from the relaxation calculation (1.OPT). We should not directly use the experimental/real lattice constant value. Depending on the method and pseudo-potential, it might result stress in the system. We run the scf calculation:
```
pw.x < input.2.scf > output.scf
```
Next, we have prepared the input file for the **nscf** calculation (`input.3.nscf`). Where we have added occupations in the `&system` card as tetrahedra (appropriate for DOS calculation). We have increased the number of k-points to 12 × 12 × 12 with automatic option. Also specify `nosym = .TRUE.` to avoid generation of additional k-points in low symmetry cases. `outdir` and `prefix` must be the same as in the scf step, some of the inputs and output are read from previous step.
```
pw.x < input.3.nscf > output.nscf
```
Now our final step is to calculate the density of states (DOS). The DOS input file is `input.4.dos` and need to type
```
dos.x < input.4.dos > output.dos
```
The DOS data in the `C.dos.dat` file that we specified in our input file `input.4.dos`. 

## **HOMEWORK**
(一). Run DOS calculation of your structure.

(二). Adopt and use a draft of the python script from the `2.DOS` folder to plot density of state function.

(三). Define correct Fermi energy and the band gap of your semiconductor.

(四). Compare your result with available literature data (experimental or theoretical). Explain the differencem if any.

## **LAB #3**
### **Electronic bands structure**



