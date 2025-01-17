# source this - it sets up shell environment variable
# this is to use the installation of hpc spack on Myriad as user ccspapp


if [[ "$USER" == "ccspapp" ]]; then

    cd /home/ccspapp/Scratch/spack/0.20/hpc-spack
    alias sps=/home/ccspapp/Scratch/spack/0.20/hpc-spack/spacksites/spacksites
    source  /home/ccspapp/Scratch/spack/0.20/hpc-spack/spacksites/process-env-scripts/spack-deps-rhel-7.8.sh
    pip install --user pyyaml
    echo "An alias has been set:"
    echo "       alias sps=/home/ccspapp/Scratch/spack/0.20/hpc-spack/spacksites/spacksites"
    echo "This will disappear if you use 'bash' to get another shell, e.g. prior to entering a particular spack site."
    echo "This script has called spack-deps-rhel-7.8.sh to load gcc from RHEL's devtoolset 11 and python38 also from RHEL to run spacksites."
    echo "Also a dependency, pyyaml, of spacksites has been installed"
    echo "Do an 'sps list' to test."

else

    echo "This script expects that you are using the installation of spack for user ccspapp"
    echo "You are not logged in as such - so this script has done nothing"

fi
