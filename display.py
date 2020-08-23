#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
import tkinter as tk
from tkinter import font
from const import KEY_LEFT
from const import KEY_RIGHT
from const import KEY_DOWN
from const import KEY_UP
from const import TITLE
from const import NEXT_LABEL
from const import WINDOW_WIDTH
from const import WINDOW_HEIGHT
from const import BACK_GROUND_COLOR
from const import BLOCK_SIZE
from const import TETRIS_FIELD_WIDTH
from const import TETRIS_FIELD_HEIGHT
from const import NEXT_TETRIMINO_FIELD_WIDTH
from const import NEXT_TETRIMINO_FIELD_HEIGHT
from const import TETRIS_BACK_GROUND_COLOR
from const import TETRIS_OUTLINE_COLOR
from const import NEXT_TETRIMINO_BACK_GROUND_COLOR
from const import TETRIS_CANVAS_X
from const import TETRIS_CANVAS_Y
from const import NEXT_LABEL_SIZE
from const import NEXT_LABEL_X
from const import NEXT_LABEL_Y
from const import NEXT_TETRIMINO_CANVAS_X
from const import NEXT_TETRIMINO_CANVAS_Y


# ----------------------------------------------------------------------------- #
# display tetris canvas�N���X                                                    #
# ----------------------------------------------------------------------------- #
# �e�g���X��ʂ�`�悷��N���X
class TetrisCanvas(tk.Canvas):

    # Tetris�N���X�̃C���X�^���X�쐬
    def __init__(self, app, field):
        print("[DISPLAY]tetris_canvas init")
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


# ----------------------------------------------------------------------------- #
# display tetris square�N���X                                                                      #
# ----------------------------------------------------------------------------- #
# �u���b�N�̍��W��ݒ肷��N���X
class TetrisSquare:

    def __init__(self, x=0, y=0, color=TETRIS_BACK_GROUND_COLOR):
        print(f"[DISPLAY]tetris_square init x={x} y={y}")
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


# ----------------------------------------------------------------------------- #
# display tetris field�N���X                                                     #
# ----------------------------------------------------------------------------- #
# �e�g���X��ʂ̃t�B�[���h
class TetrisField:

    def __init__(self):
        print("[DISPLAY]tetris_field init")
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


# ----------------------------------------------------------------------------- #
# display next tetrimino canvas�N���X                                            #
# ----------------------------------------------------------------------------- #
# ���̃e�g���~�m�\����ʂ�`�悷��N���X
class NextTetriminoCanvas(tk.Canvas):

    def __init__(self, app, field):
        print("[DISPLAY]next_tetrimino_canvas init")
        # ���̃e�g���~�m��`�悷��L�����o�X���쐬
        next_tetrimino_canvas_width = field.get_width()
        next_tetrimino_canvas_height = field.get_height()

        # tk.Canvas�N���X��init
        super().__init__(app, width=next_tetrimino_canvas_width,
                         height=next_tetrimino_canvas_height,
                         bg=NEXT_TETRIMINO_BACK_GROUND_COLOR)

        # �L�����o�X����ʏ�ɐݒu
        next_label_font = font.Font(size=NEXT_LABEL_SIZE, weight='bold')
        next_label = tk.Label(app, text=NEXT_LABEL, font=next_label_font, bg=BACK_GROUND_COLOR)
        next_label.place(x=NEXT_LABEL_X, y=NEXT_LABEL_Y)
        self.place(x=NEXT_TETRIMINO_CANVAS_X, y=NEXT_TETRIMINO_CANVAS_Y)


# ----------------------------------------------------------------------------- #
# display next tetris square�N���X                                               #
# ----------------------------------------------------------------------------- #
# ���̃e�g���~�m�\����ʗ̈�̍쐬
class NextTetrisArea:

    def __init__(self, x=0, y=0, color=TETRIS_BACK_GROUND_COLOR):
        print(f"[DISPLAY]next_tetris_square init")
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


# ----------------------------------------------------------------------------- #
# display tetris field�N���X                                                     #
# ----------------------------------------------------------------------------- #
# ���̃e�g���~�m�\����ʂ̃t�B�[���h
class NextTetriminoField:

    def __init__(self):
        print("[DISPLAY]next_tetrimino_field init")
        self.width = NEXT_TETRIMINO_FIELD_WIDTH
        self.height = NEXT_TETRIMINO_FIELD_HEIGHT

        self.square = NextTetrisArea(self.width, self.height, NEXT_TETRIMINO_BACK_GROUND_COLOR)

    def get_width(self):
        # �t�B�[���h�̐����`�̐��i�������j���擾
        return self.width

    def get_height(self):
        # �t�B�[���h�̐����`�̐��i�c�����j���擾
        return self.height


# ----------------------------------------------------------------------------- #
# display main�N���X                                                             #
# ----------------------------------------------------------------------------- #
class DisplayMain:

    def __init__(self, app):
        print("[DISPLAY]display init")
        # �e�g���X�C���X�^���X�̐���
        app.title(TITLE)
        app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        app.configure(bg=BACK_GROUND_COLOR)

        # �u���b�N�̊Ǘ����X�g��������
        self.tetris_field = TetrisField()

        # ���̃e�g���~�m�Ǘ���������
        self.next_tetrimino_field = NextTetriminoField()

        # �����u���b�N���Z�b�g
        self.block = None

        # �e�g���X��ʂ��Z�b�g
        self.canvas = TetrisCanvas(app, self.tetris_field)

        # ���̃e�g���~�m�\����ʂ��Z�b�g
        self.canvas = NextTetriminoCanvas(app, self.next_tetrimino_field)
