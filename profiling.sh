#!/bin/bash
#SBATCH --job-name=profiling     # create a short name for your job
#SBATCH --output=logs/job_log_%j.out 	# name of job outlog (print statements go here by default)
#SBATCH --error=logs/job_log_%j.err  	# name of job error log (error messages show up here) 
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem=4G                 # total memory per node
#SBATCH --time=00:05:00          # total run time limit (HH:MM:SS)
#SBATCH --partition=normal      	# part of the cluster to use: use-every, normal, mcdermott
#SBATCH --gres=gpu:a100:1

module add openmind/anaconda/3-2019.10     # how to add modules you need eg python reqs like conda 
source activate /scratch2/weka/mcdermott/schen77/conda_envs/slots    # eg activate conda env

python -m pyheat /om2/user/schen77/prj-slots/idk.py --out "profiling.png" 

