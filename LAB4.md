## **LAB #4**
### **Phonon calculations**
In `Quantum ESPRESSO`, phonon dispersion is calculated using `ph.x` program, which is the implementation of density functional perturbation theory (DFPT).

Here are the steps for calculating phonon dispersion (thought that structure is fully relaxed):

(一). Perform SCF calculation using `pw.x`
```
pw.x < input.scf > output.scf
```
#### Comments
* Usually higher energy cutoff values are used for phonon calculation to get better accuracy.
* In case of two-dimensional systems, use assume_isolated = '2D' in the SYSTEM namelist to avoid negative or imaginary acoustic frequencies near Γ-point. Read more in [here](https://doi.org/10.1103/PhysRevB.96.075448).

(二). calculate the dynamical matrix on a uniform mesh of q-points using `ph.x`. Input file `ph.in` is in the `4.PH`
```
ph.x < ph.in > ph.out
```
The above calculation is computationally demanding, so, probably it is better to run simpler system

### Comments
* You can restart an interrupted `ph.x` calculation with `recover = .true.` keyword in the `INPUTPH` namelist of `ph.in` file. You can cleanly exit an ongoing calculation by creating an empty file with name `{prefix}.EXIT.`

(三). perform inverse Fourier transform of the dynamical matrix to obtain inverse Fourier components in real space using `q2r.x`. You can find `q2r.in` in the `4.PH` folder and type
```
q2r.x < q2r.in > q2r.out
```
(四). Finally, perform Fourier transformation of the real space components to get the dynamical matrix at any `q` by using `matdyn.x.`
```
matdyn.x < matdyn.freq.in > matdyn.freq.out
```

(五). Then you can now plot the phonon dispersion of GaAs using the draft of python script in the `4.PH` folder。

As a result you will obtain similar picture.

![image](https://github.com/user-attachments/assets/7b1ac319-2787-4491-b451-4e3e60c9b15b)


(七). Now we can calculate the phonon density of states. Input file for phonon DOS calculation is in `matdyn.dos.in` in the `4.PH` folder
```
matdyn.x < matdyn.dos.in > matdyn.dos.out
```
And plot the phonon DOS by using the dtemplate of the corresponding python script.
As example you will obtain the following picture
![dos](https://github.com/user-attachments/assets/463bbce6-d58d-46e2-be4b-8ef9fa760ac4)

