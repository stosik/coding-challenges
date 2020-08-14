/*
This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
 */
public class Day36 {

    // Time complexity O(h) where h is height of the BST tree
    // Method: reverse inorder traversal
    // Traversal of tree is O(logn)
    static void  findSecondLargestNode(Node node, Count count) {
        if (node == null || count.c >= 2)
            return;

        findSecondLargestNode(node.getRight(), count);

        count.c++;

        if (count.c == 2) {
            System.out.print("2nd largest element is "+ node.getValue());
            return;
        }

        findSecondLargestNode(node.getLeft(), count);
    }

    static void secondLargest(Node node) {
        Count C = new Count();
        findSecondLargestNode(node, C);
    }

    public static void main(String[] args) {
        Node firstNode = new Node(null, null, 1);
        Node secondNode = new Node(null, null, 5);
        Node thirdNode = new Node(null, null, 8);
        Node fourthNode = new Node(null, null, 14);
        Node fifthNode = new Node(firstNode, secondNode, 2);
        Node sixthNode = new Node(thirdNode, fourthNode, 9);
        Node root = new Node(fifthNode, sixthNode, 7);

        secondLargest(root);
    }

    public final static class Count {
        int c = 0;
    }

    public final static class Node {
        private final Node left;
        private final Node right;
        private final int value;

        public Node(Node left, Node right, int value) {
            this.left = left;
            this.right = right;
            this.value = value;
        }

        public Node getLeft() {
            return left;
        }

        public Node getRight() {
            return right;
        }

        public int getValue() {
            return value;
        }
    }
}
