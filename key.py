#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from const import KEY_LEFT
from const import KEY_RIGHT
from const import KEY_DOWN
from const import KEY_UP
from const import KEY_ESC


# ----------------------------------------------------------------------------- #
# key mainクラス                                                                      #
# ----------------------------------------------------------------------------- #
class KeyMain:

    # Keyクラスのインスタンス作成
    def __init__(self, mng, app):
        print("[KEY]key init")
        self.mng = mng
        app.bind("<Left>", self.left_key_event)
        app.bind("<Right>", self.right_key_event)
        app.bind("<Down>", self.down_key_event)
        app.bind("<Up>", self.up_key_event)
        app.bind("<Escape>", self.esc_key_event)

    # LeftKey押下検知処理
    def left_key_event(self, evt):
        print("[KEY]left key down")
        self.mng.receive_key_down_event(KEY_LEFT)

    # RightKey押下検知処理
    def right_key_event(self, evt):
        print("[KEY]right key down")
        self.mng.receive_key_down_event(KEY_RIGHT)

    # DownKey押下検知処理
    def down_key_event(self, evt):
        print("[KEY]down key down")
        self.mng.receive_key_down_event(KEY_DOWN)

    # UpKey押下検知処理
    def up_key_event(self, evt):
        print("[KEY]up key down")
        self.mng.receive_key_down_event(KEY_UP)

    # EscKey押下検知処理
    def esc_key_event(self, evt):
        print("[KEY]esc key down")
        self.mng.receive_key_down_event(KEY_ESC)
