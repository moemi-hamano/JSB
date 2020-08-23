#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
import tkinter as tk
from key import KeyMain
from timer import TimerMain
from tetris_field import TetrisField
from display import DisplayMain
from main_exit import main_exit_routine
from const import KEY_LEFT
from const import KEY_RIGHT
from const import KEY_DOWN
from const import KEY_UP
from const import KEY_ESC


# ----------------------------------------------------------------------------- #
# manager�N���X                                                                    #
# ----------------------------------------------------------------------------- #
class ManagerMain:

    # Manager�N���X�̃C���X�^���X�쐬
    def __init__(self):
        print("[MNG]manager init")
        # �A�v��(tkinter)�C���X�^���X����
        self.app = tk.Tk()
        # �L�[�C���X�^���X����
        self.key = KeyMain(self, self.app)
        # �^�C�}�C���X�^���X����
        self.timer = TimerMain(self, self.app)
        # �u���b�N�̊Ǘ����X�g��������
        self.tetris_field = TetrisField()
        # �f�B�X�v���C�C���X�^���X����
        self.display = DisplayMain(self.app, self.tetris_field)

    # �Q�[���J�n
    def start_event(self):
        # �^�C�}�J�n
        self.timer.timer_start()

    # �e�g���~�m�ړ�
    def tetrimino_move(self, key):
        print("[MNG]tetrimino_move", key)

    # �e�g���~�m����
    def tetrimino_drop(self):
        print("[MNG]tetrimino_drop")

    # �L�[���������ꂽ���̃C�x���g
    def receive_key_down_event(self, key):
        print("[MNG]receive_key_down_event", key)
        if key == KEY_LEFT or key == KEY_RIGHT or key == KEY_DOWN:
            self.tetrimino_move(key)
        if key == KEY_UP:
            self.tetrimino_drop()
        if key == KEY_ESC:
            main_exit_routine()

    # �^�C�}�����C�x���g
    def timer_expired_event(self):
        print("[MNG]timer expired")
        # TODO kashida to �S���̕� �^�C�}�������ɂȂ������̏���
        # �^�C�}���ăX�^�[�g
        self.timer.timer_start()
