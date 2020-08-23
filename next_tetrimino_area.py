#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from const import TETRIS_BACK_GROUND_COLOR


# ----------------------------------------------------------------------------- #
# next tetrimino area�N���X                                                         #
# ----------------------------------------------------------------------------- #
# ���̃e�g���~�m�\����ʗ̈�̍쐬(�u���b�N�̍��W��ݒ肷��N���X(TetrisSquare�N���X)�Ə����͓���)
class NextTetriminoArea:

    def __init__(self, x=0, y=0, color=TETRIS_BACK_GROUND_COLOR):
        print(f"[NEXT_TETRIMINO_AREA]next_tetrimino_area init")
        # 1�̐����`���쐬
        self.x = x
        self.y = y
        self.color = color

    def set_cord(self, x, y):
        # �����`�̍��W��ݒ�
        self.x = x
        self.y = y

    def get_cord(self):
        # �����`�̍��W���擾
        return int(self.x), int(self.y)

    def set_color(self, color):
        # �����`�̐F��ݒ�
        self.color = color

    def get_color(self):
        # �����`�̐F���擾
        return self.color


