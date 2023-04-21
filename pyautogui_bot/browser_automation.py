import random

import pandas as pd
import pyautogui as gui
from pyautogui_bot.utils import localiza, preenche, seleciona_sexo, envia


gui.hotkey("win", "r")
gui.PAUSE = random.random()
gui.typewrite("https://www.gabrielcasemiro.com.br/atividade_pyautogui/", interval=random.random() / 1000)
gui.PAUSE = random.random()
gui.press("enter")
gui.PAUSE = 0.5
coordenadas = localiza()

membros_table = pd.read_csv("pyautogui_bot/files/membros.csv")
linhas = len(membros_table)
i = 0

while i < linhas:
    info = membros_table.iloc[i, :].values.flatten().tolist()[0].split(";")

    preenche(coordenadas.get("nome"), info[0])
    preenche(coordenadas.get("email"), info[2])
    preenche(coordenadas.get("tel"), info[3])
    seleciona_sexo(coordenadas.get("sex"), info[1][0:3].lower())
    envia(coordenadas.get("enviar"))
    gui.press('f5')

    i += 1
