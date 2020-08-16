package goldman;

import java.util.Stack;

// Inorder traversal DFS (left, root, right)
// if array has elements in not ascending order the tree is not BST
public class BinaryTreeIsBinarySearchTree {

    static boolean isBinarySearchTree(Node root) {
        Stack<Node> stack = new Stack<>();
        double inorder = -Double.MAX_VALUE;

        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }

            root = stack.pop();

            if (root.value <= inorder)
                return false;

            inorder = root.value;
            root = root.right;
        }

        return true;
    }

    public static void main(String[] args) {


    }

    public static class Node {
        private Node left;
        private Node right;
        private int value;

        public Node(int value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }

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

        public void setLeft(Node left) {
            this.left = left;
        }

        public void setRight(Node right) {
            this.right = right;
        }
    }
}
