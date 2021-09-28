#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import csv

# 翻訳したい文章(英語)
input_text = "I like robots."

# CSVを読み込んで辞書データを作成
dictionary = {}
with open("./dictionary.csv", "r") as f:
    for row in csv.reader(f):
        if len(row) > 0:
            sp_row = row[0].split(" ")
            dictionary[sp_row[0]] = sp_row[1]


# 翻訳したい文を分割
texts = []
sp_text = input_text.lower().split(".")
for st in sp_text:
    # スペースで単語を区切る
    words = st.split(" ")
    # 無の要素があったら削除
    while "" in words:
        words.remove("")
    # 1単語も含まれていない配列は除いてtextsに追加
    if len(words) > 0:
        texts.append(words)


# 辞書データを元に翻訳してみる
translate_text = ""
# 文単位で展開
for text in texts:
    # 単語単位で展開
    for index, word in enumerate(text):
        # -------------------------------------------------
        # 単語が辞書データにある場合は日本語訳を取り出す
        if word in dictionary:
            translate_word = dictionary[word]
            # 取り出した日本語訳がNoneの場合は空にする
            if translate_word == "None":
                translate_word = ""
        # 単語が辞書データにない場合は元の単語を表示する
        else:
            translate_word = word
        # -------------------------------------------------
        # 翻訳した単語を連結
        translate_text += translate_word
    # 文章の終わりに句点を追加
    translate_text += "。"

# 翻訳した文を表示
print("------------------------------------")
print("○  翻訳前: {}".format(input_text))
print("------------------------------------")
print("○  翻訳後: {}".format(translate_text))
