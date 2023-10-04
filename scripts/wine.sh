https://wiki.winehq.org/Ubuntu

sudo dpkg --add-architecture i386 

sudo mkdir -pm755 /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key

f"sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/{distro_code}/winehq-{distro_code}.sources"

sudo apt install --install-recommends winehq-stable


https://wiki.winehq.org/Debian

sudo dpkg --add-architecture i386 

sudo mkdir -pm755 /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key

	
f"sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/{distro_code}/winehq-{distro_code}.sources"

sudo apt install --install-recommends winehq-stable
