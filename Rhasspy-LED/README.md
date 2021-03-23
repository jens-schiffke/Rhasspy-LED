
# Rhasspy-LED
LED-Service for Rhasspy with a Raspberry and ReSpeaker 2-Mics Pi HAT  
  
  Nach dem Wakeword werden die LEDs grün und nach dem Sprachbefehl bis zum Ende des Prozesses blau. Anschließend erlöschen die LEDs wieder.
  Man kann die Funktion durch einen kurzen Tastendruck auf den Button (de)aktivieren.
  Drückt man 3 Sekunden, wird das Mikro aus- bzw. angeschaltet.
  Hält man den Button 10 Sekunden gedrückt, leuchtet die LED für 2 Sekunden rot und der RPI wird heruntergefahren. Nach ca. 30 Sekunden kann man ihn dann vom Strom trennen.

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
sudo apt-get install python3-pip  
sudo pip3 install rpi.gpio  
sudo pip3 install apa102_pi  
sudo apt-get install python3-paho-mqtt  
sudo cp /opt/Rhasspy-LED/Rhasspy-LED/rhasspy-led.service /etc/systemd/system/  
sudo systemctl daemon-reload  
sudo systemctl enable rhasspy-led.service  
sudo reboot  
