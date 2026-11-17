# ucd-hpc

- **Kind:** agent skill
- **Owner:** West Coast Metabolomics Center, Gert Wohlgemuth
- **Status:** public
- **Source:** https://github.com/berlinguyinca/ucdhpc-cluster-skill

## What it does

Teaches an AI agent how to work on the HPC@UCD clusters Farm, Franklin and Hive: finding the right account, partition and limits, writing and submitting Slurm jobs, and checking on them. Facts about each cluster are kept as configuration rather than prose, so they can be updated in one place.

## Tools or commands

- A cluster summary script that prints partitions, limits, GPUs and storage for one cluster.
- An installer that copies the skill to a cluster login node and links it for Claude Code, Codex, OpenCode and pi.
- Reference notes on Slurm usage for each cluster.

## Access

- **Writes:** none by itself. The skill guides an agent that submits jobs under your own cluster account.
- **Sign-in:** your own HPC@UCD account.
- **How to get access:** public; install it from the repository.

## Install

Clone the repository and run its install script, locally or on a cluster login node. See the repository README.

## How it was checked

The repository includes evals that test an agent's answers about each cluster against the configuration.
