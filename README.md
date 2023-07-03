# SNU MVI Detection TEAM
* Codes and materials repository
* Seperate directories for each user
* Mainly based on PyTorch & MONAI

## How To Access (fastmri2)

ssh -L 2222:localhost:8888 fastmri2@147.46.121.39 -p 22  
jupyter lab  

http://localhost:2222  

unset DISPLAY  
coss_vgpu -g 1  
conda activate snumvi

git config --global credential.helper cache  
git config --global --unset credential.helper
