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
# tetris block�N���X                                                                  #
# ----------------------------------------------------------------------------- #
# �e�g���X�̃u���b�N���쐬����N���X
class TetrisBlock:

    def __init__(self):
        print("[TETRIS_BLOCK]tetris_block init")
        # �u���b�N���\�����郊�X�g
        self.squares = []
        color = None
        cords = None

        # �u���b�N�̌`�������_���Ɍ���
        # TODO kashida to �_�삳�� �e�X�g�p��block_type��1�ŌŒ肳���Ă��܂��B�K�X�폜���āA�����w��ɏC�����Ă��������B
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

        # ���肵���F�ƍ��W�̐����`���쐬���ă��X�g�ɒǉ�
        for cord in cords:
            self.squares.append(TetrisSquare(cord[0], cord[1], color))

    # �u���b�N���\�����鐳���`���擾
    def get_squares(self):

        return self.squares

    # �u���b�N���ړ�
    def move(self, direction):

        # �u���b�N���\�����鐳���`���ړ�
        for square in self.squares:
            x, y = square.get_moved_cord(direction)
            square.set_cord(x, y)
