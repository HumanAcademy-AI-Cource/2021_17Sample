#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import boto3


# テキストファイルから文章を読み出す
with open("./aws_translate2.txt") as f:
    input_text = f.read()

# AWSを使った翻訳の準備
translate = boto3.client(service_name="translate")
# テキストファイルから読み込んだ文章を翻訳
translate_text = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="en",
    TargetLanguageCode="ja"
)["TranslatedText"].encode("UTF-8")

# 結果を表示
print("------------------------------------")
print("○  翻訳前: \n{}".format(input_text))
print("------------------------------------")
print("○  翻訳後: \n{}".format(translate_text))
