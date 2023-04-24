var sum=0,product=1;
for (i = 1; i <= 20; i++) {
    if (i % 2 != 0) {
        console.log(i);
    }
}
for (i1 = 100; i1 >= 0; i1--) {
    if (i1 % 3 == 0) {
        console.log(i1);
    }
}
for (i2 = 4; i2 > -4; i2 -= 1.5) {
    console.log(i2);
}
for (i3 = 1; i3 <= 100; i3++) {
    sum += i3;
}
console.log(sum);
for (i4 = 1; i4 <= 12; i4++) {
    product *= i4;
}
console.log(product);