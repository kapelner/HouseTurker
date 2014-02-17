package HouseTurkerLoader;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.util.LinkedHashMap;
import java.util.Map;

public class WordDictionary {
  private LinkedHashMap<String, Integer> dict;
  private String word;
  private int counter;

  public WordDictionary(String inputfile) throws IOException {
    dict = new LinkedHashMap<String, Integer>();
    WordScanner s = new WordScanner(new FileReader(inputfile));
    add(s);
  }

  private void add(WordScanner s) {
    while (s.hasNext() && s != null) {
      word = s.next();
      if (!dict.containsKey(word) && word != "" && word != " ") {
        dict.put(word, new Integer(counter));
        counter++;
      }
    }
  }

  public void printString() {
    for (Map.Entry<String, Integer> entry : dict.entrySet()) {
      System.out.println("Key = " + entry.getKey() + ", Value = "
          + entry.getValue());
    }
  }

  public int getSize() {
    return dict.size();
  }

  public int getValue(String word) {
    return dict.get(word);
  }

  public boolean contains(String w) {
    return dict.containsKey(w);
  }

  public void write() throws FileNotFoundException,
      UnsupportedEncodingException {
    PrintWriter writer = new PrintWriter("dictmap.txt", "UTF-8");
    for (Map.Entry<String, Integer> entry : dict.entrySet()) {
      writer.write("Key = " + entry.getKey() + ", Value = " + entry.getValue()
          + "\n");
    }
    writer.close();
  }
}
