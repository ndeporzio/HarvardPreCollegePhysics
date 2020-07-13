#1 Check if you have python3
# Open the "Terminal" app
python3 --version
# If you don't get a version number printed out, complete steps 2-5

#2 Install homebrew                                                               
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
                                                                                
#3 Intall pyenv                                                                   
brew install pyenv                                                              
                                                                                
#4 Install python 3.7.3                                                           
pyenv install 3.7.3                                                             
                                                                                
#5 Activate python                                                                
pyenv global 3.7.3                                                              
pyenv version                                                                   
                                                                                
#Install packages                                                               
pip install numpy                                                               
pip install matplotlib                                                          
                                                                                
#Setup workspace                                                                
cd ~/Desktop                                                                    
mkdir PhysicsWorkshop                                                           
cd PhysicsWorkshop
git clone git@github.com:ndeporzio/HarvardPreCollegePhysics.git


