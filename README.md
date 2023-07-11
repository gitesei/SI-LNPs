# pH-sensitive coarse-grained model of mRNA lipid nanoparticles

This repository contains Python code, [Jupyter](http://jupyter.org) Notebooks, and data for reproducing the results presented in the manuscript _Lipid shape and packing are key for optimal design of pH sensitive mRNA lipid nanoparticles_.

### Usage

To open the Notebooks, install [Miniconda](https://conda.io/miniconda.html) and make sure all required packages are installed by issuing the following terminal commands

```bash
    conda env create -f environment.yml
    source activate faunus
    jupyter-notebook
```

#### Commands to install [Faunus](https://mlund.github.io/faunus/) 

```bash
    tar xvfj faunus.tar.bz2
    conda activate faunus
    cmake . -DENABLE_MPI=OFF -DCMAKE_BUILD_TYPE=Release -DENABLE_OPENMP=OFF
    make faunus -j4
```

#### Contributors

[Giulio Tesei (@gitesei)](https://github.com/gitesei)

[Mikael Lund (@mlund)](https://github.com/mlund)
