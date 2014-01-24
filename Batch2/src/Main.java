import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;

public class Main {
	
	public static void main(String[] args) throws IOException {
		WordDictionary dict = new WordDictionary(args[0]);
		dict.printString();
		dict.write();
	}
}
