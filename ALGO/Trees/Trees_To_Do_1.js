class BTNode {
    constructor(value) {
        this.val = value;
        this.left = null;
        this.right = null;
    }
}

class BST {
    constructor() {
        this.root = null;
    }

    // Add a new value to the BST
    add(val) {
        const newNode = new BTNode(val);
        if (!this.root) {
            this.root = newNode;
        } else {
            this._addRecursive(this.root, newNode);
        }
    }

    _addRecursive(currentNode, newNode) {
        if (newNode.val < currentNode.val) {
            if (!currentNode.left) {
                currentNode.left = newNode;
            } else {
                this._addRecursive(currentNode.left, newNode);
            }
        } else {
            if (!currentNode.right) {
                currentNode.right = newNode;
            } else {
                this._addRecursive(currentNode.right, newNode);
            }
        }
    }

    // Check if the BST contains a given value
    contains(val) {
        return this._containsRecursive(this.root, val);
    }

    _containsRecursive(currentNode, val) {
        if (!currentNode) {
            return false;
        }

        if (currentNode.val === val) {
            return true;
        } else if (val < currentNode.val) {
            return this._containsRecursive(currentNode.left, val);
        } else {
            return this._containsRecursive(currentNode.right, val);
        }
    }

    // Find the smallest value in the BST
    min() {
        if (!this.root) {
            return null;
        }
        let currentNode = this.root;
        while (currentNode.left) {
            currentNode = currentNode.left;
        }
        return currentNode.val;
    }

    // Find the largest value in the BST
    max() {
        if (!this.root) {
            return null;
        }
        let currentNode = this.root;
        while (currentNode.right) {
            currentNode = currentNode.right;
        }
        return currentNode.val;
    }

    // Get the number of nodes in the BST
    size() {
        return this._sizeRecursive(this.root);
    }

    _sizeRecursive(currentNode) {
        if (!currentNode) {
            return 0;
        }
        return 1 + this._sizeRecursive(currentNode.left) + this._sizeRecursive(currentNode.right);
    }

    // Check if the BST is empty
    isEmpty() {
        return this.root === null;
    }
}