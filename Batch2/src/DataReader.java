import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Reader;
import java.io.UnsupportedEncodingException;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.HashMap;
import java.util.Map;
import java.util.NoSuchElementException;

public class DataReader {
	private Reader r;
	private WordDictionary d;
	private LinkedHashMap<int[], Integer> m;
	private int c;
	private final int size;
	private HashSet<String> temps;
	private int[] arr;
	private int counter;

	public DataReader(Reader r, WordDictionary d) throws IOException {
		BufferedReader x = new BufferedReader(r);
		this.r = x;
		this.d = d;
		m = new LinkedHashMap<int[], Integer>();
		c = r.read();
		size = d.getSize();
		arr = new int[size];
		temps = new HashSet<String>();
	}

	// this method does nothing if the end of file or a space is reached
	// this method will keep reading until it reaches the first valid character
	private void skipBadChar() throws IOException {
		while (!isValid()) {
			if (c == -1 || isSpace() || shouldStop()) {
				return;
			}
			c = r.read();
		}
	}

	// checks if the current character is a space
	private boolean isSpace() {
		return (char) c == ' ';
	}

	// checks if there are anymore words in the file to read
	public boolean hasNext() {
		return c != -1;
	}

	public boolean shouldStop() {
		return c == 94;
	}

	// checks if the current character is "valid", 39 is apostrophe
	private boolean isValid() {
		return Character.isLetter(c);
	}

	public String next() {
		try {
			// creates a new word
			String word = "";
			// while the characters are valid, concatenate to string
			// stops when a space is reached
			while (isValid()) {
				if (isSpace()) {
					break;
				} else {
					skipBadChar();
				}
				word += (char) c;
				// System.out.println(word + " is the word");
				c = r.read();
			}
			// if the word is empty, call the method again after skipping the
			// current char

			if (shouldStop()) {
				return word.toLowerCase();
			} else if (word.equals("") && hasNext()) {
				// System.out.println(c + " is value of c and ");
				c = r.read();
				return next();
			} else {
				// adds the word in lowercase
				return word.toLowerCase();
			}
		} catch (IOException e) {
			throw new NoSuchElementException();
		}
	}

	// reads a description, adding all the words in a temporary set
	public void readDescription() throws IOException {
		while (!shouldStop()) {
			String word = next();
			if (word != "") {
				// System.out.println(word);
				temps.add(word);
			}
		}
		c = r.read();
	}

	// reads the answer key, which is 1 if the answer is A, and 0 or the answer
	// is B
	private int getAnswer() throws IOException {
		String w = next();
		while (w.equals("")) {
			w = next();
		}
		// System.out.println(w + " is the answer key");
		c = r.read();
		if (w.equals("a")) {
			return 1;
		} else {
			return 0;
		}
	}

	public void readSet() throws IOException {
		// resets the temporary set that contains the words in 1 description
		temps = new HashSet<String>();
		readDescription();
		// adds the words in the temporary set to the temp array
		for (String w : temps) {
			int v = d.getValue(w);
			arr[v]++;
		}
		temps = new HashSet<String>();
		readDescription();
		// does the same thing above, except since this is the second
		// description, subtract 1 from array
		for (String w : temps) {
			int v = d.getValue(w);
			arr[v]--;
		}
		// get the answer value
		int a = getAnswer();
		// put the array (x values) and the answer key (y value) into the map
		m.put(arr, new Integer(a));
		// resets the array
		arr = new int[size];
	}

	// function call to read the data file
	public void readData() throws IOException {
		// as long as there are stuff left, keep reading by sets, which are
		// pairs of description + answer
		while (hasNext()) {
			System.out.println("counter is " + counter);
			counter++;
			readSet();
		}
	}

	public void print() {
		for (Map.Entry<int[], Integer> entry : m.entrySet()) {
			for (int i = 0; i < entry.getKey().length; i++) {
				System.out.print(entry.getKey()[i] + " ");
			}
			System.out.print("\n" + " the value is " + entry.getValue());
			System.out.println();
			System.out.println();
		}
	}
	
	public void write() throws FileNotFoundException, UnsupportedEncodingException {
		PrintWriter writer = new PrintWriter("data_p2.txt", "UTF-8");
		for (Map.Entry<int[], Integer> entry : m.entrySet()) {
			writer.write(entry.getValue() + " " + "\n");
			for (int i = 0; i < entry.getKey().length; i++) {
				writer.write(entry.getKey()[i] + " ");
			}
			writer.write("\n");
		}
	}
}
