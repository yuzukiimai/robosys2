# Robosys2_ROS_Package
___

## 概要

2021年度ロボットシステム学の課題2で作成したROSパッケージです。

2つのノード（パブリッシャとサブスクライバの関係）を用いています。

片方のノードで、1秒に1回、1～100までの乱数を発生させて、もう片方のノードに乱数データを送り、それが3のつく数字もしくは3の倍数であれば、某芸人が出てきて数字を叫んでくれます。

___

## 動作環境

- Raspberry Pi 3 Model B
- ubuntu 20.04 server
- ROS Noetic
- Python 3

___

## 使用方法

### 【インストール】

以下のコマンドを実行してください。

``` 
$ cd ~/catkin_ws/src

$ git clone https://github.com/yuzukiimai/robosys2.git 

$ cd ..

$ catkin_make
```
___

### 【実行】

※ページ下に実行時の動画があります。

インストール後に以下のコマンドを実行してください。

___

#### 1. 端末①でroscoreを立ち上げる

```
$ roscore
```

___

#### 2. 端末②でrand.pyのプログラムを立ち上げる

```
$ rosrun robosys2 rand.py
```

___

#### 3. 端末③でrand.pyの出力を確認する
```
$ rostopic echo /rand_number
```

___

#### 4. 端末④でnabeatu.pyのプログラムを立ち上げる
```
$ rosrun robosys2 nabeatu.py
```

___

## デモ動画

https://youtu.be/eBlk2m3OMB8

___

## ライセンス
[BSD 3-Clause License](https://github.com/yuzukiimai/robosys2/blob/master/LICENSE)
