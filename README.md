# Raspberry pi zeroからPWM制御して鉄道模型を動かす。

# Overview

[Raspberrypi_Ngauge_Python/ngauge.py](https://github.com/mswaka/Raspberrypi_Ngauge_Python/blob/master/ngauge.py) - PythonからラズパイのGPIOを制御して、PWMドライバーを制御して鉄道模型を動かすプログラム

[Raspberrypi_Ngauge_Python/volume.py](https://github.com/mswaka/Raspberrypi_Ngauge_Python/blob/master/volume.py) - ボリュームを回すとADコンバータからGPIOを通って、SPI通信して、Pythonでデータが取得できるプログラム

# 必要なもの
1. Raspberry pi zero
2. PWMドライバー TB6643KQ
3. ACアダプター12V1A
4. 鉄道模型

# OS
Rasbian OS

# AutoStart
/etc/rc.localを開いて、exit 0の前に、下記の実行文を記述します。

python /home/pi/ngauge.py
