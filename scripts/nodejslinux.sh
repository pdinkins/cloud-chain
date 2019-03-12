# Verify that you have all required tools
sudo apt-get install python g++ make checkinstall fakeroot
# Create tmp dir and switch to it
src=$(mktemp -d) && cd $src
# Download the latest version of Node
wget -N http://nodejs.org/dist/node-latest.tar.gz
# Extract the content of the tar file
tar xzvf node-latest.tar.gz && cd node-v*
# Run configuration
./configure
# Create .deb for Node
sudo fakeroot checkinstall -y --install=no --pkgversion $(echo $(pwd) | sed -n -re's/.+node-v(.+)$/\1/p') make -j$(($(nproc)+1)) install
# Replace [node_*] with the name of the generated .deb package of the previous step
sudo dpkg -i node_*
