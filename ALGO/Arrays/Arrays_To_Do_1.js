// Arrays To Do 1

// Push Front
function pushFront(array, num) {
    length = array.length;
    new_array = [];
    new_array[0] = num
    for (i = 1; i <= length; i++) {
        new_array[i] = array[i - 1]
    }
    console.log(new_array)
}
// pushFront([5,7,2,3], 8) => [8,5,7,2,3]
pushFront([5, 7, 2, 3], 8)
// pushFront([99], 7) => [7,99]
pushFront([99], 7)

// Pop Front
function popFront(array, num) {
    length = array.length;
    new_array = [];
    for (i = 1; i < length; i++) {
        new_array[i - 1] = array[i]
    }
    console.log(new_array)
}
// popFront([0,5,10,15]) => 0 returned, with [5,10,15] printed in the function
popFront([0, 5, 10, 15])
// popFront([4,5,7,9]) => 4 returned, with [5,7,9] printed in the function
popFront([4, 5, 7, 9])

// Insert At
function insertAt(array, num, val) {
    length = array.length;
    new_array = [];
    for (i = 0; i < num; i++) {
        new_array[i] = array[i]
    }
    for (i = num + 1; i <= length; i++) {
        new_array[i] = array[i - 1]
    }
    new_array[num] = val
    console.log(new_array)
}
// insertAt([100,200,5], 2, 311) => [100,200,311,5]
insertAt([100, 200, 5], 2, 311)
// insertAt([9,33,7], 1, 42) => [9,42,33,7]
insertAt([9, 33, 7], 1, 42)

// BONUS: Remove At
function removeAt(array, num) {
    length = array.length;
    new_array = [];
    for (i = 0; i < length; i++) {
        if (i <= num) {
            new_array[i] = array[i]
        }
        if (i > num) {
            new_array[i - 1] = array[i]
        }
    }
    console.log(new_array)
}



// removeAt([1000,3,204,77], 1) => 3 returned, with [1000,204,77] printed in the function
removeAt([1000, 3, 204, 77], 1)
// removeAt([8,20,55,44,98], 3) => 44 returned, with [8,20,55,98] printed in the function
removeAt([8, 20, 55, 44, 98], 3)


// BONUS: Swap Pairs
function swap(array) {

    num = array[0]
    array[0] = array[1]
    array[1] = num



    console.log(array)
}

// insertAt([1,2,3,4]) => [2,1,4,3]
swap([1, 2, 3, 4])
// insertAt(["Brendan",true,42]) => [true,"Brendan",42]
swap(["Brendan", true, 42])


// BONUS: Remove Duplicates
function removeDupes(array) {
    length = array.length;
    new_array = [];
    for (i = 0; i < length; i++) {
        if (array[i] != array[i - 1]) {
            new_array.push(array[i])

        }
    }
    console.log(new_array)
}


// removeDupes([-2, -2, 3.14, 5, 5, 10]) => [-2, 3.14, 5, 10]
removeDupes([-2, -2, 3.14, 5, 5, 10])
// removeDupes([9, 19, 19, 19, 19, 19, 29]) => [9, 19, 29]
removeDupes([9, 19, 19, 19, 19, 19, 29])