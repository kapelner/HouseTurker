package HouseTurkerLoader;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Reader;
import java.io.UnsupportedEncodingException;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class WordScanner implements Iterator<String>{
	// c is an integer that is read from the file, -1 if there is no more to
	// read
	private Reader r;
	private int c;

	public WordScanner(Reader initR) throws IOException {
		this.r = initR;
		c = r.read();
		skipBadChar();
	}

	// this method does nothing if the end of file or a space is reached
	// this method will keep reading until it reaches the first valid character
	private void skipBadChar() throws IOException {
		while (!isValid()) {
			if (c == -1 || isSpace()) {
				return;
			}
			c = r.read();
		}
	}

	// checks if the current character is "valid", 39 is apostrophe
	private boolean isValid() {
		return Character.isLetter(c);
	}

	// checks if the current character is a space
	private boolean isSpace() {
		return (char) c == ' ';
	}

	// checks if there are anymore words in the file to read
	@Override
	public boolean hasNext() {
		return c != -1;
	}

	// returns the next valid word
	@Override
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
			// if the word is empty, call the method again after skipping the current char
			if (word.equals("") && hasNext()) {
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

	@Override
	public void remove() {
		throw new UnsupportedOperationException();
	}

}
