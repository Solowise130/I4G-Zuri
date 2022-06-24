alert("Hi there, this is a simple calculator for you. kindly insert the right parameters as this calculator can only perform operations between two numbers. Cheers.");


function add(a, b) {
    alert("Result: "+ (a) + " + " + (b) + " = " + (a + b));
}
function subtract(a, b) {
    alert("Result: "+ (a) + " - " + (b) + " = " + (a - b));
}
function divide(a, b) {
    alert("Result: " + (a) + " / " + (b) + " = " + (a / b));
}
function multiply(a, b) {
    alert("Result: "+ (a) + " * " + (b) + " = " + (a * b));
}


function calculate(a, b, operation) {
    if (operation == "+") {
        add(a, b);
    } else if (operation == "-") {
        subtract(a, b);
    } else if (operation == "/") {
        divide(a, b);
    } else if (operation == "*") {
        multiply(a, b);
    } else {
        alert("Kindly insert a valid operation.");
    }
}

let a = parseFloat(prompt("Kindly insert the first number: "));
let b = parseFloat(prompt("Kindly insert the second number: "));
let operation = prompt("Kindly insert the operation you would like to perform: add +, subtract -, divide /, multiply * ");

calculate(a, b, operation);
