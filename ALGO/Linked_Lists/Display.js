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

    addFront(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        return this.head;
    }

    display() {
        let values = [];
        let current = this.head;
        while (current) {
            values.push(current.data);
            current = current.next;
        }
        return values.join(', ');
    }
}

// Test the implementation
const SLL1 = new SLL();
SLL1.addFront(76);
SLL1.addFront(2);
console.log(SLL1.display()); // => "2, 76"
SLL1.addFront(11.41);
console.log(SLL1.display()); // => "11.41, 2, 76"