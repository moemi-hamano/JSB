#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from const import TIMER_FALLING_SPEED
import datetime


# ----------------------------------------------------------------------------- #
# timerクラス                                                                    #
# ----------------------------------------------------------------------------- #
class TimerMain:

    # timerクラスのインスタンス生成
    def __init__(self, mng, app):
        print("[TIMER]timer init")
        self.timer = None
        self.mng = mng
        self.app = app

    # タイマ開始
    def timer_start(self):
        print("[TIMER]timer start")
        if self.timer is not None:
            # タイマを一旦キャンセル
            self.app.after_cancel(self.timer)

        self.timer = self.app.after(TIMER_FALLING_SPEED, self.time_passed_event)

    # タイマ終了
    def timer_end(self):
        print("[TIMER]timer end")
        if self.timer is not None:
            self.app.after_cancel(self.timer)
            self.timer = None

    # タイマ満了
    def time_passed_event(self):
        # TODO kashida to somebody 以下のdatetimeはデバッグ用に記述した。不要な場合はカッコ内の記述とファイル上部のimportを削除する。
        print(f"[TIMER]{TIMER_FALLING_SPEED} ms passed ({datetime.datetime.now()})")
        self.mng.timer_expired_event()
