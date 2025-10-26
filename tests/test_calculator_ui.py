import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service


class TestCalculatorUI:

    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации и закрытия браузера Edge"""
        edge_options = Options()
        edge_options.add_argument("--headless")  # Режим без графического интерфейса
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        edge_options.add_argument("--disable-gpu")

        # Указываем прямой путь к EdgeDriver
        edge_driver_path = r"C:\Program Files\JetBrains\PyCharm Community Edition 2025.1.2\bin\msedgedriver.exe"

        # Создаем сервис с указанием пути к драйверу
        service = Service(executable_path=edge_driver_path)

        # Создаем драйвер
        driver = webdriver.Edge(service=service, options=edge_options)
        driver.implicitly_wait(10)

        # Получаем абсолютный путь к index.html
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        html_file = f"file://{project_root}/index.html"

        driver.get(html_file)
        yield driver
        driver.quit()

    def test_addition(self, driver):
        """Тест сложения"""
        # Вводим 2 + 3
        driver.find_element(By.XPATH, "//button[text()='2']").click()
        driver.find_element(By.XPATH, "//button[text()='+']").click()
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        driver.find_element(By.CLASS_NAME, "equals").click()

        result = driver.find_element(By.ID, "result").get_attribute('value')
        assert result == '5', f"Ожидалось 5, получено {result}"

    def test_subtraction(self, driver):
        """Тест вычитания"""
        # Вводим 10 - 4
        driver.find_element(By.XPATH, "//button[text()='1']").click()
        driver.find_element(By.XPATH, "//button[text()='0']").click()
        driver.find_element(By.XPATH, "//button[text()='-']").click()
        driver.find_element(By.XPATH, "//button[text()='4']").click()
        driver.find_element(By.CLASS_NAME, "equals").click()

        result = driver.find_element(By.ID, "result").get_attribute('value')
        assert result == '6', f"Ожидалось 6, получено {result}"

    def test_multiplication(self, driver):
        """Тест умножения"""
        # Вводим 3 × 4
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        driver.find_element(By.XPATH, "//button[text()='×']").click()
        driver.find_element(By.XPATH, "//button[text()='4']").click()
        driver.find_element(By.CLASS_NAME, "equals").click()

        result = driver.find_element(By.ID, "result").get_attribute('value')
        assert result == '12', f"Ожидалось 12, получено {result}"

    def test_division(self, driver):
        """Тест деления"""
        # Вводим 15 / 3
        driver.find_element(By.XPATH, "//button[text()='1']").click()
        driver.find_element(By.XPATH, "//button[text()='5']").click()
        driver.find_element(By.XPATH, "//button[text()='/']").click()
        driver.find_element(By.XPATH, "//button[text()='3']").click()
        driver.find_element(By.CLASS_NAME, "equals").click()

        result = driver.find_element(By.ID, "result").get_attribute('value')
        assert result == '5', f"Ожидалось 5, получено {result}"

    def test_clear_button(self, driver):
        """Тест кнопки очистки"""
        # Вводим число и очищаем
        driver.find_element(By.XPATH, "//button[text()='7']").click()
        driver.find_element(By.XPATH, "//button[text()='8']").click()
        driver.find_element(By.XPATH, "//button[text()='C']").click()

        result = driver.find_element(By.ID, "result").get_attribute('value')
        assert result == '', f"Ожидалась пустая строка, получено {result}"

    def test_decimal_calculation(self, driver):
        """Тест вычислений с десятичными числами"""
        # Вводим 2.5 + 1.5
        driver.find_element(By.XPATH, "//button[text()='2']").click()
        driver.find_element(By.XPATH, "//button[text()='.']").click()
        driver.find_element(By.XPATH, "//button[text()='5']").click()
        driver.find_element(By.XPATH, "//button[text()='+']").click()
        driver.find_element(By.XPATH, "//button[text()='1']").click()
        driver.find_element(By.XPATH, "//button[text()='.']").click()
        driver.find_element(By.XPATH, "//button[text()='5']").click()
        driver.find_element(By.CLASS_NAME, "equals").click()

        result = driver.find_element(By.ID, "result").get_attribute('value')
        assert result == '4', f"Ожидалось 4, получено {result}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--html=report.html"])