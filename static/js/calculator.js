const output = document.getElementById('out')

const sings = document.querySelectorAll('.sing')
const digits = document.querySelectorAll('.digit')

digits.forEach(button => {
    button.addEventListener('click', function () {
        if(output.value ==" ") {
            output.value = button.value;
        }else if(button.value == 'C'){
            output.value = "";
        } else{
           output.value += button.value;
        }
    })
})