function rSigma(num) {
    num = Math.floor(num)
    if (num <= 0) {
        return 0;
    }
    return num + rSigma(num - 1);
}

// Test the function
console.log(rSigma(5)); // Output: 15
console.log(rSigma(2.5)); // Output: 3
console.log(rSigma(-1)); // Output: 0


function rFact(num) {
    num = Math.floor(num)
    if (num <= 0) {
        return 1;
    }
    return num * rFact(num - 1);
}

// Test the function
console.log(rFact(3)); // Output: 6
console.log(rFact(6.5)); // Output: 720