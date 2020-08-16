package goldman;


// Floyd’s Cycle-Finding Algorithm
// move two pointers at the same time
// one by one node, and second by two nodes
// if they meet at some point in the same node there is the CYCLE

import java.util.Objects;

// Time complexity O(n)
// Space complexity O(1)
public class CycleInLinkedList {

    static boolean hasCycle(Node head) {
        if (head.next == null) {
            return false;
        }

        Node slowPointer = head;
        Node fastPointer = head;
        int flag = 0;

        while (slowPointer != null && fastPointer != null && fastPointer.next != null) {
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next.next;
            if (slowPointer == fastPointer) {
                flag = 1;
                break;
            }
        }

        return flag == 1;
    }

    public static void main(String[] args) {
        Node firstNode = new Node(5);
        Node secondNode = new Node(firstNode, 4);
        Node thirdNode = new Node(secondNode, 3);
        Node fourthNode = new Node(thirdNode, 2);
        Node head = new Node(fourthNode, 1);

        firstNode.setNext(fourthNode);

        System.out.println(hasCycle(head));
    }

    public static class Node {
        private Node next;
        private int val;

        public Node(Node next, int val) {
            this.next = next;
            this.val = val;
        }

        public Node(int val) {
            this.val = val;
        }

        public int getVal() {
            return val;
        }

        public Node getNext() {
            return next;
        }

        public void setNext(Node next) {
            this.next = next;
        }
    }
}
