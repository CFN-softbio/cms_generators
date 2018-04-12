# Install

1. create a conda environment
2. conda create -n cms-generator python=3.5 numpy matplotlib h5py scipy ipython lxml pillow
3. conda activate cms-generator
4. Install extra pims module
    conda install -c soft-matter pims
5. install SciAnalysis: 
    pip install git+https://www.github.com/CFN-Softbio/SciAnalysis

6. in cms_generators/simluation.py, modify these lines:
    # location of SciAnalysis
    SciAnalysis_PATH="/home/lhermitte/research/projects/code-profiling/SciAnalysis"
    # location of masks
    mask_dir ="/home/lhermitte/research/projects/code-profiling/masks"
    # place where to save data
    root_dir ="/home/lhermitte/research/projects/code-profiling/data"

    to the directories desired


# To run the generator
After installation, To run, in folder with simulation.py run:
python simulation.py

