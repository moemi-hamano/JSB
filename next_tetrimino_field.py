#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from next_tetrimino_area import NextTetriminoArea
from const import NEXT_TETRIMINO_FIELD_WIDTH
from const import NEXT_TETRIMINO_FIELD_HEIGHT
from const import NEXT_TETRIMINO_BACK_GROUND_COLOR


# ----------------------------------------------------------------------------- #
# next tetrimino fieldクラス                                                             #
# ----------------------------------------------------------------------------- #
# 次のテトリミノ表示画面のフィールド
class NextTetriminoField:

    def __init__(self):
        print("[NEXT_TETRIMINO_FIELD]next_tetrimino_field init")
        self.width = NEXT_TETRIMINO_FIELD_WIDTH
        self.height = NEXT_TETRIMINO_FIELD_HEIGHT

        self.square = NextTetriminoArea(self.width, self.height, NEXT_TETRIMINO_BACK_GROUND_COLOR)

    def get_width(self):
        # フィールドの正方形の数（横方向）を取得
        return self.width

    def get_height(self):
        # フィールドの正方形の数（縦方向）を取得
        return self.height
