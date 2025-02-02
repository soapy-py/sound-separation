#!/bin/bash
#SBATCH --job-name=audioslots_l1 		     # what shows up on the slurm job cue 
#SBATCH --output=logs/job_log_%j.out 	# name of job outlog (print statements go here by default)
#SBATCH --error=logs/job_log_%j.err  	# name of job error log (error messages show up here) 
#SBATCH --mem=16Gb               	# amount of memory you want for this job
#SBATCH --cpus-per-task=1       	# number of cpu cores for the task
#SBATCH --time=8:00:00          	# wall time. Either HH:MM:SS or D-HH:MM:SS
#SBATCH --partition=normal      	# part of the cluster to use: use-every, normal, mcdermott
#SBATCH --gres=gpu:a100:1

module add openmind/anaconda/3-2019.10     # how to add modules you need eg python reqs like conda 
source activate /scratch2/weka/mcdermott/schen77/conda_envs/slots    # eg activate conda env

export WANDB_CONFIG_DIR='wandb'
#CUDA_VISIBLE_DEVICES=0 
python /om2/user/schen77/prj-slots/slot_attention/train_audio.py

#python -m cProfile -o programm.prof /om2/user/schen77/prj-slots/idk.py
