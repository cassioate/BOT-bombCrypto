import pyautogui
import time

pyautogui.PAUSE = 2

def procurarImagem(imagem):
    contadorProcurarImagem = 0
    img = None
    confidence = 0.9
    while img == None:
        print("Procurando imagem: "+ imagem)
        img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
        contadorProcurarImagem += 1
        print(img)
        if contadorProcurarImagem >= 500:
            raise Exception('Erro ao achar a imagem: ' + imagem)
    return img

def procurarImagemSemRetornarErro(imagem):
    confidence = 0.75
    print("Procurando imagem: "+ imagem)
    img = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
    print(img)
    if img != None:
        return True

def conectarFunc():
    pyautogui.click(procurarImagem("ConnectWallet"), duration=3)
    pyautogui.click(procurarImagem("AssinarMetamask"), duration=3)

def enviarParaTrabalhar():
    pyautogui.click(procurarImagem("Heroes"), duration=3)
    pyautogui.click(procurarImagem("AllVerde"), duration=3)
    pyautogui.click(procurarImagem("X"), duration=3)
    pyautogui.click(procurarImagem("TreasureHunt"), duration=3)

def resetarPosicaoDosBonecosNoMapa():
    print("Atualizando Bonecos")
    pyautogui.click(procurarImagem("SetaVerdeVoltandoParaOMenu"), duration=3)
    pyautogui.click(procurarImagem("TreasureHunt"), duration=3)

def existirZzz(contadorZZZ, main, descansar):
    for i in range(5):
        if procurarImagemSemRetornarErro("zzz") or procurarImagemSemRetornarErro("z"):
            contadorZZZ += 1
            if contadorZZZ > 5:
                contadorZZZ = 0
                main = False
                descansar = True
                return contadorZZZ, main, descansar
    return contadorZZZ, main, descansar

def procurarLocalizacaoDaImagemPelosEixos(imagem):
    confidence = 0.9
    x, y = pyautogui.locateCenterOnScreen('./assets/'+ imagem+'.png', confidence=confidence)
    return x, y

