from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: Pruebas
    Package: TestProject.Generated.Tests.Pruebas
    Test: CP-7
    Generated by: MIGUEL ANGEL FLOREZ TRASLAVINA (maflorez14@ucatolica.edu.co)
    Generated on 10/14/2021, 01:10:18
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="XlEruqXuApR03aR7B3ihNrnu7FjCaTUK8FfUGJ-crgU",
                              project_name="Pruebas",
                              job_name="CP-7")
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

    # 5. Type '777' in 'pass'
    _pass = driver.find_element(By.CSS_SELECTOR,
                                "[name='pass']")
    _pass.send_keys("777")

    # 6. Click 'INPUT1'
    input1 = driver.find_element(By.XPATH,
                                 "//input[4]")
    input1.click()

    # 7. Click 'Eliminar materia'
    eliminar_materia = driver.find_element(By.XPATH,
                                           "//a[. = 'Eliminar materia']")
    eliminar_materia.click()

    # 8. Click 'INPUT2'
    input2 = driver.find_element(By.XPATH,
                                 "//form/input")
    input2.click()

    # 9. Navigate to 'http://localhost/proyecto/php/estudiante.php'
    step_settings = StepSettings(invert_result=True)
    with DriverStepSettings(driver, step_settings):
        driver.get("http://localhost/proyecto/php/estudiante.php")

    # 10. Click 'Eliminar materia1'
    eliminar_materia1 = driver.find_element(By.XPATH,
                                            "//h1[. = ' Eliminar materia ']")
    eliminar_materia1.click()