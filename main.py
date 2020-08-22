#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from manager import ManagerMain


# ----------------------------------------------------------------------------- #
# main関数                                                                      #
# ----------------------------------------------------------------------------- #
def main():

    # マネージャインスタンスを作成
    mng = ManagerMain()
    # ゲーム開始
    mng.start_event()
    # ゲーム終了
    print("mainloop end")


if __name__ == "__main__":
    main()
