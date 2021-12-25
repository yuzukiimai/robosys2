# Robosys2_ROS_Package
___

## 概要

2021年度ロボットシステム学の課題2で作成したROSパッケージです。

2つのノード（パブリッシャとサブスクライバの関係）を活用しています。

片方のノードで、1秒1回、1～100までの乱数を発生させて、もう片方のノードに乱数データを送り、それが3のつく数字もしくは3の倍数であれば、某芸人が出てきて数字を叫んでくれます。

___

## 動作環境

- Raspberry Pi 3 Model B
- ubuntu 20.04 server
- ROS Noetic
- Python 3

___

## 使用方法

### 【インストール】

``` 
$ cd ~/catkin_ws/src
```

```
$ git clone https://github.com/yuzukiimai/robosys2.git 
```

```
$ cd ..
```

```
$ catkin_make
```

