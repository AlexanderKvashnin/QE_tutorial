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

## **Almost line-by-line explanation of the input file for relaxation**
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

Second block belongs to the studied structure. Paramters with necessary comments are below
```
&system
    ibrav=0                        # determine the type of Bravais lattice 
    nat=8                          # number of atoms in the unit cell 
    ntyp=1                         # number of types of atoms in the unit cell
    ecutwfc=60.0                   # kinetic energy cutoff (Ry) for wavefunctions
    occupations = 'smearing'       # type of occupation for electronic bands
    degauss=0.05                   # value of the gaussian spreading (Ry) for brillouin-zone
integration
 /
```
Our example is based on the diamond structure. Here we are using unit cell of 8 arbon atoms, thus the type of the Bravais lattice is selected to be 0. You can try to specify diamond structure using primitive cell of 2 atoms by using special type of the Bravais lattic. See [this](https://www.quantum-espresso.org/Doc/INPUT_PW.html#idm226).

Third block is called `electrons` and here parameters for relaxation of electronic sub-system is specifyed
```
 &electrons
    conv_thr = 1d-12,         # convergence threshold for selfconsistency
    mixing_beta=0.3,          # mixing factor for self-consistency
    electron_maxstep = 100    # maximum number of iterations in a scf step
 /
```

If our calculation type is `relax` or `vc-relax`, then you need to spcify the next block of paramters related to ion relaxation
```
&IONS
  ion_dynamics='bfgs',                  # specify the type of ionic dynamics
  pot_extrapolation = "first_order",    # used to extrapolate the potential from preceding ionic steps
 /
```

In the case of `vc-relax` another block of parameters is required called as `CELL`
```
&CELL
   cell_dynamics = 'bfgs' ,         # specify the type of dynamics for the cell
   cell_factor = 1.5,               # it should exceed the maximum linear contraction of the
cell during a simulation
   press = 0 ,                      # target pressure [KBar] in a variable-cell md or relaxation run
/
```

Next lines are devoted to specification of the atomic species via definintion of the pseudopotential files for each atomic type
```
ATOMIC_SPECIES
C 12 C.pbe-n-rrkjus_psl.1.0.0.UPF
```
Here we specify carbon atom with mass 12 and pseudopotential file with name `C.pbe-n-rrkjus_psl.1.0.0.UPF`. This file should be placed in the folder which you specify in the block `control` using keyword `pseudo_dir`.

Next block is atomic positions which can be specified in different ways (please refer to [this](https://www.quantum-espresso.org/Doc/INPUT_PW.html#idm1495)). As in our example we use diamond fo study, here are coordinated of 8 carbon atoms in the structure using `{crystal}` representations of coordinates. 
```
C 0.250000 0.750000 0.250000 
C 0.000000 0.000000 0.500000 
C 0.250000 0.250000 0.750000 
C 0.000000 0.500000 0.000000 
C 0.750000 0.750000 0.750000 
C 0.500000 0.000000 0.000000 
C 0.750000 0.250000 0.250000 
C 0.500000 0.500000 0.500000 
```
Next we specify the cell parametres of out structure using the following block 
```
CELL_PARAMETERS {Angstrom}
3.573710 0.000000 0.000000
0.000000 3.573710 0.000000
0.000000 0.000000 3.57232
```
Explicit specification of call parameters is requiring only if you have not specified type of the Bravais lattice in the `system` block. Otherwise you do not need this block. See [this](https://www.quantum-espresso.org/Doc/INPUT_PW.html#idm226) for details.

And the final block os devoted to k-point mesh. Here we use automatically generated uniform grid of k-points as specified by the `{automatic}` option, see below
```
K_POINTS {automatic}
  8 8 8 1 1 1
```
