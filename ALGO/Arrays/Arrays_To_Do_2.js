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



function filterRangeV2(arr, minVal, maxVal) {
    var nextInd = 0; // Index where the next array value that's from min to max (inclusively) will go
    // Loop through the array
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] >= minVal && arr[i] <= maxVal) {
            arr[nextInd] = arr[i];
            nextInd++; // Increment index for next valid value found
        }
    }
    arr.length = nextInd; // Chop off excess values
}



// Concat

function arrConcat(array1, array2) {
    new_arr = []
    for (i = 0; i < array1.length; i++) {
        new_arr[new_arr.length] = array1[i]
    }
    for (i = 0; i < array2.length; i++) {
        new_arr[new_arr.length] = array2[i]
    }
    console.log(new_arr)
}
arrConcat(['a', 'b'], [1, 2])