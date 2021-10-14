from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Pruebas Proyecto
    Package: TestProject.Generated.Tests.PruebasProyecto
    Test: CP01_Registrar estudiante-Usuario
    Generated by: Fredy Jerez (fajerez81@ucatolica.edu.co)
    Generated on 10/14/2021, 01:49:47
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="qyJeWun1EXv3arDm_jbj0EAqyUq4_u-dQhJ-J5NDhqY",
                              project_name="Pruebas Proyecto",
                              job_name="CP01_Registrar estudiante-Usuario")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
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

    # 2. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//input[3]")
    input.click()

    # 3. Click 'cod'
    cod = driver.find_element(By.CSS_SELECTOR,
                              "[name='cod']")
    cod.click()

    # 4. Click 'cod'
    cod = driver.find_element(By.CSS_SELECTOR,
                              "[name='cod']")
    cod.click()

    # 5. Type '6700000' in 'cod'
    cod = driver.find_element(By.CSS_SELECTOR,
                              "[name='cod']")
    cod.send_keys("6700000")

    # 6. Click 'nomb'
    nomb = driver.find_element(By.CSS_SELECTOR,
                               "[name='nomb']")
    nomb.click()

    # 7. Type 'Fredy' in 'nomb'
    nomb = driver.find_element(By.CSS_SELECTOR,
                               "[name='nomb']")
    nomb.send_keys("Fredy")

    # 8. Type 'Jerez' in 'ape'
    ape = driver.find_element(By.CSS_SELECTOR,
                              "[name='ape']")
    ape.send_keys("Jerez")

    # 9. Click 'semes'
    semes = driver.find_element(By.CSS_SELECTOR,
                                "[name='semes']")
    semes.click()

    # 10. Type 'VII' in 'semes'
    semes = driver.find_element(By.CSS_SELECTOR,
                                "[name='semes']")
    semes.send_keys("VII")

    # 11. Click 'corre'
    corre = driver.find_element(By.CSS_SELECTOR,
                                "[name='corre']")
    corre.click()

    # 12. Type 'fajerez81@ucatolica.edu.co' in 'corre'
    corre = driver.find_element(By.CSS_SELECTOR,
                                "[name='corre']")
    corre.send_keys("fajerez81@ucatolica.edu.co")

    # 13. Click 'pass'
    _pass = driver.find_element(By.CSS_SELECTOR,
                                "[name='pass']")
    _pass.click()

    # 14. Type '123456' in 'pass'
    _pass = driver.find_element(By.CSS_SELECTOR,
                                "[name='pass']")
    _pass.send_keys("123456")

    # 15. Click 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//input[7]")
    input1.click()
