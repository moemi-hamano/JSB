#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
import random
from tetris_square import TetrisSquare
from const import TETRIMINO_SHAPE_O
from const import TETRIMINO_SHAPE_I
from const import TETRIMINO_SHAPE_T
from const import TETRIMINO_SHAPE_L
from const import TETRIMINO_SHAPE_J
from const import TETRIMINO_SHAPE_Z
from const import TETRIMINO_SHAPE_S
from const import TETRIMINO_COLOR_O
from const import TETRIMINO_COLOR_I
from const import TETRIMINO_COLOR_T
from const import TETRIMINO_COLOR_L
from const import TETRIMINO_COLOR_J
from const import TETRIMINO_COLOR_Z
from const import TETRIMINO_COLOR_S
from const import TETRIS_FIELD_WIDTH


# ----------------------------------------------------------------------------- #
# tetris blockクラス                                                                  #
# ----------------------------------------------------------------------------- #
# テトリスのブロックを作成するクラス
class TetrisBlock:

    def __init__(self):
        print("[TETRIS_BLOCK]tetris_block init")
        # ブロックを構成するリスト
        self.squares = []
        color = None
        cords = None

        # ブロックの形をランダムに決定
        # TODO kashida to 濱野さん テスト用にblock_typeを1で固定させています。適宜削除して、乱数指定に修正してください。
        # block_type = random.randint(1, 7)
        block_type = 1
        if block_type == TETRIMINO_SHAPE_O:
            color = TETRIMINO_COLOR_O
            cords = [
                [TETRIS_FIELD_WIDTH / 2, 0],
                [TETRIS_FIELD_WIDTH / 2, 1],
                [TETRIS_FIELD_WIDTH / 2 - 1, 0],
                [TETRIS_FIELD_WIDTH / 2 - 1, 1],
            ]

        # 決定した色と座標の正方形を作成してリストに追加
        for cord in cords:
            self.squares.append(TetrisSquare(cord[0], cord[1], color))

    # ブロックを構成する正方形を取得
    def get_squares(self):

        return self.squares

    # ブロックを移動
    def move(self, direction):

        # ブロックを構成する正方形を移動
        for square in self.squares:
            x, y = square.get_moved_cord(direction)
            square.set_cord(x, y)
