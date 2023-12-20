# -*- coding: utf-8 -*-

import pyaudio
import wave
import pyttsx3
import os
from pydub import AudioSegment

class Microphone:
    def __init__(self):
        self.db = None

    @staticmethod
    def get_audio(_time=1) -> None:
        """
        录制麦克风声音并保存为临时音频文件
        :param _time: 录制时间
        :return: None
        """
        _CHUNK = 256  # 数据块大小
        _FORMAT = pyaudio.paInt16  # 数据格式
        _CHANNELS = 1  # 通道数
        _RATE = 11025  # 采样率
        _RECORD_SECONDS = _time  # 录制时间
        _WAVE_OUTPUT_FILENAME = ".temp.wav"  # 临时音频文件名

        p = pyaudio.PyAudio()
        stream = p.open(format=_FORMAT,
                        channels=_CHANNELS,
                        rate=_RATE,
                        input=True,
                        frames_per_buffer=_CHUNK)
        frames = []
        for i in range(0, int(_RATE / _CHUNK * _RECORD_SECONDS)):
            data = stream.read(_CHUNK)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(_WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(_CHANNELS)
        wf.setsampwidth(p.get_sample_size(_FORMAT))
        wf.setframerate(_RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    def get_decibel(self) -> None:
        """
        获取音频文件的分贝
        :return: None
        """
        sound = AudioSegment.from_file(".temp.wav", "wav")  # 加载WAV文件
        _db = sound.dBFS  # 取得音频文件的声音分贝值
        _x = [i for i in range(0, 101)]
        _x.reverse()
        if str(_db) == "-inf":
            _db = -100
        self.db = _x[abs(int(_db))]
        print(self.db)

    def play_people_sound(self, _db, _name) -> None:
        """
        播放指定文字
        :param _db: 分贝
        :param _name: 文字
        :return: None
        """
        if self.db >= _db:
            _x = self.db / 100
            engine = pyttsx3.init()
            engine.setProperty("volume", _x)
            engine.say(_name)
            engine.runAndWait()
            engine.getProperty("volume")

    def play_sound_recording(self, _db) -> None:
        """
        播放录音
        :return: None
        """
        if self.db >= _db:
            _CHUNK = 1024
            wf = wave.open(".temp.wav", 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            data = wf.readframes(_CHUNK)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(_CHUNK)
            stream.stop_stream()
            stream.close()
            wf.close()
            p.terminate()

    def play_sound_lili(self, _db, _name) -> None:
        """
        指定音频
        :param _name:
        :param _db: 分贝
        :return: None
        """
        if self.db >= _db:
            _CHUNK = 1024
            wf = wave.open(_name, 'rb')
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            data = wf.readframes(_CHUNK)
            while len(data) > 0:
                stream.write(data)
                data = wf.readframes(_CHUNK)
            stream.stop_stream()
            stream.close()
            wf.close()
            p.terminate()

def getinput(msg: str):
    while True:
        try:
            return int(input(msg).strip())
        except TypeError:
            continue

def main():
    my_main = Microphone()
    print("睡觉神器,启动! 如果你的室友狗叫, 以以下方式回击(输入序号):")
    sounds = os.listdir("./sounds/")
    for n, i in enumerate(sounds):
        print(f"[{n + 1}]  {i[:-4]}")
    
    selected = getinput(">") - 1

    
    db = getinput("输入反击触发阈值(1-100):")

    while True:
        my_main.get_audio()
        my_main.get_decibel()
        my_main.play_sound_lili(db, "./sounds/" + sounds[selected])


if __name__ == '__main__':
    try:
        main()
    except OSError as e:
        if e.args[1] == "Invalid input device (no default output device)":
            print("请连接音响和麦克风.")
            exit()