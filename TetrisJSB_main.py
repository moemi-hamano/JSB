#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from TetrisJSB_manager import manager_main
from TetrisJSB_key import key_main
import tkinter as tk

# ----------------------------------------------------------------------------- #
# main関数                                                                      #
# ----------------------------------------------------------------------------- #
def main():

    app = tk.Tk()
    app.geometry("200x100")

    mng = manager_main()
    key_main(mng, app)
    app.mainloop()
    print("mainloop end")

if __name__ == "__main__":

    main()
