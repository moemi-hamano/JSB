#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from next_tetrimino_area import NextTetriminoArea
from const import NEXT_TETRIMINO_FIELD_WIDTH
from const import NEXT_TETRIMINO_FIELD_HEIGHT
from const import NEXT_TETRIMINO_BACK_GROUND_COLOR


# ----------------------------------------------------------------------------- #
# next tetrimino field�N���X                                                             #
# ----------------------------------------------------------------------------- #
# ���̃e�g���~�m�\����ʂ̃t�B�[���h
class NextTetriminoField:

    def __init__(self):
        print("[NEXT_TETRIMINO_FIELD]next_tetrimino_field init")
        self.width = NEXT_TETRIMINO_FIELD_WIDTH
        self.height = NEXT_TETRIMINO_FIELD_HEIGHT

        self.square = NextTetriminoArea(self.width, self.height, NEXT_TETRIMINO_BACK_GROUND_COLOR)

    def get_width(self):
        # �t�B�[���h�̐����`�̐��i�������j���擾
        return self.width

    def get_height(self):
        # �t�B�[���h�̐����`�̐��i�c�����j���擾
        return self.height
