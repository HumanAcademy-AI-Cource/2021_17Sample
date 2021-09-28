#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ライブラリのインポート
import boto3


# テキストファイルから文章を読み出す
with open("./aws_translate5.txt") as f:
    input_text = f.read()

# 翻訳前の文を表示
print("------------------------------------")
print("○  翻訳前:\n{}".format(input_text))
print("------------------------------------")

# AWSを使った翻訳の準備
translate = boto3.client(service_name="translate")

############################################


def honyaku(text, source, target):
    """
    AWSを使って簡単に翻訳できるようにした関数
    """

    result = translate.translate_text(
        Text=text,
        SourceLanguageCode=source,
        TargetLanguageCode=target
    )["TranslatedText"].encode("UTF-8")
    return result

#############################################


# 日本語から英語へ翻訳
translate_en = honyaku(input_text, "ja", "en")
# 英語への翻訳結果から日本語に翻訳
translate_ja = honyaku(translate_en, "en", "ja")
print("○  英語から日本語:\n{}".format(translate_ja))
print("------------------------------------")

#############################################

# 英語からスペイン語に翻訳
translate_es = honyaku(translate_en, "en", "es")
# スペイン語への翻訳結果から日本語に翻訳
translate_ja = honyaku(translate_es, "es", "ja")
print("○  スペイン語から日本語:\n{}".format(translate_ja))
print("------------------------------------")

#############################################

# スペイン語からフィンランド語に翻訳
translate_fi = honyaku(translate_es, "es", "fi")
# フィンランド語への翻訳結果から日本語に翻訳
translate_ja = honyaku(translate_fi, "fi", "ja")
print("○  フィンランド語から日本語:\n{}".format(translate_ja))
print("------------------------------------")

#############################################

# フィンランド語からイタリア語に翻訳
translate_it = honyaku(translate_fi, "fi", "it")
# イタリア語への翻訳結果から日本語に翻訳
translate_ja = honyaku(translate_it, "it", "ja")
print("○  イタリア語から日本語:\n{}".format(translate_ja))
print("------------------------------------")

#############################################

# イタリア語からドイツ語に翻訳
translate_de = honyaku(translate_it, "it", "de")
# ドイツ語への翻訳結果から日本語に翻訳
translate_ja = honyaku(translate_de, "de", "ja")
print("○  ドイツ語から日本語:\n{}".format(translate_ja))
print("------------------------------------")

#############################################

# ドイツ語からチェコ語に翻訳
translate_cs = honyaku(translate_de, "de", "cs")
# チェコ語への翻訳結果から日本語に翻訳
translate_ja = honyaku(translate_cs, "cs", "ja")
print("○  チェコ語から日本語:\n{}".format(translate_ja))
print("------------------------------------")

#############################################

# チェコ語からロシア語に翻訳
translate_ru = honyaku(translate_cs, "cs", "ru")
# ロシア語への翻訳結果から日本語に翻訳
translate_ja = honyaku(translate_ru, "ru", "ja")
print("○  ロシア語から日本語:\n{}".format(translate_ja))
