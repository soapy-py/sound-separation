#!/bin/bash
#SBATCH --job-name=jupyter_notebook
#SBATCH --output=outLogs/notebook%j.out
#SBATCH --error=outLogs/notebook%j.err
#SBATCH --mem=6Gb
#SBATCH -n 1 
#SBATCH -N 1
#SBATCH --time=6:00:00
#SBATCH --partition=normal
#SBATCH --cpus-per-task=1
#SBATCH -x node091

module add openmind/anaconda/3-2019.10

export HDF5_USE_FILE_LOCKING=FALSE


source activate /scratch2/weka/mcdermott/schen77/conda_envs/slots



export LC_ALL=C; unset XDG_RUNTIME_DIR && jupyter notebook --no-browser --ip='0.0.0.0' --port=1234 --NotebookApp.allow_origin='*'
