#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from tetris_square import TetrisSquare
from const import TETRIS_FIELD_WIDTH
from const import TETRIS_FIELD_HEIGHT
from const import TETRIS_BACK_GROUND_COLOR


# ----------------------------------------------------------------------------- #
# tetris field�N���X      �@�@�@�@�@                                               #
# ----------------------------------------------------------------------------- #
# �e�g���X��ʂ̃t�B�[���h
class TetrisField:

    def __init__(self):
        print("[TETRIS_FIELD]tetris_field init")
        self.width = TETRIS_FIELD_WIDTH
        self.height = TETRIS_FIELD_HEIGHT

        # �t�B�[���h��������
        self.squares = []
        for y in range(self.height):
            for x in range(self.width):
                # �t�B�[���h�𐳕��`�C���X�^���X�̃��X�g�Ƃ��ĊǗ�
                self.squares.append(TetrisSquare(x, y, TETRIS_BACK_GROUND_COLOR))

    def get_width(self):
        # �t�B�[���h�̐����`�̐��i�������j���擾
        return self.width

    def get_height(self):
        # �t�B�[���h�̐����`�̐��i�c�����j���擾
        return self.height

    def get_squares(self):
        # �t�B�[���h���\�����鐳���`�̃��X�g���擾
        return self.squares

    def get_square(self, x, y):
        # �w�肵�����W�̐����`���擾
        return self.squares[y * self.width + x]
