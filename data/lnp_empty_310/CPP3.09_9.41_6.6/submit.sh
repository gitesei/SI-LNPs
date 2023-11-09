#!/bin/bash
#requesting the number of cores needed on exclusive nodes
#SBATCH -N 1
#SBATCH --ntasks-per-node=1
#SBATCH -A lu2023-2-83
#
# job time, change for what your job requires
#SBATCH -t 48:0:0
#
# job name
#SBATCH -J ../lnp_310/CPP3.09_9.41_6.6
#
# filenames stdout and stderr
#SBATCH -o out
#SBATCH -e err

source /home/gtesei00/.bashrc
module load GCCcore/12.3.0
module load CMake/3.26.3
module load GCC/12.3.0
conda activate faunus

/home/gtesei00/Jun22/faunus/faunus --input inp.json --output outp.json --state state.json -v0