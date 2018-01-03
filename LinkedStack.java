/**
 * Linked Stack class for maze solver
 */

import java.awt.Point;
public class LinkedStack {
	
	/**
	 * Node class of Stack Class
	 * @author SadiqSarwar
	 */
	private static class Node {
		/** data in point object of node **/
		private Point data;
		/** next node in node object **/
		private Node next;
		
		/**
		 * Constructs a node
		 * @param p passed in point object
		 * @param n passed in node
		 */
		public Node(Point p, Node n) {
			data = p;
			next = n;
		}
		
		/**
		 * Returns data as string
		 * @return point data
		 */
		@Override
		public String toString() {
				return data.toString();
		}
		
	}
	
	/** top node of stack **/
	private Node top;
	
	/** 
	 * Constructs the stack
	 */
	public LinkedStack() {
		top = null;
	}
	
	/**
	 * Checks to see if stack is empty
	 * @return T/F depending on condition
	 */
	public boolean isEmpty() {
		return top == null;
	}
	
	/**
	 * Adds a new point to the stack
	 * @param p passed in point object
	 */
	public void push( Point p ) {
		top = new Node( p, top );
	}
	
	/**
	 * Removes a point from the stack
	 * @return removed point as string
	 */
	public String pop() {
		String retVal = "";
		if( isEmpty() ){
			System.out.println("Nothing to Remove");
		} else {
			retVal = top.data.toString();
			top = top.next;
		}
		return retVal;
	}
	
	/**
	 * Checks the top point in stack
	 * @return top point as string
	 */
	public String peek() {
		String retVal = "";
		if( isEmpty() ){
			System.out.println("Stack is Empty");
		} else {
			retVal = top.data.toString();
		}
		return retVal;
	}
	
	/**
	 * Returns stacks as a string
	 * @return stack as string
	 */
	@Override
	public String toString() {
		String s = "";
		Node n = top;
		while( n != null ) {
			s = s + n.data.toString() + " ";
			n = n.next;
		}
		return s;
	}
	
	/**
	 * Returns data of top stack
	 * @return top point
	 */
	public Point retData() {
		return top.data;
	}
	
}
