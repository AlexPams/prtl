const output = document.getElementById('out');
const sings = document.querySelectorAll('.sing');
const digits = document.querySelectorAll('.digit');

digits.forEach(button => {
    button.addEventListener('click', function () {
            output.value += button.value;
    })
})

sings.forEach(button => {
    button.addEventListener('click', function () {
        if (button.value == "=") {
            output.value = eval(output.value)
        } else {
            output.value += ` ${button.value} `;
        }
    })
})
