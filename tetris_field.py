#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from tetris_square import TetrisSquare
from const import TETRIS_FIELD_WIDTH
from const import TETRIS_FIELD_HEIGHT
from const import TETRIS_BACK_GROUND_COLOR


# ----------------------------------------------------------------------------- #
# tetris fieldクラス      　　　　　                                               #
# ----------------------------------------------------------------------------- #
# テトリス画面のフィールド
class TetrisField:

    def __init__(self):
        print("[TETRIS_FIELD]tetris_field init")
        self.width = TETRIS_FIELD_WIDTH
        self.height = TETRIS_FIELD_HEIGHT

        # フィールドを初期化
        self.squares = []
        for y in range(self.height):
            for x in range(self.width):
                # フィールドを正方形インスタンスのリストとして管理
                self.squares.append(TetrisSquare(x, y, TETRIS_BACK_GROUND_COLOR))

    def get_width(self):
        # フィールドの正方形の数（横方向）を取得
        return self.width

    def get_height(self):
        # フィールドの正方形の数（縦方向）を取得
        return self.height

    def get_squares(self):
        # フィールドを構成する正方形のリストを取得
        return self.squares

    def get_square(self, x, y):
        # 指定した座標の正方形を取得
        return self.squares[y * self.width + x]
