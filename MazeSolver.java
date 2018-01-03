
/**
 * Sadiq Sarwar
 * Project #4
 * Date: 11/29/2017
 * Solves imported mazes using stacks and queues
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.awt.Point;

public class MazeSolver {

	public static void main(String[] args) {
		int choice = -1;
		char [] [] array = null;
		while(choice != 0){
			LinkedStack stack = new LinkedStack();
			LinkedQueue queue = new LinkedQueue();
			System.out.println("[Maze Solver Menu]");
			System.out.println("1 - Maze #1");
			System.out.println("2 - Maze #2");
			System.out.println("3 - Maze #3");
			System.out.println("4 - Maze #4");
			System.out.println("0 - Quit");
			System.out.print("Which Maze Would You Like To Solve? ");
			choice = CheckInput.checkIntRange(0, 4);
			if(choice == 0){
				System.out.println("[Program Will Now Exit]");
				break;
			}else{
				array = importer(choice);
			}
			
			System.out.println("[Maze Solver Method]");
			System.out.println("1 - Depth First Search (DFS)");
			System.out.println("2 - Breadth First Search (BFS)");
			System.out.println("3 - User Solve");
			System.out.print("How Would You Like To Solve The Maze? ");
			int method = CheckInput.checkIntRange(1, 3);
			if(method == 1){
				Point start = startFinder(array);
				display(array);
				stack.push(start);
				mazeStackSolve(stack, array, start);
			}
			else if(method == 2){
				Point start = startFinder(array);
				display(array);
				queue.add(start);
				mazeQueueSolve(queue, array, start);
			}
			else if(method == 3){
				Point start = startFinder(array);
				display(array);
				queue.add(start);
				mazeUserSolve(stack, array, start);
			}
		}
	}
	
	/**
	 * Imports the maze from the files
	 * @param choice choice of maze
	 * @return 2D array of maze
	 */
	public static char [][] importer(int choice){
		char [][] array = new char [0][0];
		if (choice == 1){
			Scanner sc = new Scanner (System.in);
			char [][] array1 = new char [5][5];
			int row = 0;
			boolean testInputRead = true;
			while (testInputRead){
				try{
					Scanner read = new Scanner (new File("Maze-Level0.txt"));
					read.nextLine();
					while(read.hasNext()){ 
						String fileLine = read.nextLine();
						for(int i = 0; i < fileLine.length(); i++){
							array1[row][i] = fileLine.charAt(i);
						}
						row++;

					} // while(Read.hasNextInt())
					testInputRead = false;
				} // try --> while (TestInputRead)
				catch(FileNotFoundException e){
					System.out.println("Error - File Not Found");
				} // catch(FileNotFoundException e)
			} // while (TestInputRead)

			return(array1);
		}
		if (choice == 2){
			Scanner sc = new Scanner (System.in);
			char [][] array2 = new char [9][15];
			int row = 0;
			boolean testInputRead = true;
			while (testInputRead){
				try{
					Scanner read = new Scanner (new File("Maze-Level1.txt"));
					read.nextLine();
					while(read.hasNext()){ 
						String fileLine = read.nextLine();
						for(int i = 0; i < fileLine.length(); i++){
							array2[row][i] = fileLine.charAt(i);
						}
						row++;

					} // while(Read.hasNextInt())
					testInputRead = false;
				} // try --> while (TestInputRead)
				catch(FileNotFoundException e){
					System.out.println("Error - File Not Found");
				} // catch(FileNotFoundException e)
			} // while (TestInputRead)

			return(array2);
		}
		if (choice == 3){
			Scanner sc = new Scanner (System.in);
			char [][] array3 = new char [11][21];
			int row = 0;
			boolean testInputRead = true;
			while (testInputRead){
				try{
					Scanner read = new Scanner (new File("Maze-Level2.txt"));
					read.nextLine();
					while(read.hasNext()){ 
						String fileLine = read.nextLine();
						for(int i = 0; i < fileLine.length(); i++){
							array3[row][i] = fileLine.charAt(i);
						}
						row++;

					} // while(Read.hasNextInt())
					testInputRead = false;
				} // try --> while (TestInputRead)
				catch(FileNotFoundException e){
					System.out.println("Error - File Not Found");
				} // catch(FileNotFoundException e)
			} // while (TestInputRead)
			return(array3);
		}
		if (choice == 4){
			Scanner sc = new Scanner (System.in);
			char [][] array4 = new char [41][82];
			int row = 0;
			boolean testInputRead = true;
			while (testInputRead){
				try{
					Scanner read = new Scanner (new File("Maze-Level3.txt"));
					read.nextLine();
					while(read.hasNext()){ 
						String fileLine = read.nextLine();
						for(int i = 0; i < fileLine.length(); i++){
							array4[row][i] = fileLine.charAt(i);
						}
						row++;

					} // while(Read.hasNextInt())
					testInputRead = false;
				} // try --> while (TestInputRead)
				catch(FileNotFoundException e){
					System.out.println("Error - File Not Found");
				} // catch(FileNotFoundException e)
			} // while (TestInputRead)

			return(array4);
		}
		return(array);
	}
	
	/**
	 * Displays the 2D array
	 * @param array 2D maze
	 */
	public static void display(char [][] array){
		for(int i = 0; i < array.length; i++){
			for(int j = 0; j < array[i].length; j++){
				System.out.print(array[i][j]);
			}
			System.out.println();
		}
	}
	
	/**
	 * Finds the starting point of maze
	 * @param array 2D maze array
	 * @return point of start
	 */
	public static Point startFinder(char [][] array){
		Point start = new Point (0,0);	
		for(int i = 0; i < array.length; i++){
			for(int j = 0; j < array[i].length; j++){
				if(array[i][j] == 's'){
					System.out.println("("+i+","+j+")");
					start.setLocation(i, j);	
				}
			}
		}
		return start;
	}
	
	/**
	 * Solves the maze using stacks
	 * @param stack stack of empty
	 * @param array 2D maze
	 * @param start starting point of maze
	 */
	public static void mazeUserSolve(LinkedStack stack, char [][] array, Point start){
		stack.push(start);
		Point current = start;
		
		while(array[current.x][current.y] != 'f'){
			System.out.println("[Maze Solver Menu]");
			System.out.println("1 - Right");
			System.out.println("2 - Left");
			System.out.println("3 - Top");
			System.out.println("4 - Bottom");
			System.out.println("0 - Quit");
			System.out.print("Which Maze Would You Like To Solve? ");
			int choice = CheckInput.checkIntRange(0, 4);
			
			int x = current.x;
			int y = current.y;
			
			if(choice == 1){
				if(array[x][y+1] != '*' && array[x][y+1] != '.'){
					if(array[x][y+1] == 'f'){
						System.out.println("[Finish Found]");
						break;
					}
					Point p = new Point(x,y+1);
					stack.push(p);
					array[x][y+1] = '.';
					current = p;
				}else{
					System.out.println("[Direction is Blocked]");
				}
			}
			else if(choice == 2){
				if(array[x][y-1] != '*' && array[x][y-1] != '.'){
					if(array[x][y-1] == 'f'){
						System.out.println("[Finish Found]");
						break;
					}
					Point p = new Point(x,y-1);
					stack.push(p);
					array[x][y-1] = '.';
					current = p;
				}else{
					System.out.println("[Direction is Blocked]");
				}
			}
			else if(choice == 3){
				if(array[x-1][y] != '*' && array[x-1][y] != '.'){
					if(array[x-1][y] == 'f'){
						System.out.println("[Finish Found]");
						break;
					}
					Point p = new Point(x-1,y);
					stack.push(p);
					array[x-1][y] = '.';
					current = p;
				}else{
					System.out.println("[Direction is Blocked]");
				}
			}
			else if(choice == 4){
				if(array[x+1][y] != '*' && array[x+1][y] != '.'){
					if(array[x+1][y] == 'f'){
						System.out.println("[Finish Found]");
						break;
					}
					Point p = new Point(x+1,y);
					stack.push(p);
					array[x+1][y] = '.';
					current = p;
				}else{
					System.out.println("[Direction is Blocked]");
				}
			}
			else if(choice == 0){
				mazeStackSolve(stack, array, stack.retData());
				break;
			}
			display(array);
		}
		
		
	}
	
	/**
	 * Solves maze using stacks
	 * @param stack empty stack of points
	 * @param array 2D maze array
	 * @param start starting point of maze
	 */
	public static void mazeStackSolve(LinkedStack stack, char [][] array, Point start){
		boolean found = false;
		stack.push(start);
		
		while(!found){
			
			if(array[stack.retData().x][stack.retData().y] != 'f'){
				
				int x = stack.retData().x;
				int y = stack.retData().y;
				array[x][y] = '.';
				
				stack.pop();
				
				if(array[x+1][y] != '*' && array[x+1][y] != '.'){
					Point p = new Point (x+1,y);
					stack.push(p);
				}
				if(array[x][y+1] != '*' && array[x][y+1] != '.'){
					Point p = new Point (x,y+1);
					stack.push(p);
				}
				if(array[x-1][y] != '*' && array[x-1][y] != '.'){
					Point p = new Point (x-1,y);
					stack.push(p);
				}
				if(array[x][y-1] != '*' && array[x][y-1] != '.'){
					Point p = new Point (x,y-1);
					stack.push(p);
				}
//				display(array);
			}
			else if(array[stack.retData().x][stack.retData().y] == 'f'){
				found = true;
				System.out.println("[Finish Found]");
				display(array);
			}
//			System.out.println("Stack: " + stack.retData());
		}
		
	}
	
	/**
	 * Solves maze using queue
	 * @param queue empty queue of points
	 * @param array 2D maze array
	 * @param start starting point of maze
	 */
	public static void mazeQueueSolve(LinkedQueue queue, char [][] array, Point start){
		boolean found = false;
		queue.add(start);
		
		while(!found){
			
			if(array[queue.retData().x][queue.retData().y] != 'f'){
				
				int x = queue.retData().x;
				int y = queue.retData().y;
				array[x][y] = '.';
				
				queue.remove();
				
				if(array[x+1][y] != '*' && array[x+1][y] != '.'){
					Point p = new Point (x+1,y);
					queue.add(p);
				}
				if(array[x][y+1] != '*' && array[x][y+1] != '.'){
					Point p = new Point (x,y+1);
					queue.add(p);
				}
				if(array[x-1][y] != '*' && array[x-1][y] != '.'){
					Point p = new Point (x-1,y);
					queue.add(p);
				}
				if(array[x][y-1] != '*' && array[x][y-1] != '.'){
					Point p = new Point (x,y-1);
					queue.add(p);
				}
//				display(array);
			}
			else if(array[queue.retData().x][queue.retData().y] == 'f'){
				found = true;
				System.out.println("[Finish Found]");
				display(array);
			}
//			System.out.println("Stack: " + stack.retData());
		}
		
	}
	

}
