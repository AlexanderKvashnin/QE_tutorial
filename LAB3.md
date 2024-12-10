## **LAB #3**
### **Electronic bands structure**
Before we can run bands calculation, we need to perform single-point self consistent field calculation (after relaxation)
```
pw.x < input.2.scf > output.2.scf
```
Next step is our band calculation (non-self consistent field) calculation. The bands calculation is non self-consistent in the sense that it uses the ground state electron density, Hartree, exchange and correlation potentials determined in the previous step. In case of non self-consistent calculation, the `pw.x` determines the Kohn-Sham eigenfunction and eigenvalues without updating Kohn-Sham Hamiltonian at every iteration. We need to specify the k-points for which we want to calculate the eigenvalues. We can also specify the number of electronic bands required for calculations `nbnd`. Input file `inpute.5.bands`
is for band calculations, while files 
* `inpute.1.opt` is for relaxation
* `inpute.2.scf` is for self-consistent calculation
* `inpute.3.nscf` is for non self-consistent calculation

So, type
```
pw.x < input.5.bands > output.bands
```
The bands are now calculated. 

We need some post-processing in order to obtain the data in more usable manner. 
Need to use `bands.x` program and `input.6.pp` inpute file to run post-processing (PP) module
```
bands.x < input.6.pp > output.pp
```
After this step you will get the text file with electronic bands structure, which can be plotted using template of the python script `bands.py`.

## HOMEWORK
(一). Try to modify the python script to obtain nice electronic bands structure.

(二). Modify the script to plot together bands structure and density of states.

