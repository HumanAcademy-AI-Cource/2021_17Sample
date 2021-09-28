# -*- coding: utf-8 -*-
from pydub import AudioSegment
import subprocess
import os
import csv


# 発話させたい文章
input_text = "こんにちは"

# 発話させたい文章を表示
print("------------------------------------")
print("○  発話させたい文章: {}".format(input_text))
print("------------------------------------")


# wavesフォルダの中身を読み込む
voices = {}
for filename in os.listdir("./waves"):
    name, ext = os.path.splitext(filename)
    voices[name] = AudioSegment.from_file("./waves/{}".format(filename), "wav")

# 母音の対応表を読み込む
vowel = {}
with open("./vowel.csv", "r") as f:
    for row in csv.reader(f):
        sp_row = row[0].split(" ")
        vowel[sp_row[0]] = sp_row[1]

# 文字をわける
words = []
for word in list(unicode(input_text, 'utf-8')):
    encode_word = word.encode('utf_8')
    if encode_word == "ゃ" or encode_word == "ゅ" or encode_word == "ょ":
        words[-1] += encode_word
    elif encode_word == "ー" or encode_word == "～":
        words.append(vowel[words[-1]])
    else:
        words.append(encode_word)

# 先頭に無音の音声を追加
sound = AudioSegment.from_file("./waves/無音.wav", "wav")

# わけた文字を使って音声合成
for word in words:
    if word in voices:
        sound += voices[word]
    else:
        print("「{}」の音声データがありませんでした。".format(word))

# 末尾に無音の音声を追加
sound += AudioSegment.from_file("./waves/無音.wav", "wav")

# 合成した音声をWAVで保存
sound.export("speech.wav", format="wav")

# 保存したWAVデータを再生
subprocess.check_call('aplay -D plughw:0 {}'.format("speech.wav"), shell=True)
