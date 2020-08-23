#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
import tkinter as tk
from tetris_field import TetrisField
from const import BLOCK_SIZE
from const import TETRIS_OUTLINE_COLOR
from const import TETRIS_CANVAS_X
from const import TETRIS_CANVAS_Y


# ----------------------------------------------------------------------------- #
# tetris canvasクラス                                                    #
# ----------------------------------------------------------------------------- #
# テトリス画面を描画するクラス
class TetrisCanvas(tk.Canvas):

    # Tetrisクラスのインスタンス作成
    def __init__(self, app, field):
        print("[TETRIS_CANVAS]tetris_canvas init")
        # テトリスを描画するキャンパスを作成
        canvas_width = field.get_width() * BLOCK_SIZE
        canvas_height = field.get_height() * BLOCK_SIZE
        # tk.Canvasクラスのinit
        super().__init__(app, width=canvas_width, height=canvas_height, bg=TETRIS_OUTLINE_COLOR)

        # キャンバスを画面上に設置
        self.place(x=TETRIS_CANVAS_X, y=TETRIS_CANVAS_Y)

        # 10x20個の正方形を描画することでテトリス画面を作成
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

        # 一つ前に描画したフィール尾を設定
        self.before_field = field

    # テトリス画面の更新
    def update(self, field, block):

        # 描画用フィールド作成
        new_field = TetrisField()
        for y in range(field.get_height()):
            for x in range(field.get_width()):
                square = field.get_square(x, y)
                color = square.get_color()

                new_square = new_field.get_square(x, y)
                new_square.set_color(color)

        # フィールドにブロックの正方形情報を合わせる
        if block is not None:
            block_squares = block.get_squares()
            for block_square in block_squares:
                # ブロックの正方形座標と色を取得
                x, y = block_square.get_cord()
                color = block_square.get_color()

                # 取得した座標の正方形の色を更新
                new_field_square = new_field.get_square(x, y)
                new_field_square.set_color(color)

        # 描画用のフィールドでキャンバスに描画
        for y in range(field.get_height()):
            for x in range(field.get_width()):

                # (x,y)座標のフィールドの色を取得
                new_square = new_field.get_square(x, y)
                new_color = new_square.get_color()

                # (x,y)座標に変化がない場合は描画しない
                before_square = self.before_field.get_square(x, y)
                before_color = before_square.get_color()
                if new_color == before_color:
                    continue

                x1 = x * BLOCK_SIZE
                x2 = (x + 1) * BLOCK_SIZE
                y1 = y * BLOCK_SIZE
                y2 = (y + 1) * BLOCK_SIZE

                # フィールドの各位置の色で長方形を描画
                self.create_rectangle(
                    x1, y1, x2, y2,
                    outline="gray", width=1,
                    fill=new_color
                )
        # 前回描画したフィールドの情報を更新
        self.before_field = new_field
