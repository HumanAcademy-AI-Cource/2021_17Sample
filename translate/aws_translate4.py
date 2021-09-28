#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import boto3


# テキストファイルから文章を読み出す
with open("./aws_translate4.txt") as f:
    input_text = f.read()

# 翻訳前の文章を表示
print("------------------------------------")
print("○  翻訳前: \n{}".format(input_text))
print("------------------------------------")

# AWSを使った翻訳の準備
translate = boto3.client(service_name="translate")

#############################################

# 日本語から英語へ翻訳
translate_en = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="ja",
    TargetLanguageCode="en"
)["TranslatedText"].encode("UTF-8")
# 結果を表示
print("○  翻訳後（英語）:\n{}".format(translate_en))
print("------------------------------------")

#############################################

# 日本語からスペイン語へ翻訳
translate_es = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="ja",
    TargetLanguageCode="es"
)["TranslatedText"].encode("UTF-8")
# 結果を表示
print("○  翻訳後（スペイン語）:\n{}".format(translate_es))
print("------------------------------------")

#############################################

# 日本語からフィンランド語へ翻訳
translate_fi = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="ja",
    TargetLanguageCode="fi"
)["TranslatedText"].encode("UTF-8")
# 結果を表示
print("○  翻訳後（フィンランド語）:\n{}".format(translate_fi))
print("------------------------------------")

#############################################

# 日本語からイタリア語へ翻訳
translate_it = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="ja",
    TargetLanguageCode="it"
)["TranslatedText"].encode("UTF-8")
# 結果を表示
print("○  翻訳後（イタリア語）:\n{}".format(translate_it))
print("------------------------------------")

#############################################

# 日本語からドイツ語へ翻訳
translate_de = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="ja",
    TargetLanguageCode="de"
)["TranslatedText"].encode("UTF-8")
# 結果を表示
print("○  翻訳後（ドイツ語）:\n{}".format(translate_de))
print("------------------------------------")

#############################################

# 日本語からチェコ語へ翻訳
translate_cs = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="ja",
    TargetLanguageCode="cs"
)["TranslatedText"].encode("UTF-8")
# 結果を表示
print("○  翻訳後（チェコ語）:\n{}".format(translate_cs))
print("------------------------------------")

#############################################

# 日本語からロシア語へ翻訳
translate_ru = translate.translate_text(
    Text=input_text,
    SourceLanguageCode="ja",
    TargetLanguageCode="ru"
)["TranslatedText"].encode("UTF-8")
# 結果を表示
print("○  翻訳後（ロシア語）:\n{}".format(translate_ru))
print("------------------------------------")
