## **LAB #5**
### **Mechanical properties**

This LAB work is devoted to calculations of elastic properties of materials using Density Functional Theory as impelemnted in the `Quantum ESPRESSO` program.

All required files are located in the `5.Mech` folder.

The you can find several input files with names `input.relax.N`, where N is the deformation of the crystal (you will see later).

Second idea of this LAB is to show that you can construct a single script file which will do multiple calculations.
The main information (i.e. main script) is `job`. If you will open it you will find many lines of the codes. 

First several lines are 

`
#!/bin/bash
#SBATCH -J dos # Job name
#SBATCH -o job.%j.out # Name of stdout output file (%j expands to %jobId)
#SBATCH -N 1 # Total number of nodes requested
#SBATCH -n 4 # Total number of mpi tasks #requested
#SBATCH -t 999:00:00 # Run time (hh:mm:ss) - 1.5 hours
`
which are service lines for task scheduler which is installed on the cluster. Most HPC cluster are working under the scheduler systems like this. Here all the information about your task is specified, namely, name of the job, name of the standard output file `job.%j.out`, number of compute nodes, number of cores and computational time. 

Script `get_data.sh` is for collecting data after the calculations

(一). Try to understand what is written in the scripts

(二). Why do we have such types of scripts and such type of the calculations?

(三). What output information do we obtain?
