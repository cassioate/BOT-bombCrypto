import pyautogui
import time

pyautogui.PAUSE = 2

def conectarFunc():
    pyautogui.keyDown("ctrl")
    pyautogui.press("f5")
    pyautogui.keyUp("ctrl")
    pyautogui.click(procurarImagem("ConnectWallet"), duration=3)
    pyautogui.click(procurarImagem("AssinarMetamask"), duration=3)
    pyautogui.click(procurarImagem("TreasureHunt"), duration=3)

def procurarImagem(imagem):
    contadorProcurarImagem = 0
    img = None
    confidence = 0.9
    while img == None:
        error = pyautogui.locateCenterOnScreen('./assets/Error.png', confidence=confidence)
        ok = pyautogui.locateCenterOnScreen('./assets/Ok.png', confidence=confidence)
        if error != None:
            raise Exception('Erro ao achar a imagem: ' + imagem)
        if ok != None:
            raise Exception('Erro ao achar a imagem: ' + imagem)
        print("Procurando imagem: "+ imagem)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        if contadorProcurarImagem >= 500:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    return img

def procurarImagemSemRetornarErro(imagem):
    confidence = 0.85
    if imagem == "SuperRaroXpCheioCavaleiro" or imagem == "SuperRaroXpCheioBruxa":
        confidence = 0.99
    print("Procurando imagem: "+ imagem)
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
    if img != None:
        return True
    return False

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    if procurarImagemSemRetornarErro(imagem):
        confidence = 0.9
        x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        return x, y
    else:
        return None, None

def resetarPosicaoDosBonecosNoMapa():
    print("Atualizando Bonecos")
    pyautogui.click(procurarImagem("SetaVerdeVoltandoParaOMenu"), duration=3)
    pyautogui.click(procurarImagem("TreasureHunt"), duration=3)


def descerTela1x():
    #DESCENDO TELA
    pyautogui.moveTo(x=550, y=626)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=550, y=400, duration=1.5)
    pyautogui.mouseUp(button='left')
    time.sleep(2)

def subindoTela1x():
    #SUBINDO TELA
    pyautogui.moveTo(x=550, y=380)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=550, y=626, duration=1.5)
    pyautogui.mouseUp(button='left')
    time.sleep(2)

def reiniciarBugDoBau(tempoAtual, contadorDeTempoBugDoBau, contadorResetBugDoBau, hasJustResetNow, blockReset):
    resetBugDoBau = procurarImagemSemRetornarErro("newMap")
    if resetBugDoBau == True:
        contadorResetBugDoBau += 1
    if (contadorDeTempoBugDoBau != 0 and contadorDeTempoBugDoBau % 900 == 0 and tempoAtual <= 1800):
        if contadorResetBugDoBau == 0 and hasJustResetNow == False:
            hasJustResetNow = True
            blockReset = False
            return contadorDeTempoBugDoBau, contadorResetBugDoBau, hasJustResetNow, blockReset
        else:
            if contadorDeTempoBugDoBau % 1800 == 0:
                hasJustResetNow = False
            contadorResetBugDoBau = 0
    contadorDeTempoBugDoBau += 1
    blockReset = True
    return contadorDeTempoBugDoBau, contadorResetBugDoBau, hasJustResetNow, blockReset

def goToWork():
    pyautogui.click(procurarImagem("SetaVerdeVoltandoParaOMenu"), duration=3)
    pyautogui.click(procurarImagem("Heroes"), duration=3)
    if procurarImagemSemRetornarErro("AllVerde"):
        pyautogui.click(procurarImagem("AllVerde"), duration=3)
    else:
        pyautogui.click(procurarImagem("AllLaranja"), duration=3)
        pyautogui.click(procurarImagem("AllVerde"), duration=3)
    pyautogui.click(procurarImagem("X"), duration=3)
    pyautogui.click(procurarImagem("TreasureHunt"), duration=3)

conectar = True
trabalhar = False
contadorDeTempoBugDoBau = 0
contadorResetBugDoBau = 0
hasJustResetNow = False
blockReset = True
#CONNECT
time.sleep(3)
while True:
    try:
        conectar = True
        contadorDeTempoBugDoBau = 0
        contadorResetBugDoBau = 0
        blockReset = True
        while conectar == True:
            conectarFunc()
            conectar = False
            trabalhar = True

        while trabalhar == True:
            goToWork()
            for i in range(3600):
                time.sleep(1)
                if (i < 1200):
                    contadorDeTempoBugDoBau, contadorResetBugDoBau, hasJustResetNow, blockReset = reiniciarBugDoBau(contadorDeTempoBugDoBau, contadorResetBugDoBau, hasJustResetNow, blockReset)
                    if hasJustResetNow == True and blockReset == False:
                        raise Exception('Erro ao achar um novo mapa')
                if (i != 0 and i % 90 == 0):
                    resetarPosicaoDosBonecosNoMapa()
            trabalhar = False

    except BaseException as err:
        print("Ocorreu um ERRO:")
        print(err)
        conectar = True