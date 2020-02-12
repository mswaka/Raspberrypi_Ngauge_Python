# Raspberry pi zeroからPWM制御して鉄道模型を動かす。

# Overview

[Raspberrypi_Ngauge_Python/ngauge.py](https://github.com/mswaka/Raspberrypi_Ngauge_Python/blob/master/ngauge.py) - PythonからラズパイのGPIOを制御して、PWMドライバーを制御して鉄道模型を動かすプログラム

[Raspberrypi_Ngauge_Python/volume.py](https://github.com/mswaka/Raspberrypi_Ngauge_Python/blob/master/volume.py) - ボリュームを回すとADコンバータからGPIOを通って、SPI通信して、Pythonでデータが取得できるプログラム

[Raspberrypi_Ngauge_Python/controller.py](https://github.com/mswaka/Raspberrypi_Ngauge_Python/blob/master/controller.py) - ボリュームを回した値を、PWMのデューティー比に渡して制御するプログラム(キュー・イベント駆動)

[Raspberrypi_Ngauge_Python/controller2.py](https://github.com/mswaka/Raspberrypi_Ngauge_Python/blob/master/controller2.py) - ボリュームを回した値を、PWMのデューティー比に渡して制御するプログラム(シーケンシャル)

[Raspberrypi_Ngauge_Python/controller3.py](https://github.com/mswaka/Raspberrypi_Ngauge_Python/blob/master/controller3.py) - ボリュームを回した値を、PWMのデューティー比に渡すのと、PWMの周波数に渡して制御するプログラム

# LICENSE

MIT LICENSEです。

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

# YouTube

使い方動画です。

[![](https://img.youtube.com/vi/75QfVEN4zzc/0.jpg)](https://www.youtube.com/watch?v=75QfVEN4zzc)
