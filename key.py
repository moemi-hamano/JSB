#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from const import KEY_LEFT
from const import KEY_RIGHT
from const import KEY_DOWN
from const import KEY_UP
from const import KEY_ESC


# ----------------------------------------------------------------------------- #
# key main�N���X                                                                      #
# ----------------------------------------------------------------------------- #
class KeyMain:

    # Key�N���X�̃C���X�^���X�쐬
    def __init__(self, mng, app):
        print("[KEY]key init")
        self.mng = mng
        app.bind("<Left>", self.left_key_event)
        app.bind("<Right>", self.right_key_event)
        app.bind("<Down>", self.down_key_event)
        app.bind("<Up>", self.up_key_event)
        app.bind("<Escape>", self.esc_key_event)

    # LeftKey�������m����
    def left_key_event(self, evt):
        print("[KEY]left key down")
        self.mng.receive_key_down_event(KEY_LEFT)

    # RightKey�������m����
    def right_key_event(self, evt):
        print("[KEY]right key down")
        self.mng.receive_key_down_event(KEY_RIGHT)

    # DownKey�������m����
    def down_key_event(self, evt):
        print("[KEY]down key down")
        self.mng.receive_key_down_event(KEY_DOWN)

    # UpKey�������m����
    def up_key_event(self, evt):
        print("[KEY]up key down")
        self.mng.receive_key_down_event(KEY_UP)

    # EscKey�������m����
    def esc_key_event(self, evt):
        print("[KEY]esc key down")
        self.mng.receive_key_down_event(KEY_ESC)
