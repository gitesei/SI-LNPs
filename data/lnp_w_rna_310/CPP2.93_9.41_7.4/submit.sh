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
#SBATCH -J ../lnp_298/CPP2.93_9.41_7.4
#
# filenames stdout and stderr
#SBATCH -o out
#SBATCH -e err

source /home/gtesei00/.bashrc
module load GCCcore/12.3.0
module load CMake/3.26.3
module load GCC/12.3.0
conda activate faunus

#/home/gtesei00/Jun22/faunus/faunus --input ine1.json --output oute1.json
#/home/gtesei00/Jun22/faunus/faunus --input ine2.json --output oute2.json --state state_e1.json -v0
#sed -i -e 's/": -0.9999999999999999/": 5.01422348404507/g' state_e2.json
/home/gtesei00/Jun22/faunus/faunus --input inp.json --output outp.json --state state.json -v0