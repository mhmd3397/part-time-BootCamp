class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }

    max() {
        if (!this.head) {
            return null;
        }
        let current = this.head;
        let max = this.head.data;
        while (current) {
            if (current.data > max) {
                max = current.data;
            }
            current = current.next;
        }
        return max;
    }

    min() {
        if (!this.head) {
            return null;
        }
        let current = this.head;
        let min = this.head.data;
        while (current) {
            if (current.data < min) {
                min = current.data;
            }
            current = current.next;
        }
        return min;
    }

    average() {
        if (!this.head) {
            return null;
        }
        let current = this.head;
        let sum = 0;
        let count = 0;
        while (current) {
            sum += current.data;
            count++;
            current = current.next;
        }
        return sum / count;
    }
}