function rBinarySearch(arr, value, start = 0, end = arr.length - 1) {
    if (start > end) {
        return false;
    }

    const mid = Math.floor((start + end) / 2);
    if (arr[mid] === value) {
        return true;
    } else if (arr[mid] < value) {
        return rBinarySearch(arr, value, mid + 1, end);
    } else {
        return rBinarySearch(arr, value, start, mid - 1);
    }
}

console.log(rBinarySearch([1, 3, 5, 6], 4));
console.log(rBinarySearch([4, 5, 6, 8, 12], 5));


function rGCF(num1, num2) {
    if (num2 === 0) {
        return num1;
    }

    return rGCF(num2, num1 % num2);
}

console.log(rGCF(12, 18)); // Output: 6
console.log(rGCF(48, 18)); // Output: 6
console.log(rGCF(123456, 987654)); // Output: 6
