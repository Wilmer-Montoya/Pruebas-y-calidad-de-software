from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: My first Project
    Package: TestProject.Generated.Tests.MyFirstProject
    Test: CP9
    Generated by: nicolas quintero (nic210597@gmail.com)
    Generated on 10/14/2021, 01:22:55
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="2Eq5wTBvQSEFpP0uGKHEtmg86yGL2TDPDarRn3yplA0",
                              project_name="My first Project",
                              job_name="CP9")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=1000,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "http://localhost/proyecto/login1/Login.html"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'cod'
    cod = driver.find_element(By.CSS_SELECTOR,
                              "[name='cod']")
    cod.click()

    # 3. Type '3006' in 'cod'
    cod = driver.find_element(By.CSS_SELECTOR,
                              "[name='cod']")
    cod.send_keys("3006")

    # 4. Click 'pass'
    _pass = driver.find_element(By.CSS_SELECTOR,
                                "[name='pass']")
    _pass.click()

    # 5. Type '123' in 'pass'
    _pass = driver.find_element(By.CSS_SELECTOR,
                                "[name='pass']")
    _pass.send_keys("123")

    # 6. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//input[4]")
    input.click()

    # 7. Click 'editar informacion'
    editar_informacion = driver.find_element(By.XPATH,
                                             "//a[. = 'editar informacion']")
    editar_informacion.click()

    # 8. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//input[4]")
    input.click()

    # 9. Click 'semes'
    semes = driver.find_element(By.CSS_SELECTOR,
                                "[name='semes']")
    semes.click()

    # 10. Type 'II' in 'semes'
    semes = driver.find_element(By.CSS_SELECTOR,
                                "[name='semes']")
    semes.send_keys("II")

    # 11. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//input[4]")
    input.click()

    # 12. Click 'corre'
    corre = driver.find_element(By.CSS_SELECTOR,
                                "[name='corre']")
    corre.click()

    # 13. Type 'NIC@GMAIL.COM' in 'corre'
    corre = driver.find_element(By.CSS_SELECTOR,
                                "[name='corre']")
    corre.send_keys("NIC@GMAIL.COM")

    # 14. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//input[4]")
    input.click()

    # 15. Click 'pass'
    _pass = driver.find_element(By.CSS_SELECTOR,
                                "[name='pass']")
    _pass.click()

    # 16. Type '123' in 'pass'
    _pass = driver.find_element(By.CSS_SELECTOR,
                                "[name='pass']")
    _pass.send_keys("123")

    # 17. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//input[4]")
    input.click()

    # 18. Navigate to 'http://localhost/proyecto/php/estudiante.php'
    step_settings = StepSettings(invert_result=True)
    with DriverStepSettings(driver, step_settings):
        driver.get("http://localhost/proyecto/php/estudiante.php")

    # 19. Click 'BODY'
    body = driver.find_element(By.XPATH,
                               "//body")
    body.click()

    # 20. Click 'Cerrar Sesion'
    cerrar_sesion = driver.find_element(By.XPATH,
                                        "//a[. = 'Cerrar Sesion']")
    cerrar_sesion.click()
