## **LAB #5**
### **Mechanical properties**

This LAB work is devoted to calculations of elastic properties of materials using Density Functional Theory as impelemnted in the `Quantum ESPRESSO` program.

All required files are located in the `5.Mech` folder.

The you can find several input files with names `input.relax.N`, where N is the deformation of the crystal (you will see later).

Second idea of this LAB is to show that you can construct a single script file which will do multiple calculations.
The main information (i.e. main script) is `job`. If you will open it you will find many lines of the codes. 

First several lines are 

```
#!/bin/bash
#SBATCH -J dos # Job name
#SBATCH -o job.%j.out # Name of stdout output file (%j expands to %jobId)
#SBATCH -N 1 # Total number of nodes requested
#SBATCH -n 4 # Total number of mpi tasks #requested
#SBATCH -t 999:00:00 # Run time (hh:mm:ss) - 1.5 hours
```
which are service lines for task scheduler which is installed on the cluster. Most HPC cluster are working under the scheduler systems like this. Here all the information about your task is specified, namely, name of the job, name of the standard output file `job.%j.out`, number of compute nodes, number of cores and computational time. `j` is the external variable determining the `jobID`.

After this you will find another line 
```
module load mpi/intel qe/7.2
```
which is responsbile for the load of special modulus. Here we load Intel MPI for parallel computing and `qe-7.2` which is `Quantum ESPRESSO` ver. 7.2, installed on the cluser. It needs to run programs without knowing where it is located.

Next line is specification of the working directory for this LAB and `cd` command to go to this folder. 
```
DIR=/home/elgatito/BACKUP1/students/tutorial/5.Mech
cd $DIR
```
This is internal variable which has a value only within this script. 

Next two lines define the `for` loop 
```
for i in 0990 0995 1000 1005 1010
do
```
Here variable `i` takes values in a loop equal to 0990, 0995, 1000, 1005, 1010 define the relative deformation of our unit cell. Why do we need to specify them is such a strange way? We split here variables needed for deformation and for naming of the files. 

Variable `A` determines the actual lattice parameter for which we will perform the calculations, and defines as
```
A=$(echo "scale=10; $i/1000*3.570387185" | bc);
```
Here the number `3.570387185` is the lattice parameter of relax structure which you obtained during [LAB#1](https://github.com/AlexanderKvashnin/QE_tutorial/blob/main/LAB1.md)
Now you can understand that `i` means the relative deformation times 1000. So 0990 means 0.99 raio of deformation. Why so? It is no so convenient to use names of files with dot, like `input.relax.0.99`. Different linux shells can process with such files in a wrong way. To be in a safe zone we substitute 0.99 by 0990 within the `i` variable. 

Then we have special construction inside which we can specify entire input file which will be created
```
cat << EOF > $DIR/input.relax.$i
```
Here we are creating `input.relax.$i` in the `$DIR` folder. When you call variable you need to use `$` sign.
All line below this one will written to the input file while the program will meet the line `EOF`.
Between `cat` and `EOF` you can find all line which you are familiar with. 
The most important part here is specification of lattice parameters in the lines 
```
CELL_PARAMETERS {Angstrom}
$A 0.000000 0.000000
0.000000 3.573710 0.000000
0.000000 0.000000 3.573710
```
You can find that instead of the lattice parameter `a` here we put the variable `$A` which defines in the beginning of the script.

Final line is 
```
mpirun -np 4 pw.x < input.relax.${i} | tee output.relax.${i}
```
which runs the `pw.x` with inpute file with the name  `input.relax.${i}` and create output file with the name `output.relax.${i}`. 

Now you can run this script by submitting it to the queue using the command
```
sbatch job
```

## **Post-processing**

You will get several output files, where you can find all necessary information.
For the convenient there is another script which will help to extract all the data. Imagine that you will have 1000 output files? How can you get information from 1000 files?
Script `get_data.sh` is a linux bash script allowing extraction of information from the output files. 

You can run it using the command
```
sh get_data.sh
```
After which you will get several files
```
data.c11
data.c12
data.c13
data.cell
```
Here you have `stress-strain` dependencies, which sould be approximated by the linear function in order to find `Cij` constants. 


## **HOMEWORK**
(一). Try to understand the physical meaning of the script? 

(二). Construct 3x3 matrix of elastic constants containing C11, C22, C33 and all valuable non-diagonal elements.

(三). How can we calculate elastic constant C22, C33?

(四). How many files do you obtain after the script `job` is finished?

(五). What output information do we obtain by using `get_data.sh` script?

(六). Why this LAB is limited for elastic deformations? How can we change the script to perform the simulations of larger deformations (plastic regime)? 
