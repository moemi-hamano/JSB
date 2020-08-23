#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
import tkinter as tk
from key import KeyMain
from timer import TimerMain
from tetris_field import TetrisField
from display import DisplayMain
from tetris_block import TetrisBlock
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
        # キーインスタンス生成
        self.key = KeyMain(self, self.app)
        # タイマインスタンス生成
        self.timer = TimerMain(self, self.app)
        # ブロックの管理リストを初期化
        self.tetris_field = TetrisField()
        # 落下ブロックをセット
        self.block = None
        # ディスプレイインスタンス生成
        self.display = DisplayMain(self.app, self.tetris_field)

    # ゲーム開始
    def start_event(self):
        # タイマ開始
        self.timer.timer_start()
        # 落下ブロックを新規追加
        self.new_block()

    def new_block(self):
        # ブロックを新規追加

        # 落下中のブロックインスタンスを作成
        self.block = TetrisBlock()

        if self.tetris_field.judge_game_over(self.block):
            self.end_func()
            print("GAME OVER")

        # テトリス画面をアップデート
        self.display.canvas.update(self.tetris_field, self.block)

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
