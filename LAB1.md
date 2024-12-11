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

### **Almost line-by-line explanation of the input file for relaxation**
Description of all keywords for every input file in `QE` is located [here](https://www.quantum-espresso.org/Doc/INPUT_PW.html)  

As one can note from the example of `input.1.opt` file presented in the `1.OPT` folder input file contains blocks of key parameters which are respondible for specifying of different parts of the task.

Each block is started from the `&` symbol. This is specific character allowing QE to understant the blocks.
First block named as `control` is here 
```
 &control
    calculation  = 'vc-relax'            # type of the calculations, see the beginning of the LAB
    restart_mode = 'from_scratch'        # do we need to start with previous steps of relaxation?
    pseudo_dir   = './'                  # directory where required pseudopotential files are located 
    outdir       = './'                  # directory where the output and auxilary files are stored to
    prefix = 'C'                         # prepended to input/output filenames
    forc_conv_thr=1.0d-4                 # convergence threshold on forces (a.u)
    etot_conv_thr=1.0d-5                 # convergence threshold on total energy (a.u)
    nstep=1000
 /
```
