public class collection2 {

	public collection2() {
		
	}
	public static void main (String[] args) {
		collection1 c1 = new collection1();
		c1.addItem("Pihll");
		c1.addItem("Pony");
		c1.addItem("Tracy");
		
		while (c1.hasNext()==true) {
			String surname=c1.getNext();
			String s1 = surname.substring(0,1);
			String s2= "P";
			if (s2.equals(s1)) {
				System.out.print(surname+"\n");
			}
		}
	}
}
