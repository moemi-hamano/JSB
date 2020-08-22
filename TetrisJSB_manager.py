#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from TetrisJSB_main_exit import main_exit_routine
from TetrisJSB_const import KEY_LEFT
from TetrisJSB_const import KEY_RIGHT
from TetrisJSB_const import KEY_DOWN
from TetrisJSB_const import KEY_UP
from TetrisJSB_const import KEY_ESC

# ----------------------------------------------------------------------------- #
# managerクラス                                                                    #
# ----------------------------------------------------------------------------- #
class manager_main():

    # Managerクラスのインスタンス作成
    def __init__(self):
        print("manager init")

    def tetrimino_move(self, key):
        print("[MNG]tetrimino_move", key)

    def tetrimino_drop(self):
        print("[MNG]tetrimino_drop")

    def recieve_key_down_event(self, key):
        print("[MNG]recieve_key_down_event", key)
        if key == KEY_LEFT or key == KEY_RIGHT or key == KEY_DOWN:
            self.tetrimino_move(key)
        if key == KEY_UP:
            self.tetrimino_drop()
        if key == KEY_ESC:
            main_exit_routine()
