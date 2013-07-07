import java.io.*;
import java.util.ArrayList;

public class Palindromes {
	
	public static void main(String[] args) throws IOException{
		
		BufferedReader reader = new BufferedReader(new FileReader("../palindromesTWO.tsv"));
		ArrayList<String> arr = new ArrayList<String>();
		String line = null;
		boolean flag = true;
		
		while((line = reader.readLine()) != null) {
			
			String temp, reverse;
			
			for(int i = 0; i < line.length() - 4; i++){
				for(int k = 4; k < line.length(); k++){
					temp = line.substring(i, k);
					reverse = new StringBuilder(temp).reverse().toString();
					if(temp.equals(reverse)){
						arr.add(temp);				
					}
				}
			}
			
		}
		
		System.out.print(arr);
				
	}

}
