#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import boto3
import subprocess
import wave


# 発話させたい文章
input_text = raw_input("発話させたい文章を入力 > ")

# 発話させたい文章を表示
print("------------------------------------")
print("○  発話させたい文章: {}".format(input_text))
print("------------------------------------")

# AWSを使った音声合成の準備
polly = boto3.client(service_name="polly")

# 音声合成を実行
speech_data = polly.synthesize_speech(
    Text=input_text,
    OutputFormat='pcm',
    VoiceId='Mizuki'
)['AudioStream']

# 音声合成の結果をWAVデータとして保存する
wave_data = wave.open("speech.wav", 'wb')
wave_data.setnchannels(1)
wave_data.setsampwidth(2)
wave_data.setframerate(16000)
wave_data.writeframes(speech_data.read())
# ファイルを閉じる
wave_data.close()

# 保存したWAVデータを再生
subprocess.check_call('aplay -D plughw:0 {}'.format("speech.wav"), shell=True)
