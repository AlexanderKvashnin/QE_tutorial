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
Here the number `3.570387185` is the lattice parameter of relax structure which you obtained during LAB#1
Now you can understand that `i` means the relative deformation times 1000. So 0990 means 0.99 raio of deformation. Why so? It is no so convenient to use names of files with dot, like `input.relax.0.99`. Different linux shells can process with such files in a wrong way. To be in a safe zone, we substitute 0.99 by 0990 within the `i` variable. 




Script `get_data.sh` is for collecting data after the calculations

(一). Try to understand what is written in the scripts

(二). Why do we have such types of scripts and such type of the calculations?

(三). What output information do we obtain?
