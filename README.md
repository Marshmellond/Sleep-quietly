<div align="center"><h1>大学宿舍睡觉神器</h1></div>
<div align="center"><img src="https://www.freeimg.cn/i/2023/12/19/6581a1983bb3e.png" ></div>

## 如果你的舍友有如下情况

- 每到晚上就兴奋
- 打开游戏对麦喷
- 外放声音刷视频
- 无缘无故叫飞起
- 不到凌晨不作罢
- 打扰他人睡美觉

## 那么本项目能帮你解决痛点
当麦克风检测到周围环境音大于某个分贝时，将会自动播放

支持模式

- [x] 播放系统警告声
- [] 播放指定一段话
- [] 播放录音
- [x] 播放指定音频 [wav格式]


## 预设声音

- 1.wav 大早上的你叫啥啊
- 2.wav 你在狗叫什么
- 3.wav 还在看手机
- 4.wav 雪豹闭嘴

## 运行效果图
<img src="https://s2.loli.net/2023/12/19/Rl8OKnJ6ITMzw9V.png" >

## 环境

# 安装 ffmpeg
https://ffmpeg.org/

```shell
# 克隆仓库
git clone https://github.com/Marshmellond/Sleep-quietly.git
cd Sleep-quietly

# 使用conda
conda create -n sleep python=3.11
conda activate sleep
pip install -r requirements.txt
# 启动
python main.py
```

> Linux 安装 pyaudio前 需要安装依赖

```shell
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
```

## 项目结构

```shell
┌Project
├─sound  预设声音
│      1.wav  预设文件
│      2.wav  预设文件
│      ... 
└─main.py  主类
```

### 声明：本项目纯属娱乐，切勿入戏太深