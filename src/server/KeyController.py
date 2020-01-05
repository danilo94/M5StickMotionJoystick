from KeyHardwareInput import *
from time import *
from Enderecos import *
class KeyController(object):

    def __init__(self):
        sleep(5)


    def pressionar(self,tecla):

        if (tecla==0): # Andar pra frente
            self.pressKey(LEFT)
            sleep(0.15)
            self.releaseKey(LEFT)
            pass
        elif(tecla==1): # Andar para trás
            self.pressKey(RIGHT)
            sleep(0.15)
            self.releaseKey(RIGHT)
            pass

        elif(tecla==2): # Pular
            self.pressKey(JUMP)
            sleep(0.15)
            self.releaseKey(JUMP)
            pass
        elif(tecla==6):
            self.pressKey(CARREGARSAVESTATE)
            sleep(0.1)
            self.releaseKey(CARREGARSAVESTATE)



    def pressKey(self,hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def releaseKey(self,hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0,
                            ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
