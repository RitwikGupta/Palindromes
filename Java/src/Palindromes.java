import java.io.*;

public class Palindromes {
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader reader = new BufferedReader(new FileReader("../palindromesTWO.tsv"));
		String line = null;
		
		while((line = reader.readLine()) != null) {
			
			System.out.println(line);
			
		}
				
	}

}
