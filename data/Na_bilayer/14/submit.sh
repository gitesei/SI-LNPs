#!/bin/bash
#requesting the number of cores needed on exclusive nodes
#SBATCH -p tetralith
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -A snic2021-5-246
#
# job time, change for what your job requires
#SBATCH -t 20:0:0
#
# job name
#SBATCH -J 45018_14
#
# filenames stdout and stderr
#SBATCH -o out
#SBATCH -e err

module load CMake/3.16.5
module load buildtool-easybuild/4.3.1-nsc1aeca6f
module load GCCcore/8.2.0

source /home/x_giute/.bashrc
conda activate myenv

#/home/x_giute/faunus/faunus --verbosity 1 --input ine.json --output oute.json 
/home/x_giute/faunus/faunus --verbosity 1 --input inp.json --output outp.json --state state.json 