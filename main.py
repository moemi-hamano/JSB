#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from manager import ManagerMain


# ----------------------------------------------------------------------------- #
# main�֐�                                                                      #
# ----------------------------------------------------------------------------- #
def main():

    # �}�l�[�W���C���X�^���X���쐬
    mng = ManagerMain()
    # �Q�[���J�n
    mng.start_event()
    # �A�v���̑ҋ@�y�уC�x���g�����ҋ@�J�n
    mng.app.mainloop()
    # �Q�[���I��
    print("mainloop end")


if __name__ == "__main__":
    main()
