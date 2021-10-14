from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: My first Project
    Package: TestProject.Generated.Tests.MyFirstProject
    Test: CP 5
    Generated by: MIGUEL ANGEL FLOREZ TRASLAVINA (maflorez14@ucatolica.edu.co)
    Generated on 10/14/2021, 01:05:12
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="XlEruqXuApR03aR7B3ihNrnu7FjCaTUK8FfUGJ-crgU",
                              project_name="My first Project",
                              job_name="CP 5")
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
    MateriaNOExist = "NOEXISTE"  # Materia NO Existente

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

    # 4. Type '777' in 'pass'
    _pass = driver.find_element(By.CSS_SELECTOR,
                                "[name='pass']")
    _pass.send_keys("777")

    # 5. Send 'ENTER' key(s)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    # 6. Click 'Agregar Materia'
    agregar_materia = driver.find_element(By.XPATH,
                                          "//a[. = 'Agregar Materia']")
    agregar_materia.click()

    # 7. Click 'semes'
    semes = driver.find_element(By.CSS_SELECTOR,
                                "[name='semes']")
    semes.click()

    # 8. Type '{MateriaNOExist}' in 'semes'
    semes = driver.find_element(By.CSS_SELECTOR,
                                "[name='semes']")
    semes.send_keys(f'{MateriaNOExist}')

    # 9. Click 'INPUT'
    input = driver.find_element(By.XPATH,
                                "//input[2]")
    input.click()

    # 10. Navigate to 'http://localhost/proyecto/php/agegar.php'
    step_settings = StepSettings(invert_result=True)
    with DriverStepSettings(driver, step_settings):
        driver.get("http://localhost/proyecto/php/agegar.php")

    # 11. Click 'Agregar materia1'
    agregar_materia1 = driver.find_element(By.XPATH,
                                           "//h1[. = ' Agregar materia ']")
    agregar_materia1.click()
