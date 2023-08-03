function rFib(num) {
    num = Math.floor(num)
    if (num <= 0) {
        return 0;
    }
    if (num == 1) {
        return 1;
    }
    return rFib(num - 1) + rFib(num - 2);
}

// Test the function
console.log(rFib(2));
console.log(rFib(3));
console.log(rFib(4));
console.log(rFib(5));
console.log(rFib(3.65));
console.log(rFib(-2));

function rTrib(num) {
    num = Math.floor(num)
    if (num === 0) {
        return 0;
    }
    if (num == 1) {
        return 0;
    }
    if (num == 2) {
        return 1;
    }
    return rTrib(num - 3) + rTrib(num - 2) + rTrib(num - 1);
}

// Test the function
console.log(rTrib(3));
console.log(rTrib(4));
console.log(rTrib(5));
console.log(rTrib(6));

function ackermann(num1, num2) {
    if (num1 === 0) {
        return num2 + 1;
    } else if (num2 === 0) {
        return ackermann(num1 - 1, 1);
    } else {
        return ackermann(num1 - 1, ackermann(num1, num2 - 1));
    }
}

// Test the function
console.log(ackermann(0, 3));
console.log(ackermann(3, 0));
console.log(ackermann(3, 3));

function zibonacci(num) {
    if (num === 0) {
        return 1;
    }
    if (num === 1) {
        return 1;
    }
    if (num === 2) {
        return 2;
    }
    if (num % 2 === 1) {
        const n = Math.floor(num / 2);
        return zibonacci(n) + zibonacci(n - 1) + 1;
    } else {
        const n = Math.floor(num / 2);
        return zibonacci(n) + zibonacci(n + 1) + 1;
    }
}
// Test the function
console.log(zibonacci(10));
console.log(zibonacci(100));