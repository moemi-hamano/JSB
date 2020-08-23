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

    # ゲームオーバーかどうかを判断
    def judge_game_over(self, block):

        # フィールド上で既に埋まっている座標の集合作成
        no_empty_cord = set(square.get_cord() for square
                            in self.get_squares() if square.get_color() != TETRIS_BACK_GROUND_COLOR)

        # ブロックがある座標の集合作成
        block_cord = set(square.get_cord() for square
                         in block.get_squares())

        # ブロックの座標の集合と
        # フィールドの既に埋まっている座標の集合の積集合を作成
        collision_set = no_empty_cord & block_cord

        # 積集合が空であればゲームオーバーではない
        if len(collision_set) == 0:
            ret = False
        else:
            ret = True

        return ret

    # 指定した方向にブロックを移動できるかを判断
    def judge_can_move(self, block, direction):

        # フィールド上で既に埋まっている座標の集合作成
        no_empty_cord = set(square.get_cord() for square
                            in self.get_squares() if square.get_color() != TETRIS_BACK_GROUND_COLOR)

        # 移動後のブロックがある座標の集合作成
        move_block_cord = set(square.get_moved_cord(direction) for square
                              in block.get_squares())

        # フィールドからはみ出すかどうかを判断
        for x, y in move_block_cord:

            # はみ出す場合は移動できない
            if x < 0 or x >= self.width or \
                    y < 0 or y >= self.height:
                return False

        # 移動後のブロックの座標の集合と
        # フィールドの既に埋まっている座標の集合の積集合を作成
        collision_set = no_empty_cord & move_block_cord

        # 積集合が空なら移動可能
        if len(collision_set) == 0:
            move_pos_ret = True
        else:
            move_pos_ret = False

        return move_pos_ret
