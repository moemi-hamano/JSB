#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
import tkinter as tk
from tkinter import font
from const import NEXT_LABEL
from const import BACK_GROUND_COLOR
from const import NEXT_TETRIMINO_BACK_GROUND_COLOR
from const import NEXT_LABEL_SIZE
from const import NEXT_LABEL_X
from const import NEXT_LABEL_Y
from const import NEXT_TETRIMINO_CANVAS_X
from const import NEXT_TETRIMINO_CANVAS_Y



# ----------------------------------------------------------------------------- #
# next tetrimino canvas�N���X                                            #
# ----------------------------------------------------------------------------- #
# ���̃e�g���~�m�\����ʂ�`�悷��N���X
class NextTetriminoCanvas(tk.Canvas):

    def __init__(self, app, field):
        print("[NEXT_TETRIMINO_CANVAS]next_tetrimino_canvas init")
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


