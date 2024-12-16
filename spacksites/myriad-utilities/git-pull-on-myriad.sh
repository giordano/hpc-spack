#!/bin/bash
# git stash is because spack_sites.ini will have been edited w.r.t to the repo for the root of the spack sites. 
git stash
git pull
sed -i "s%sites_root =.*%sites_root = ${HOME}/repo/hpc-spack%" "${HOME}/repo/hpc-spack/spacksites/settings/spack_sites.ini"
