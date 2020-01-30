# ros_ledstrip
Raspberry Pi上のROSで動くパッケージで、フルカラーLEDを光らせることができます。
17時から23時まで点灯します。
## 導入&実行
まずLEDの一番長い足を3.3Vに、他をGPIO18、23、24に接続してください。

GPIOを使う準備をします。

```
sudo sh -c "echo 18 > /sys/class/gpio/export"
sudo sh -c "echo 23 > /sys/class/gpio/export"
sudo sh -c "echo 24 > /sys/class/gpio/export"
sudo sh -c "echo out > /sys/class/gpio/gpio18/export"
sudo sh -c "echo out > /sys/class/gpio/gpio23/export"
sudo sh -c "echo out > /sys/class/gpio/gpio24/export"
```

ワークスペースでクローンします。

```
cd /<ワークスペース>/src
git clone https://github.com/sendai01/ros_ledstrip.git
```

ビルドして実行しましょう。

```
cd ../
catkin_make -j 1
roslaunch ros_ledstrip ros_ledstrip.launch
```

コードをいじると色を変えたり、点灯時刻を変えることもできます😇

## 終了する

満足したら`ctrl+c`で終了し、そしてGPIOの後始末をしてください

```
sudo sh -c "echo 18 > /sys/class/gpio/unexport"
sudo sh -c "echo 23 > /sys/class/gpio/unexport"
sudo sh -c "echo 24 > /sys/class/gpio/unexport"
```
