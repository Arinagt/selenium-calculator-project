let display = document.getElementById('result');

function appendToDisplay(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

function deleteLast() {
    display.value = display.value.slice(0, -1);
}

function calculate() {
    try {
        let expression = display.value.replace('×', '*');
        let result = eval(expression);
        display.value = result;
    } catch (error) {
        display.value = 'Ошибка';
    }
}