#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
import tkinter as tk
from key import KeyMain
from timer import TimerMain
from main_exit import main_exit_routine
from const import KEY_LEFT
from const import KEY_RIGHT
from const import KEY_DOWN
from const import KEY_UP
from const import KEY_ESC


# ----------------------------------------------------------------------------- #
# managerクラス                                                                    #
# ----------------------------------------------------------------------------- #
class ManagerMain:

    # Managerクラスのインスタンス作成
    def __init__(self):
        print("[MNG]manager init")
        # アプリ(tkinter)インスタンス生成
        self.app = tk.Tk()
        self.app.geometry("200x100")
        # キーインスタンス生成
        self.key = KeyMain(self, self.app)
        # タイマインスタンス生成
        self.timer = TimerMain(self, self.app)

    # ゲーム開始
    def start_event(self):
        # タイマ開始
        self.timer.timer_start()
        # アプリの待機及びイベント処理待機開始
        self.app.mainloop()

    # テトリミノ移動
    def tetrimino_move(self, key):
        print("[MNG]tetrimino_move", key)

    # テトリミノ落下
    def tetrimino_drop(self):
        print("[MNG]tetrimino_drop")

    # キーが押下された時のイベント
    def receive_key_down_event(self, key):
        print("[MNG]receive_key_down_event", key)
        if key == KEY_LEFT or key == KEY_RIGHT or key == KEY_DOWN:
            self.tetrimino_move(key)
        if key == KEY_UP:
            self.tetrimino_drop()
        if key == KEY_ESC:
            main_exit_routine()

    # タイマ満了イベント
    def timer_expired_event(self):
        print("[MNG]timer expired")
        # TODO kashida to 担当の方 タイマが満了になった時の処理
        # タイマを再スタート
        self.timer.timer_start()
