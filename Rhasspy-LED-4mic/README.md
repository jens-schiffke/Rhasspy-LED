
# Rhasspy-LED
LED-Service for Rhasspy with a Raspberry and ReSpeaker 4-Mics Pi HAT  
  
  Nach dem Wakeword werden die LEDs grün und nach dem Sprachbefehl bis zum Ende des Prozesses blau. Anschließend erlöschen die LEDs wieder.
  einen Button gibt es beim 4-Mics Pi HAT nicht.

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
sudo apt-get install python3-paho-mqtt  
sudo cp /opt/Rhasspy-LED/Rhasspy-LED-4mic/rhasspy-led.service /etc/systemd/system/  
sudo systemctl daemon-reload  
sudo systemctl enable rhasspy-led-4mic.service  
sudo reboot  
