#!/bin/bash
#requesting the number of cores needed on exclusive nodes
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -A lu2022-2-36
#
# job time, change for what your job requires
#SBATCH -t 100:0:0
#
# job name
#SBATCH -J 600
#
# filenames stdout and stderr
#SBATCH -o out
#SBATCH -e err

source /home/gtesei00/.bashrc
module load GCCcore/9.3.0
module load CMake/3.16.4
module load GCC/9.3.0
conda activate faunus

/home/gtesei00/Jun22/faunus/faunus --input inp.json --output outp.json -v0 # --state state.json 