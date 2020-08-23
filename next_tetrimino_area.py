#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from const import TETRIS_BACK_GROUND_COLOR


# ----------------------------------------------------------------------------- #
# next tetrimino areaクラス                                                         #
# ----------------------------------------------------------------------------- #
# 次のテトリミノ表示画面領域の作成(ブロックの座標を設定するクラス(TetrisSquareクラス)と処理は同じ)
class NextTetriminoArea:

    def __init__(self, x=0, y=0, color=TETRIS_BACK_GROUND_COLOR):
        print(f"[NEXT_TETRIMINO_AREA]next_tetrimino_area init")
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


