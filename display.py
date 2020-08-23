#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from tetris_canvas import TetrisCanvas
from next_tetrimino_canvas import NextTetriminoCanvas
from next_tetrimino_field import NextTetriminoField
from const import BACK_GROUND_COLOR
from const import TITLE
from const import WINDOW_HEIGHT
from const import WINDOW_WIDTH


# ----------------------------------------------------------------------------- #
# display main�N���X                                                             #
# ----------------------------------------------------------------------------- #
class DisplayMain:

    def __init__(self, app, tetris_field):
        print("[DISPLAY]display init")
        # �e�g���X�C���X�^���X�̐���
        app.title(TITLE)
        app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        app.configure(bg=BACK_GROUND_COLOR)

        # ���̃e�g���~�m�Ǘ���������
        self.next_tetrimino_field = NextTetriminoField()

        # �����u���b�N���Z�b�g
        self.block = None

        # �e�g���X��ʂ��Z�b�g
        self.canvas = TetrisCanvas(app, tetris_field)

        # ���̃e�g���~�m�\����ʂ��Z�b�g
        self.canvas = NextTetriminoCanvas(app, self.next_tetrimino_field)
