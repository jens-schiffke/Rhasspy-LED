# Rhasspy-LED
LED-Service for Rhasspy with a Raspberry and ReSpeaker 2-Mics Pi HAT

#### Install Driver  
sudo apt-get update  
sudo apt-get upgrade  
git clone https://github.com/respeaker/seeed-voicecard.git  
cd seeed-voicecard  
sudo ./install.sh  
reboot  

#### Install Service  
Use 'raspi-config' to enable SPI.  
cd /opt  
sudo git clone https://github.com/jens-schiffke/Rhasspy-LED.git  
sudo pip3 install rpi.gpio  
sudo pip3 install apa102_pi  
sudo cp /opt/Rhasspy-LED/Rhasspy-LED/rhasspy-led.service /etc/systemd/system/  
sudo systemctl daemon-reload  
sudo systemctl enable rhasspy-led.service  
sudo reboot  
