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

    removeFront() {
        if (!this.head) {
            return null;
        }
        const newHead = this.head.next;
        this.head = newHead;
        return this.head;
    }

    front() {
        return this.head ? this.head.data : null;
    }
}


const SLL1 = new SLL();
console.log(SLL1.addFront(18)); // Node { data: 18, next: null }
console.log(SLL1.addFront(5)); // Node { data: 5, next: Node { data: 18, next: null } }
console.log(SLL1.addFront(73)); // Node { data: 73, next: Node { data: 5, next: Node { data: 18, next: null } } }

console.log(SLL1.removeFront()); // Node { data: 5, next: Node { data: 18, next: null } }
console.log(SLL1.removeFront()); // Node { data: 18, next: null }

console.log(SLL1.front()); // 18
console.log(SLL1.removeFront()); // null
console.log(SLL1.front()); // null