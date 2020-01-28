# Raspberry pi zeroのpythonでPWM制御して鉄道模型を動かす。

# Description

Raspberrypi_Ngauge_Python/ngauge.py - PythonからラズパイのGPIOを制御して、PWMドライバーを制御して鉄道模型を動かすプログラム

Raspberrypi_Ngauge_Python/volume.py - ボリュームを回すとADコンバータからGPIOを通って、SPI通信して、Pythonでデータが取得できるプログラム

# 必要なもの
Raspberry pi zero

# OS
Rasbian OS

# AutoStart
/etc/rc.local

python /home/pi/ngauge.py
