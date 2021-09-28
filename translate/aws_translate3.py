#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import boto3


# 翻訳したい文章(英語)を入力する
input_text = raw_input("翻訳したい文章を英語で入力: > ")

# AWSを使った翻訳の準備
translate = boto3.client(service_name="translate")
# 文章を翻訳
translate_text = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="en",
    TargetLanguageCode="ja"
)["TranslatedText"].encode("UTF-8")

# 結果を表示
print("------------------------------------")
print("○  翻訳前: {}".format(input_text))
print("------------------------------------")
print("○  翻訳後: {}".format(translate_text))
