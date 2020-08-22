#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from TetrisJSB_manager import manager_main
from TetrisJSB_const import KEY_LEFT
from TetrisJSB_const import KEY_RIGHT
from TetrisJSB_const import KEY_DOWN
from TetrisJSB_const import KEY_UP
from TetrisJSB_const import KEY_ESC

# ----------------------------------------------------------------------------- #
# key main�N���X                                                                      #
# ----------------------------------------------------------------------------- #
class key_main():

    # Key�N���X�̃C���X�^���X�쐬
    def __init__(self, mng, tk):
        print("[KEY]key init")
        self.mng = mng
        tk.bind("<Left>", self.left_key_event)
        tk.bind("<Right>", self.right_key_event)
        tk.bind("<Down>", self.down_key_event)
        tk.bind("<Up>", self.up_key_event)
        tk.bind("<Escape>", self.esc_key_event)

    # LeftKey�������m����
    def left_key_event(self, evt):
        print("[KEY]left key down")
        self.mng.recieve_key_down_event(KEY_LEFT)

    # RightKey�������m����
    def right_key_event(self, evt):
        print("[KEY]right key down")
        self.mng.recieve_key_down_event(KEY_RIGHT)

    # DownKey�������m����
    def down_key_event(self, evt):
        print("[KEY]down key down")
        self.mng.recieve_key_down_event(KEY_DOWN)

    # UpKey�������m����
    def up_key_event(self, evt):
        print("[KEY]up key down")
        self.mng.recieve_key_down_event(KEY_UP)

    # EscKey�������m����
    def esc_key_event(self, evt):
        print("[KEY]esc key down")
        self.mng.recieve_key_down_event(KEY_ESC)
