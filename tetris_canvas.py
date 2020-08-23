#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
import tkinter as tk
from tetris_field import TetrisField
from const import BLOCK_SIZE
from const import TETRIS_OUTLINE_COLOR
from const import TETRIS_CANVAS_X
from const import TETRIS_CANVAS_Y


# ----------------------------------------------------------------------------- #
# tetris canvas�N���X                                                    #
# ----------------------------------------------------------------------------- #
# �e�g���X��ʂ�`�悷��N���X
class TetrisCanvas(tk.Canvas):

    # Tetris�N���X�̃C���X�^���X�쐬
    def __init__(self, app, field):
        print("[TETRIS_CANVAS]tetris_canvas init")
        # �e�g���X��`�悷��L�����p�X���쐬
        canvas_width = field.get_width() * BLOCK_SIZE
        canvas_height = field.get_height() * BLOCK_SIZE
        # tk.Canvas�N���X��init
        super().__init__(app, width=canvas_width, height=canvas_height, bg=TETRIS_OUTLINE_COLOR)

        # �L�����o�X����ʏ�ɐݒu
        self.place(x=TETRIS_CANVAS_X, y=TETRIS_CANVAS_Y)

        # 10x20�̐����`��`�悷�邱�ƂŃe�g���X��ʂ��쐬
        for y in range(field.get_height()):
            for x in range(field.get_width()):
                square = field.get_square(x, y)
                x1 = x * BLOCK_SIZE
                x2 = (x + 1) * BLOCK_SIZE
                y1 = y * BLOCK_SIZE
                y2 = (y + 1) * BLOCK_SIZE
                self.create_rectangle(
                    x1, y1, x2, y2,
                    outline=TETRIS_OUTLINE_COLOR, width=1,
                    fill=square.get_color()
                )

        # ��O�ɕ`�悵���t�B�[������ݒ�
        self.before_field = field

    # �e�g���X��ʂ̍X�V
    def update(self, field, block):

        # �`��p�t�B�[���h�쐬
        new_field = TetrisField()
        for y in range(field.get_height()):
            for x in range(field.get_width()):
                square = field.get_square(x, y)
                color = square.get_color()

                new_square = new_field.get_square(x, y)
                new_square.set_color(color)

        # �t�B�[���h�Ƀu���b�N�̐����`�������킹��
        if block is not None:
            block_squares = block.get_squares()
            for block_square in block_squares:
                # �u���b�N�̐����`���W�ƐF���擾
                x, y = block_square.get_cord()
                color = block_square.get_color()

                # �擾�������W�̐����`�̐F���X�V
                new_field_square = new_field.get_square(x, y)
                new_field_square.set_color(color)

        # �`��p�̃t�B�[���h�ŃL�����o�X�ɕ`��
        for y in range(field.get_height()):
            for x in range(field.get_width()):

                # (x,y)���W�̃t�B�[���h�̐F���擾
                new_square = new_field.get_square(x, y)
                new_color = new_square.get_color()

                # (x,y)���W�ɕω����Ȃ��ꍇ�͕`�悵�Ȃ�
                before_square = self.before_field.get_square(x, y)
                before_color = before_square.get_color()
                if new_color == before_color:
                    continue

                x1 = x * BLOCK_SIZE
                x2 = (x + 1) * BLOCK_SIZE
                y1 = y * BLOCK_SIZE
                y2 = (y + 1) * BLOCK_SIZE

                # �t�B�[���h�̊e�ʒu�̐F�Œ����`��`��
                self.create_rectangle(
                    x1, y1, x2, y2,
                    outline="gray", width=1,
                    fill=new_color
                )
        # �O��`�悵���t�B�[���h�̏����X�V
        self.before_field = new_field
