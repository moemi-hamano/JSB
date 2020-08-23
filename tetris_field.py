#!/usr/bin/env python
# -*- coding:Shift-JIS -*-
from tetris_square import TetrisSquare
from const import TETRIS_FIELD_WIDTH
from const import TETRIS_FIELD_HEIGHT
from const import TETRIS_BACK_GROUND_COLOR


# ----------------------------------------------------------------------------- #
# tetris field�N���X      �@�@�@�@�@                                               #
# ----------------------------------------------------------------------------- #
# �e�g���X��ʂ̃t�B�[���h
class TetrisField:

    def __init__(self):
        print("[TETRIS_FIELD]tetris_field init")
        self.width = TETRIS_FIELD_WIDTH
        self.height = TETRIS_FIELD_HEIGHT

        # �t�B�[���h��������
        self.squares = []
        for y in range(self.height):
            for x in range(self.width):
                # �t�B�[���h�𐳕��`�C���X�^���X�̃��X�g�Ƃ��ĊǗ�
                self.squares.append(TetrisSquare(x, y, TETRIS_BACK_GROUND_COLOR))

    def get_width(self):
        # �t�B�[���h�̐����`�̐��i�������j���擾
        return self.width

    def get_height(self):
        # �t�B�[���h�̐����`�̐��i�c�����j���擾
        return self.height

    def get_squares(self):
        # �t�B�[���h���\�����鐳���`�̃��X�g���擾
        return self.squares

    def get_square(self, x, y):
        # �w�肵�����W�̐����`���擾
        return self.squares[y * self.width + x]

    # �Q�[���I�[�o�[���ǂ����𔻒f
    def judge_game_over(self, block):

        # �t�B�[���h��Ŋ��ɖ��܂��Ă�����W�̏W���쐬
        no_empty_cord = set(square.get_cord() for square
                            in self.get_squares() if square.get_color() != TETRIS_BACK_GROUND_COLOR)

        # �u���b�N��������W�̏W���쐬
        block_cord = set(square.get_cord() for square
                         in block.get_squares())

        # �u���b�N�̍��W�̏W����
        # �t�B�[���h�̊��ɖ��܂��Ă�����W�̏W���̐ϏW�����쐬
        collision_set = no_empty_cord & block_cord

        # �ϏW������ł���΃Q�[���I�[�o�[�ł͂Ȃ�
        if len(collision_set) == 0:
            ret = False
        else:
            ret = True

        return ret

    # �w�肵�������Ƀu���b�N���ړ��ł��邩�𔻒f
    def judge_can_move(self, block, direction):

        # �t�B�[���h��Ŋ��ɖ��܂��Ă�����W�̏W���쐬
        no_empty_cord = set(square.get_cord() for square
                            in self.get_squares() if square.get_color() != TETRIS_BACK_GROUND_COLOR)

        # �ړ���̃u���b�N��������W�̏W���쐬
        move_block_cord = set(square.get_moved_cord(direction) for square
                              in block.get_squares())

        # �t�B�[���h����͂ݏo�����ǂ����𔻒f
        for x, y in move_block_cord:

            # �͂ݏo���ꍇ�͈ړ��ł��Ȃ�
            if x < 0 or x >= self.width or \
                    y < 0 or y >= self.height:
                return False

        # �ړ���̃u���b�N�̍��W�̏W����
        # �t�B�[���h�̊��ɖ��܂��Ă�����W�̏W���̐ϏW�����쐬
        collision_set = no_empty_cord & move_block_cord

        # �ϏW������Ȃ�ړ��\
        if len(collision_set) == 0:
            move_pos_ret = True
        else:
            move_pos_ret = False

        return move_pos_ret
