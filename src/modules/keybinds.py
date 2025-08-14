import pygame as __game_source__

key_source = __game_source__

class Key:
    key_0 = 48
    key_1 = 49
    key_2 = 50
    key_3 = 51
    key_4 = 52
    key_5 = 53
    key_6 = 54
    key_7 = 55
    key_8 = 56
    key_9 = 57
    key_AMPERSAND = 38
    key_ASTERISK = 42
    key_AT = 64
    key_BACKQUOTE = 96
    key_BACKSLASH = 92
    key_BACKSPACE = 8
    key_CAPSLOCK = 1073741881
    key_CARET = 94
    key_COLON = 58
    key_COMMA = 44
    key_DELETE = 127
    key_DOLLAR = 36
    key_DOWN = 1073741905
    key_END = 1073741901
    key_EQUALS = 61
    key_ESCAPE = 27
    key_EXCLAIM = 33
    key_F1 = 1073741882
    key_F2 = 1073741883
    key_F3 = 1073741884
    key_F4 = 1073741885
    key_F5 = 1073741886
    key_F6 = 1073741887
    key_F7 = 1073741888
    key_F8 = 1073741889
    key_F9 = 1073741890
    key_F10 = 1073741891
    key_F11 = 1073741892
    key_F12 = 1073741893
    key_GREATER = 62
    key_HASH = 35
    key_HELP = 1073741941
    key_HOME = 1073741898
    key_INSERT = 1073741897
    key_KP_0 = 1073741922
    key_KP_1 = 1073741913
    key_KP_2 = 1073741914
    key_KP_3 = 1073741915
    key_KP_4 = 1073741916
    key_KP_5 = 1073741917
    key_KP_6 = 1073741918
    key_KP_7 = 1073741919
    key_KP_8 = 1073741920
    key_KP_9 = 1073741921
    key_KP_DIVIDE = 1073741908
    key_KP_ENTER = 1073741912
    key_KP_EQUALS = 1073741927
    key_KP_MINUS = 1073741910
    key_KP_MULTIPLY = 1073741909
    key_KP_PERIOD = 1073741923
    key_KP_PLUS = 1073741911
    key_LALT = 1073742050
    key_LCTRL = 1073742048
    key_LEFT = 1073741904
    key_LEFTBRACKET = 91
    key_LEFTPAREN = 40
    key_LESS = 60
    key_LSHIFT = 1073742049
    key_MENU = 1073741942
    key_MINUS = 45
    key_NUMLOCK = 1073741907
    key_PAGEDOWN = 1073741902
    key_PAGEUP = 1073741899
    key_PAUSE = 1073741896
    key_PERCENT = 37
    key_PERIOD = 46
    key_PLUS = 43
    key_PRINTSCREEN = 1073741894
    key_QUESTION = 63
    key_QUOTE = 39
    key_QUOTEDBL = 34
    key_RALT = 1073742054
    key_RCTRL = 1073742052
    key_RETURN = 13
    key_RIGHT = 1073741903
    key_RIGHTBRACKET = 93
    key_RIGHTPAREN = 41
    key_RSHIFT = 1073742053
    key_SCROLLLOCK = 1073741895
    key_SEMICOLON = 59
    key_SLASH = 47
    key_SPACE = 32
    key_TAB = 9
    key_UNDERSCORE = 95
    key_UP = 1073741906
    key_a = 97
    key_b = 98
    key_c = 99
    key_d = 100
    key_e = 101
    key_f = 102
    key_g = 103
    key_h = 104
    key_i = 105
    key_j = 106
    key_k = 107
    key_l = 108
    key_m = 109
    key_n = 110
    key_o = 111
    key_p = 112
    key_q = 113
    key_r = 114
    key_s = 115
    key_t = 116
    key_u = 117
    key_v = 118
    key_w = 119
    key_x = 120
    key_y = 121
    key_z = 122


class Keyboard:
    @staticmethod
    def is_pressed(*keys: int) -> bool|None:
        """
        Checks if a key is pressed.
        """
        for i in keys:
            if key_source.key.get_pressed()[i]:
                return True
        else:
            return False
    

class Mouse:
    x:int
    y:int
    @classmethod
    def update(cls) -> None:
        cls.x, cls.y = key_source.mouse.get_pos()
        
    @staticmethod
    def isclicked(mouse_button:int) -> bool:
        match mouse_button:
            case 1:
                return key_source.mouse.get_pressed()[0]
            case 2:
                return key_source.mouse.get_pressed()[1]
            case 3:
                return key_source.mouse.get_pressed()[2]
            case _:
                raise ValueError("Invalid mouse button detected.")
  