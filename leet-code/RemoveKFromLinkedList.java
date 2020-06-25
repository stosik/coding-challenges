public void RemoveKFromLinkedList(String[] args) {

  public ListNode<Integer> removeKFromList(ListNode<Integer> l, int k) {
    while(l != null && l.value == k) {
        l = l.next;
    }
    
    ListNode<Integer> current = l;
    while(current != null && current.next != null) {
        if(current.next.value == k) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }
    
    return l;
  }
} 