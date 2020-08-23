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
# display tetris canvasクラス                                                    #
# ----------------------------------------------------------------------------- #
# テトリス画面を描画するクラス
class TetrisCanvas(tk.Canvas):

    # Tetrisクラスのインスタンス作成
    def __init__(self, app, field):
        print("[DISPLAY]tetris_canvas init")
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


# ----------------------------------------------------------------------------- #
# display tetris squareクラス                                                                      #
# ----------------------------------------------------------------------------- #
# ブロックの座標を設定するクラス
class TetrisSquare:

    def __init__(self, x=0, y=0, color=TETRIS_BACK_GROUND_COLOR):
        print(f"[DISPLAY]tetris_square init x={x} y={y}")
        # 1つの正方形を作成
        self.x = x
        self.y = y
        self.color = color

    def set_cord(self, x, y):
        # 正方形の座標を設定
        self.x = x
        self.y = y

    def get_cord(self):
        # 正方形の座標を取得
        return int(self.x), int(self.y)

    def set_color(self, color):
        # 正方形の色を設定
        self.color = color

    def get_color(self):
        # 正方形の色を取得
        return self.color

    # 移動後の正方形の座標を取得
    def get_moved_cord(self, direction):
        # 移動前の正方形の座標を取得
        x, y = self.get_cord()

        # 移動方向を考慮して移動後の座標を計算
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
# display tetris fieldクラス                                                     #
# ----------------------------------------------------------------------------- #
# テトリス画面のフィールド
class TetrisField:

    def __init__(self):
        print("[DISPLAY]tetris_field init")
        self.width = TETRIS_FIELD_WIDTH
        self.height = TETRIS_FIELD_HEIGHT

        # フィールドを初期化
        self.squares = []
        for y in range(self.height):
            for x in range(self.width):
                # フィールドを正方形インスタンスのリストとして管理
                self.squares.append(TetrisSquare(x, y, TETRIS_BACK_GROUND_COLOR))

    def get_width(self):
        # フィールドの正方形の数（横方向）を取得
        return self.width

    def get_height(self):
        # フィールドの正方形の数（縦方向）を取得
        return self.height

    def get_squares(self):
        # フィールドを構成する正方形のリストを取得
        return self.squares

    def get_square(self, x, y):
        # 指定した座標の正方形を取得
        return self.squares[y * self.width + x]


# ----------------------------------------------------------------------------- #
# display next tetrimino canvasクラス                                            #
# ----------------------------------------------------------------------------- #
# 次のテトリミノ表示画面を描画するクラス
class NextTetriminoCanvas(tk.Canvas):

    def __init__(self, app, field):
        print("[DISPLAY]next_tetrimino_canvas init")
        # 次のテトリミノを描画するキャンバスを作成
        next_tetrimino_canvas_width = field.get_width()
        next_tetrimino_canvas_height = field.get_height()

        # tk.Canvasクラスのinit
        super().__init__(app, width=next_tetrimino_canvas_width,
                         height=next_tetrimino_canvas_height,
                         bg=NEXT_TETRIMINO_BACK_GROUND_COLOR)

        # キャンバスを画面上に設置
        next_label_font = font.Font(size=NEXT_LABEL_SIZE, weight='bold')
        next_label = tk.Label(app, text=NEXT_LABEL, font=next_label_font, bg=BACK_GROUND_COLOR)
        next_label.place(x=NEXT_LABEL_X, y=NEXT_LABEL_Y)
        self.place(x=NEXT_TETRIMINO_CANVAS_X, y=NEXT_TETRIMINO_CANVAS_Y)


# ----------------------------------------------------------------------------- #
# display next tetris squareクラス                                               #
# ----------------------------------------------------------------------------- #
# 次のテトリミノ表示画面領域の作成
class NextTetrisArea:

    def __init__(self, x=0, y=0, color=TETRIS_BACK_GROUND_COLOR):
        print(f"[DISPLAY]next_tetris_square init")
        # 1つの正方形を作成
        self.x = x
        self.y = y
        self.color = color

    def set_cord(self, x, y):
        # 正方形の座標を設定
        self.x = x
        self.y = y

    def get_cord(self):
        # 正方形の座標を取得
        return int(self.x), int(self.y)

    def set_color(self, color):
        # 正方形の色を設定
        self.color = color

    def get_color(self):
        # 正方形の色を取得
        return self.color


# ----------------------------------------------------------------------------- #
# display tetris fieldクラス                                                     #
# ----------------------------------------------------------------------------- #
# 次のテトリミノ表示画面のフィールド
class NextTetriminoField:

    def __init__(self):
        print("[DISPLAY]next_tetrimino_field init")
        self.width = NEXT_TETRIMINO_FIELD_WIDTH
        self.height = NEXT_TETRIMINO_FIELD_HEIGHT

        self.square = NextTetrisArea(self.width, self.height, NEXT_TETRIMINO_BACK_GROUND_COLOR)

    def get_width(self):
        # フィールドの正方形の数（横方向）を取得
        return self.width

    def get_height(self):
        # フィールドの正方形の数（縦方向）を取得
        return self.height


# ----------------------------------------------------------------------------- #
# display mainクラス                                                             #
# ----------------------------------------------------------------------------- #
class DisplayMain:

    def __init__(self, app):
        print("[DISPLAY]display init")
        # テトリスインスタンスの生成
        app.title(TITLE)
        app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        app.configure(bg=BACK_GROUND_COLOR)

        # ブロックの管理リストを初期化
        self.tetris_field = TetrisField()

        # 次のテトリミノ管理を初期化
        self.next_tetrimino_field = NextTetriminoField()

        # 落下ブロックをセット
        self.block = None

        # テトリス画面をセット
        self.canvas = TetrisCanvas(app, self.tetris_field)

        # 次のテトリミノ表示画面をセット
        self.canvas = NextTetriminoCanvas(app, self.next_tetrimino_field)
