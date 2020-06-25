import java.util.PriorityQueue;
import java.util.Queue;

public class KthLargestElement {

    public static void main(String[] args) {

    }


    public int kthLargestElement(int[] nums, int k) {
      Queue<Integer> minQueue = new PriorityQueue<Integer>(k);
    
      for(int number : nums) {
          minQueue.offer(number);
          if(minQueue.size() > k) {
              minQueue.poll();
          }
      }
      
      return minQueue.peek();
  }
}