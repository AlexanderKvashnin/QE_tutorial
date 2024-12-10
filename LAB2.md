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
