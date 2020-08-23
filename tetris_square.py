#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from const import TETRIS_BACK_GROUND_COLOR
from const import KEY_LEFT
from const import KEY_RIGHT
from const import KEY_UP


# ----------------------------------------------------------------------------- #
# tetris squareクラス                                                                      #
# ----------------------------------------------------------------------------- #
# ブロックの座標を設定するクラス
class TetrisSquare:

    def __init__(self, x=0, y=0, color=TETRIS_BACK_GROUND_COLOR):
        print(f"[TETRIS_SQUARE]tetris_square init x={x} y={y}")
        # 1つの正方形を作成
        self.x = x
        self.y = y
        self.color = color

    def set_cord(self, x, y):
        # 正方形の座標を設定
        self.x = x
        self.y = y

    def get_cord(self):
        # 正方形の座標を取得
        return int(self.x), int(self.y)

    def set_color(self, color):
        # 正方形の色を設定
        self.color = color

    def get_color(self):
        # 正方形の色を取得
        return self.color

    # 移動後の正方形の座標を取得
    def get_moved_cord(self, direction):
        # 移動前の正方形の座標を取得
        x, y = self.get_cord()

        # 移動方向を考慮して移動後の座標を計算
        if direction == KEY_LEFT:
            return x - 1, y
        elif direction == KEY_RIGHT:
            return x + 1, y
        # elif direction == KEY_DOWN:
        # return
        elif direction == KEY_UP:
            return x, y + 1
        else:
            return x, y
