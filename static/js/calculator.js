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
        }else if (button.value == "C"){
          output.value = " ";
        } else if (button.value == "CE"){
          output.value = output.value.substring(0, output.value.length - 1);
        }else {
            output.value += ` ${button.value} `;
        }
    })
})

