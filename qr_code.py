""" make qrcode """
# coding: utf-8
import os
import sys

import qrcode


def make_qrcode(qr_string, file_name):
    """ qrcodeライブラリを利用 """
    img = qrcode.make(qr_string)
    try:
        img.save(file_name)
        img_address = "{}".format(file_name)
    except FileNotFoundError:
        img_address = None
    return img_address, img


if __name__ == "__main__":
    args = sys.argv
    len_args = len(args)
    if len_args == 1:
        path_sep = os.sep
        current_dir = os.getcwd()
        file_name = current_dir + path_sep + 'qr_code.png'
    elif len_args == 2:
        file_name = args[1]
    else:
        print('引数は作成するQRコードのフルパスだけです。')
        sys.exit()
    print("QRコードに変換したい文字列を入力してください: ", end="")
    qr_string = input()
    img_address, img = make_qrcode(qr_string, file_name)
    if img_address:
        print("「{}」にQRコード画像を保存しました".format(img_address))
        img.show()
    else:
        print('{}が間違っています'.format(file_name))
