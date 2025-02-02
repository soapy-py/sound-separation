#!/bin/bash

#SBATCH --output=/om2/user/schen77/logs/job_log_%j.out 	# name of job outlog (print statements go here by default)
#SBATCH --error=/om2/user/schen77/logs/job_log_%j.err  	# name of job error log (error messages show up here) 


set -e
set -x

poetry install

chmod +x download_clevr.sh
./download_clevr.sh

python slot_attention/train.py
