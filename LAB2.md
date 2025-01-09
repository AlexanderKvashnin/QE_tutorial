## **LAB #2**
### **Electronic density of states**
Before we can run the Density of States (DOS) calculation the structure should be fully relaxed (see [LAB #1](https://github.com/AlexanderKvashnin/QE_tutorial/blob/main/LAB1.md)).
Then, after relaxation you need to 

(一). Perform fixed-ion self consistent filed (**scf**) calculation with denser k-point grid. Here you need to change the keywork `calculation` as follows
```
calculation='scf'
```
and change k-point mesh
```
K_POINTS {automatic}
12 12 12  0 0 0
```

Input files for this simulation is located in [2.DOS](https://github.com/AlexanderKvashnin/QE_tutorial/tree/main/2.DOS) folder. 

We use the lattice constant value that we have obtained from the relaxation calculation ([1.OPT](https://github.com/AlexanderKvashnin/QE_tutorial/tree/main/1.OPT)). We should not directly use the experimental/real lattice constant value. Depending on the method and pseudo-potential, it might result stress in the system. 

After all these changes you can run the `scf` calculation by the command
```
pw.x < input.2.scf > output.scf
```

(二). Next, we have prepared the input file for the **nscf** calculation (`input.3.nscf`). 

Fix the parameters (`ecutwfc` etc.) according to convergence test and run non-self consistent field (**nscf**) calculation with denser k-point grid.
The keyword `calculation` should be 
```
calculation='nscf'
```

You should also add the occupations in the `&system` card as `tetrahedra` (appropriate for DOS calculation). 
Then change k-point mesh to a denser one, like 12 × 12 × 12 with automatic option
```
K_POINTS {automatic}
12 12 12  0 0 0
```
Also specify `nosym = .TRUE.` to avoid generation of additional k-points in low symmetry cases. 
`outdir` and `prefix` must be the same as in the scf step, some of the inputs and output are read from previous step.

Now you can run this calculation with the following command

```
pw.x < input.3.nscf > output.nscf
```

Now our final step is to calculate the density of states (DOS).
The DOS input file is `input.4.dos` with the following several lines 
```
&DOS
  prefix='C',
  outdir='./',
  fildos='C.dos.dat',  # name of the text DOS file
  emin=-30.0,          # minimum energy for calculations of DOS
  emax=30.0            # maximum energy for calculations of DOS
/
```

All these lines are responsible for calculations of electronic DOS.
Now you can type

```
dos.x < input.4.dos > output.dos
```
The DOS data in the `C.dos.dat` file that we specified in our input file `input.4.dos`. 


## **HOMEWORK**
(一). Run DOS calculation of your structure.

(二). Adopt and use a draft of the python script from the `2.DOS` folder to plot density of state function.

(三). Define correct Fermi energy and the band gap of your semiconductor.

(四). Compare your result with available literature data (experimental or theoretical). Explain the differencem if any.

## **Advanced HOMEWORK**
(六). Try to use metaGGA functionals to obtain more accurate value of the band gap. You can use `TB09` or others which are availabe in the `Quantum ESPRESSO` by specifying `input_dft` keyword in the input file for scf, nscf calculations.
```
"tpss"  = "sla+pw+tpss+tpss"  = TPSS Meta-GGA
"m06l"  = "nox+noc+m6lx+m6lc" = M06L Meta-GGA
"tb09"  = "sla+pw+tb09+tb09"  = TB09 Meta-GGA
```
#### Comments
* To do this you need to compile `Quantum ESPRESSO` with Libxc library, which should be installed [separately](https://www.quantum-espresso.org/Doc/user_guide/node13.html).

(七). Plot densities of electronic of states calculated with different meta-GGA functional to compare it with default one
