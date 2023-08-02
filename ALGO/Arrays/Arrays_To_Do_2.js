// Reverse
function Reverse(array) {
    for (i = 0; i < array.length / 2; i++) {
        num = array[i]
        array[i] = array[array.length - i - 1]
        array[array.length - i - 1] = num
    }
    console.log(array)
}
Reverse([-2, -2, 3.14, 5, 5, 10, 1, 6])

// Rotate

function rotateArr(array, shiftBy) {
    let p = 1;
    while (p <= shiftBy) {
        last = array[0];
        for (i = 0; i < array.length - 1; i++) {
            array[i] = array[i + 1];
        }
        array[array.length - 1] = last;
        p++;
    }

console.log(array)
}
rotateArr([1, 2, 3, 4, 5, 6, 7, 8], 6)