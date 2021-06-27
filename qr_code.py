""" make qrcode """
# coding: utf-8
import os
import sys

import qrcode

DEFAULT_FILE_NAME = 'default_qr_code.png'


def make_qrcode(qr_string, file_name):
    """ qrcodeライブラリを利用
    - 与えられたfile_nameで保存出来なければソースのあるディレクトリに保存する。
    """
    path_sep = os.sep
    img = qrcode.make(qr_string)
    current_dir = os.getcwd()
    try:
        img.save(file_name)
    except FileNotFoundError:
        print('{}が間違っています'.format(file_name))
        file_name = current_dir + path_sep + DEFAULT_FILE_NAME
        img.save(file_name)
    img_address = "{0}".format(file_name)
    return img_address


if __name__ == "__main__":
    args = sys.argv
    len_args = len(args)
    if len_args == 1:
        file_name = 'qr_code.png'
        qr_string = input()
    elif len_args == 2:
        file_name = args[1]
    else:
        print('引数は作成するQRコードのフルパスだけです。')
        sys.exit()
    print("QRコードに変換したい文字列を入力してください: ", end="")
    qr_string = input()
    file_address = make_qrcode(qr_string, file_name)
    print("「{0}」にQRコード画像を保存しました".format(file_address))
