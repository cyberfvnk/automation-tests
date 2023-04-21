from random import random

import pyautogui as gui

img_enviar = "pyautogui_bot/files/img/botao_enviar.png"
img_email = "pyautogui_bot/files/img/email.png"
img_fem = "pyautogui_bot/files/img/feminino.png"
img_mas = "pyautogui_bot/files/img/masculino.png"
img_nome = "pyautogui_bot/files/img/nome.png"
img_sex = "pyautogui_bot/files/img/sexo.png"
img_tel = "pyautogui_bot/files/img/telefone.png"


def localiza():
    return {"enviar": gui.locateCenterOnScreen(img_enviar, confidence=0.8),
            "email": gui.locateCenterOnScreen(img_email, confidence=0.8),
            "nome": gui.locateCenterOnScreen(img_nome, confidence=0.8),
            "sex": gui.locateCenterOnScreen(img_sex, confidence=0.8),
            "tel": gui.locateCenterOnScreen(img_tel, confidence=0.8)
            }


def preenche(coord, info):
    gui.moveTo(coord, duration=random())
    gui.PAUSE = random()
    gui.click()
    gui.PAUSE = random()
    gui.typewrite(info, interval=random() / 1000)
    gui.PAUSE = random()


def seleciona_sexo(coord_box, sex):
    gui.moveTo(coord_box, duration=random())
    gui.PAUSE = random()
    gui.click()
    gui.PAUSE = random()
    coord_sex = {"fem": gui.locateCenterOnScreen(img_fem, grayscale=True, confidence=0.8),
                 "mas": gui.locateCenterOnScreen(img_mas, grayscale=True, confidence=0.8)}
    gui.moveTo(coord_sex.get(sex), duration=random())
    gui.PAUSE = random()
    gui.click()
    gui.PAUSE = random()


def envia(coord):
    gui.moveTo(coord, duration=random())
    gui.click()
