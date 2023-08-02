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
    contains(value) {
        let runner = this.head;
        while (runner) {
            if (runner.data === value) {
                return true;
            }
            runner = runner.next;
        }
        return false;
    }
}
