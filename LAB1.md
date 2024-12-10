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

## **Useful script**
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
You can easily check how fast energy converges with respect to relaxation steps.
All required information about the structure is summarized in the output file named `output.opt`
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

(*) Try to write your one-line script to get the atomic positions


## **HOMEWORK**
(一). Choose the structure of semiconductore (covalent material) from the materials project database (_https://next-gen.materialsproject.org/_)

(二). Perform convergence test w.r.t. k-points mesh (`K_POINTS`), cutoff energy (`ecutwfc`).

(三). Plot the dependence of the lattice constants and energy on the accuracy paramters. 

(四). Chose optimal paramters for further calculations and explain your choise. 

## **Advanced HOMEWORK**
(六). Use `relax` keyword in the input in order to calculate Equation of states (EOS), e.g. `E(V)` dependence.

(七). Calculate bulk modulus of your structure using EOS. 
