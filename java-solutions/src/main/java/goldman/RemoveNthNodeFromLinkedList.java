package goldman;

public class RemoveNthNodeFromLinkedList {

    static void removeNthFromEnd(Node head, int n) {
        Node mainPointer = head;
        Node refPointer = head;

        int count = 0;

        if (head != null) {
            while (count < n) {
                if (refPointer == null)
                    return;

                refPointer = refPointer.getNext();
                count++;
            }
        }

        while (refPointer != null) {
            mainPointer = mainPointer.getNext();
            refPointer = refPointer.getNext();
        }

        mainPointer.next = mainPointer.getNext().getNext();
    }

    public static void main(String[] args) {
        Node firstNode = new Node(5);
        Node secondNode = new Node(firstNode, 4);
        Node thirdNode = new Node(secondNode, 3);
        Node fourthNode = new Node(thirdNode, 2);
        Node head = new Node(fourthNode, 1);

        firstNode.setNext(fourthNode);

        removeNthFromEnd(head, 2);
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
