#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from const import TETRIS_BACK_GROUND_COLOR
from const import KEY_LEFT
from const import KEY_RIGHT
from const import KEY_UP


# ----------------------------------------------------------------------------- #
# tetris square�N���X                                                                      #
# ----------------------------------------------------------------------------- #
# �u���b�N�̍��W��ݒ肷��N���X
class TetrisSquare:

    def __init__(self, x=0, y=0, color=TETRIS_BACK_GROUND_COLOR):
        print(f"[TETRIS_SQUARE]tetris_square init x={x} y={y}")
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

    # �ړ���̐����`�̍��W���擾
    def get_moved_cord(self, direction):
        # �ړ��O�̐����`�̍��W���擾
        x, y = self.get_cord()

        # �ړ��������l�����Ĉړ���̍��W���v�Z
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
