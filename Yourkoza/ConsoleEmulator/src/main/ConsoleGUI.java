package main;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Image;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import javax.imageio.ImageIO;
import javax.swing.JFrame;

public class ConsoleGUI extends JFrame {
	private static final long serialVersionUID = 1L;
	private static Image icon;
	private static final Map<String, InputProcessor> commandMap = new HashMap<String, InputProcessor>(10); //hashmap to store commands
	
	public static void main(String[] args) {
		//STEP 1: Initialize and define all commands, in the form of InputProcessors.
		InputProcessor clearScreen = new InputProcessor() {
			public void process(String[] args, Console console) {
				console.cls();
			}
		};
		
		InputProcessor terminateProgram = new InputProcessor() {
            public void process(String[] args, Console console) {
                System.exit(0);
            }
        };
        
        InputProcessor echo = new InputProcessor() {
            public void process(String[] args, Console console) {
                console.write(args[1]); // only echos the first word...
                console.write("\n");
            }
        };
        
        InputProcessor IDontUnderstand = new InputProcessor() {
            public void process(String[] args, Console console) {
                console.write("Sorry, I don't understand that command\n");
            }
        };
        
        //STEP 2: Link all of these command codes to a one-word String command:
        commandMap.put("cls",clearScreen); //String command does not need to match variable name from above
        
        commandMap.put("close",terminateProgram);
        /*Multiple strings can be used for the same command, but multiple
         * commands may not be referenced by the same string.
         */
        commandMap.put("exit",terminateProgram);
        
        commandMap.put("echo",echo); //String command COULD be the same as the variable name, if you want.
        
        commandMap.put("help",IDontUnderstand);
		
        //STEP 3: Initialize the JFrame:
        JFrame consoleFrame = new JFrame("Console");
    	Image loadedIcon = null;
    		try {
    			File imageFile = new File("terminal.png");
    			if (!imageFile.exists()) {
    				throw new FileNotFoundException("Image file not found: " + imageFile.getAbsolutePath());
    			}
    			
    			loadedIcon = ImageIO.read(new File("./terminal.png"));
    		} catch (IOException e) {
    			System.err.println("Error loading icon: " + e.getMessage());
    		}
    		
    		icon = loadedIcon;

        consoleFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		/*Official Windows Command Prompt size, looks beautiful and can be resized
		 * after being opened if you so desire.
		 */
        consoleFrame.setSize(677, 343);
		
		//Init console
		Console console = new Console(Color.BLACK, Color.YELLOW, new Font(Font.MONOSPACED, Font.BOLD, 14), "$ ");
		console.setPreferredSize(new Dimension(677, 343)); // Same as above
		console.setCompletionSource(new DefaultCompSource("help", "echo", "cls", "close","exit")); //String commands go here as well
		/*This processor breaks a statement into args and passes them to the matching
		 * command defined in the hashmap above (the part in step 2)
		 */
		console.setProcessor(new InputProcessor() {
			private int requests = 0;
			
			public void process(String[] args, Console console)
            {
                //1. Print for debugging:
                System.out.println("Got Req. " + ++requests + ": '" + args[0] + "'");
                
                System.out.println("asked: " + Arrays.toString(args));
                //4. Process list of arguments
                if (args.length > 0 && commandMap.containsKey(args[0].toLowerCase()))
                    commandMap.get(args[0].toLowerCase()).process(args, console);
                else
                    commandMap.get("help").process(args, console);
            }
		});
		
		consoleFrame.setIconImage(icon);
		consoleFrame.add(console);
		consoleFrame.addComponentListener(console);
		consoleFrame.pack();
        console.setScreenHeight((int) consoleFrame.getContentPane().getSize().getHeight());
        consoleFrame.setVisible(true);
	}
	
	public static String removeQuotes(String arg) {
        return arg.substring(1,arg.length()-1);
    }
}