const element = document.querySelector('#name');
const target1 = document.querySelector('#line1');
const target2 = document.querySelector('#line2');
var element1 = document.querySelector('#ConnectionRequestsNum');
var element2 = document.querySelector('#YourConnectionsNum');
var element3 = document.querySelector('#ConnectionRequestsBox');
var ConnectionRequestsNum = 2;
var YourConnectionsNum = 495;
function accept1() {
    target1.remove();
    ConnectionRequestsNum -= 1;
    element1.innerText = ConnectionRequestsNum;
    YourConnectionsNum += 1;
    element2.innerText = YourConnectionsNum;
}
function accept2() {
    target2.remove();
    ConnectionRequestsNum -= 1;
    element1.innerText = ConnectionRequestsNum;
    YourConnectionsNum += 1;
    element2.innerText = YourConnectionsNum;
}
function deny1() {
    target1.remove();
    ConnectionRequestsNum -= 1;
    element1.innerText = ConnectionRequestsNum;
}
function deny2() {
    target2.remove();
    ConnectionRequestsNum -= 1;
    element1.innerText = ConnectionRequestsNum;
}
function edit() {
    element.innerText = "Someone Else"

}