def colocarHeroisNaCasa():
    #INSERINDO NA CASA EPIC E SUPER RARO
    xHome, yHome = procurarLocalizacaoDaImagemPelosEixos("Home")
    x590515, y590515 = procurarLocalizacaoDaImagemPelosEixos("590515")

    pyautogui.click(x=xHome, y=y590515, duration=3)
    time.sleep(5)
    pyautogui.click(x=xHome, y=y590515, duration=3)
    
    #DESCER A TELA PARA PROCURAR OUTROS HEROIS
    pyautogui.moveTo(x=673, y=626)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=670, y=380, duration=1.5)
    pyautogui.mouseUp(button='left')
    time.sleep(2)
    pyautogui.moveTo(x=673, y=626)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=670, y=380, duration=1.5)
    pyautogui.mouseUp(button='left')

    #INSERINDO NA CASA LEGEND E SUPER RARO
    xLegend, yLegend = procurarLocalizacaoDaImagemPelosEixos("Legend-746073")
    pyautogui.click(x=xHome, y=yLegend, duration=3)
    time.sleep(5)
    pyautogui.click(x=xHome, y=yLegend, duration=3)

    #VERIFICANDO SE OS DOIS SUPER RAROS ESTÃO COM EXCESSO DE BATERIA
    pyautogui.moveTo(x=673, y=626)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=670, y=380, duration=1.5)
    pyautogui.mouseUp(button='left')
    if (procurarImagemSemRetornarErro("SuperRaroXpCheioCavaleiro") and procurarImagemSemRetornarErro("SuperRaroXpCheioBruxa")):
        xSRaro, ySRaro = procurarLocalizacaoDaImagemPelosEixos("SuperRaroXpCheioCavaleiro")
        xWork, yWork = procurarLocalizacaoDaImagemPelosEixos("Work")
        pyautogui.click(x=xWork, y=ySRaro, duration=3)
        time.sleep(2)
        xSRaro2, ySRaro2 = procurarLocalizacaoDaImagemPelosEixos("SuperRaroXpCheioBruxa")
        pyautogui.click(x=xWork, y=ySRaro2, duration=3)

        #SUBINDO TELA
        pyautogui.moveTo(x=673, y=380)
        pyautogui.mouseDown(button='left')
        pyautogui.dragTo(x=670, y=626, duration=1.5)
        pyautogui.mouseUp(button='left')
        time.sleep(2)
        pyautogui.moveTo(x=673, y=380)
        pyautogui.mouseDown(button='left')
        pyautogui.dragTo(x=670, y=626, duration=1.5)
        pyautogui.mouseUp(button='left')
        time.sleep(2)
        pyautogui.moveTo(x=673, y=380)
        pyautogui.mouseDown(button='left')
        pyautogui.dragTo(x=670, y=626, duration=1.5)
        pyautogui.mouseUp(button='left')

        #PEGANDO O SRARO DE ID 590874(SuperRaroCowboy)
        xSRaro3, ySRaro3 = procurarLocalizacaoDaImagemPelosEixos("SuperRaroCowboy")
        pyautogui.click(x=xHome, y=ySRaro3, duration=3)
        
        #DESCENDO A TELA PARA PEGAR O SAPO sRARO
        pyautogui.moveTo(x=673, y=626)
        pyautogui.mouseDown(button='left')
        pyautogui.dragTo(x=670, y=400, duration=1.5)
        pyautogui.mouseUp(button='left')

        #PEGANDO O SRARO DE ID 694504(Sapo sRARO)
        xSRaro4, ySRaro4 = procurarLocalizacaoDaImagemPelosEixos("SuperRaroSapo")
        pyautogui.click(x=xHome, y=ySRaro4, duration=3)

    #COLOCANDO O RESTANTE PARA TRABALHAR
    pyautogui.moveTo(x=673, y=626)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=670, y=380, duration=1.5)
    pyautogui.mouseUp(button='left')
    time.sleep(2)
    pyautogui.moveTo(x=673, y=626)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=670, y=380, duration=1.5)
    pyautogui.mouseUp(button='left')
    time.sleep(2)
    pyautogui.moveTo(x=673, y=626)
    pyautogui.mouseDown(button='left')
    pyautogui.dragTo(x=670, y=380, duration=1.5)
    pyautogui.mouseUp(button='left')
    time.sleep(2)
    xRaro, yRaro = procurarLocalizacaoDaImagemPelosEixos("Raro-3322411")
    xWork, yWork = procurarLocalizacaoDaImagemPelosEixos("Work")
    for i in range(20):
        pyautogui.click(x=xWork, y=yRaro, duration=3)
    pyautogui.click(procurarImagem("X"), duration=3)
    pyautogui.click(procurarImagem("TreasureHunt"), duration=3)

    

conectar = True
trabalhar = True
main = False
descansar = False
contadorZZZ = 0
#CONNECT
while True:
    try:
        conectar = True
        while conectar == True:
            conectarFunc()
            conectar = False
            trabalhar = True
            main = False

        while trabalhar == True:
            enviarParaTrabalhar()
            trabalhar = False
            main = True

        while main == True:
            print(contadorZZZ, main, descansar)
            contadorZZZ, main, descansar = existirZzz(contadorZZZ, main, descansar)
            print(contadorZZZ, main, descansar)
            time.sleep(90)
            resetarPosicaoDosBonecosNoMapa()

        while descansar == True:
            pyautogui.click(procurarImagem("SetaVerdeVoltandoParaOMenu"), duration=3)
            pyautogui.click(procurarImagem("Heroes"), duration=3)
            if procurarImagemSemRetornarErro("AllLaranja"):
                pyautogui.click(procurarImagem("AllLaranja"), duration=3)
            else:
                pyautogui.click(procurarImagem("AllVerde"), duration=3)
                pyautogui.click(procurarImagem("AllLaranja"), duration=3)
            colocarHeroisNaCasa()
            for i in range(360):
                time.sleep(10)
                if (i % 9 == 0):
                    resetarPosicaoDosBonecosNoMapa

            descansar = False
            trabalhar = True

    except:
        print("Ocorreu um erro")
        conectar = True
        pyautogui.keyDown("ctrl")
        pyautogui.press("f5")
        time.sleep(5)
