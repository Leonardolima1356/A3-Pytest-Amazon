import time
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def capturar_tela(navegador, resultado):

    #Salvar evidência
    pasta_raiz = Path(__file__).resolve().parent.parent
    pasta_evidencias = pasta_raiz / "evidencias"
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    caminho_imagem = (
        pasta_evidencias
        / f"ct01_001_{resultado}_{data_hora}.png"
    )
    imagem_salva = navegador.save_screenshot(
        str(caminho_imagem)
    )

    if imagem_salva:
        print(f"\nEvidência salva em: {caminho_imagem}")
    else:
        print("\nNão foi possível salvar a evidência.")

def test_criacao_conta():
    navegador = webdriver.Chrome()

    try:
        navegador.maximize_window()

        navegador.get("https://www.amazon.com.br/")
        time.sleep(2)

        botao_login = navegador.find_element(By.ID, "nav-link-accountList")
        botao_login.click()

        campo_usuario = navegador.find_element(By.ID, "ap_email_login")
        campo_usuario.send_keys("unicuritibaaula3flavio@hotmail.com")

        botao_email = navegador.find_element(By.ID, "continue")
        botao_email.click()
        time.sleep(2)

        # Preenche a senha
        campo_senha = navegador.find_element(By.ID, "ap_password")
        campo_senha.send_keys("A3flavio1!")

        botao_entrar = navegador.find_element(By.ID, "signInSubmit")
        botao_entrar.click()
        time.sleep(2)

        botao_login2 = navegador.find_element(By.ID, "nav-link-accountList")
        botao_login2.click()
        time.sleep(5)

        capturar_tela(navegador, "sucesso")

    except Exception:
        capturar_tela(navegador, "falha")

        raise

    finally:
        print("\nO navegador será fechado em 5 segundos...")
        navegador.quit()