# Install
1. create a conda environment

2. Create the environment with the right packages:

`conda create -n cms-generator -c soft-matter pims python=3.5 numpy matplotlib h5py scipy ipython lxml pillow`

`conda activate cms-generator`

3. install SciAnalysis: 

    `pip install git+https://www.github.com/CFN-Softbio/SciAnalysis`

4. Clone this repo somewhere:

    `git clone https://www.github.com/CFN-Softbio/cms_generators`

    `cd cms_generators/cms_generators`

5. Edit the simulation.py code:

    - the mask directory:
        - mask_dir ="/home/lhermitte/research/projects/code-profiling/masks"
    - place where to save data
        - root_dir ="/home/lhermitte/research/projects/code-profiling/data"
    - sample metadata filename
        - meta_filename = "sample_meta.yml"

    You'll probably just need to modify the middle line

6. Run the simulator:
    `python simulator.py`

    This will create data in your root dir. The data is an hdf5 file:
        - img: the image
        - attribures : the metadata attributes

    The image will be an image with the same dimensions as the Pilatus 2M
    detector
