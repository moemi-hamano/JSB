#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from const import TIMER_FALLING_SPEED
import datetime


# ----------------------------------------------------------------------------- #
# timer�N���X                                                                    #
# ----------------------------------------------------------------------------- #
class TimerMain:

    # timer�N���X�̃C���X�^���X����
    def __init__(self, mng, app):
        print("[TIMER]timer init")
        self.timer = None
        self.mng = mng
        self.app = app

    # �^�C�}�J�n
    def timer_start(self):
        print("[TIMER]timer start")
        if self.timer is not None:
            # �^�C�}����U�L�����Z��
            self.app.after_cancel(self.timer)

        self.timer = self.app.after(TIMER_FALLING_SPEED, self.time_passed_event)

    # �^�C�}�I��
    def timer_end(self):
        print("[TIMER]timer end")
        if self.timer is not None:
            self.app.after_cancel(self.timer)
            self.timer = None

    # �^�C�}����
    def time_passed_event(self):
        # TODO kashida to somebody �ȉ���datetime�̓f�o�b�O�p�ɋL�q�����B�s�v�ȏꍇ�̓J�b�R���̋L�q�ƃt�@�C���㕔��import���폜����B
        print(f"[TIMER]{TIMER_FALLING_SPEED} ms passed ({datetime.datetime.now()})")
        self.mng.timer_expired_event()
