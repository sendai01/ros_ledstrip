# ros_ledstrip
Raspberry Pi上のROSで動くLEDテープを光らせるパッケージです。
17時から23時まで点灯します。
## 導入
GPIOを使う準備をします。
'''
sudo sh -c "echo 18 > /sys/class/gpio/export"
sudo sh -c "echo 23 > /sys/class/gpio/export"
sudo sh -c "echo 24 > /sys/class/gpio/export"
sudo sh -c "echo out > /sys/class/gpio/gpio18/export"
sudo sh -c "echo out > /sys/class/gpio/gpio23/export"
sudo sh -c "echo out > /sys/class/gpio/gpio24/export"
'''
ワークスペースでクローンします。
'''
git clone https://github.com/sendai01/ros_ledstrip.git
'''
ビルドして実行しましょう。
'''
cd ../
catkin_make -j 1
roslaunch ros_ledstrip ros_ledstrip.launch
'''
