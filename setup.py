#Install homebrew                                                               
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
                                                                                
#Intall pyenv                                                                   
brew install pyenv                                                              
                                                                                
#Install python 3.7.3                                                           
pyenv install 3.7.3                                                             
                                                                                
#Activate python                                                                
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


