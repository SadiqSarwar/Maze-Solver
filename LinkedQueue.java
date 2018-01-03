/**
 * Linked Queue class for maze solver
 */
import java.awt.Point;
public class LinkedQueue {
	
	/**
	 * Node class of Linked Queue
	 * @author SadiqSarwar
	 */
	private static class Node {
		/** data in point object of node **/
		private Point data;
		/** next node in node object **/
		private Node next;
		
		/**
		 * Constructs the node in queue
		 * @param d passed in point
		 */
		public Node( Point d ) {
			data = d;
			next = null;
		}
		
		/**
		 * Returns data as string
		 * @return point data
		 */
		public String toString() {
			return data.toString();
		}
	}
	
	/** first node of queue **/
	private Node first;
	/** last node of queue **/
	private Node last;
	
	/**
	 * Constructs the Queue
	 */
	public LinkedQueue(){
		first = null;
		last = null;
	}
	
	/**
	 * Checks to see if stack is empty
	 * @return T/F depending on condition
	 */
	public boolean isEmpty() {
		return first == null;
	}
	
	/**
	 * Adds a new point to the stack
	 * @param p passed in point object
	 */
	public void add( Point p ) {
		if( isEmpty() ) {
			first = new Node(p);
			last = first;
		} else {
			Node n = new Node(p);
			last.next = n;
			last = n;
		}
	}
	
	/**
	 * Removes a point from the stack
	 * @return removed point as string
	 */
	public String remove() {
		String ret = "";
		if( isEmpty() ) {
			System.out.println("Nothing to Remove");
		} else {
			ret = first.data.toString();
			first = first.next;
			if( first == null ) {
				last = null;
			}
		}
		return ret;
	}
	
	/**
	 * Checks the top point in stack
	 * @return top point as string
	 */
	public String peek() {
	String ret = "";
	if( isEmpty() ) {
		System.out.println("Queue is Empty");
		} else {
			ret = first.data.toString();
		}
		return ret;
	}
	
	/**
	 * Checks the size of the queue
	 * @return size of queue
	 */
	public int size() {
		int count = 0;
		Node n = first;
		while( n != null ) {
			count++;
			n = n.next;
		}
		return count;
	}
	
	/**
	 * Returns queue as a string
	 * @return queue as string
	 */
	@Override
	public String toString() {
		String s = "";
		Node n = first;
		while( n != null ) {
			s = s + n.data;
			n = n.next;
		}
		return s;
	}
	
	/**
	 * Returns data of top stack
	 * @return top point
	 */
	public Point retData() {
		return first.data;
	}

}
