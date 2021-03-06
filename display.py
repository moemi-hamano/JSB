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
# display mainクラス                                                             #
# ----------------------------------------------------------------------------- #
class DisplayMain:

    def __init__(self, app, tetris_field):
        print("[DISPLAY]display init")
        # テトリスインスタンスの生成
        app.title(TITLE)
        app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        app.configure(bg=BACK_GROUND_COLOR)

        # 次のテトリミノ管理を初期化
        self.next_tetrimino_field = NextTetriminoField()

        # テトリス画面をセット
        self.canvas = TetrisCanvas(app, tetris_field)

        # 次のテトリミノ表示画面をセット
        self.next_canvas = NextTetriminoCanvas(app, self.next_tetrimino_field)
