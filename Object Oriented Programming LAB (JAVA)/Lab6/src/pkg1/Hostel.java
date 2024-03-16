package pkg1;
import pkg2.SRA;
public class Hostel {
	public SRA[] sras = new SRA[10];
	int i = 0;
	public String name;
	public Hostel(String n){
		name = n;
	}
	public String sra_list() {
		String s = new String();
		int i = 0;
		while (i < sras.length && sras[i] != null) {
			s += sras[i];
			i++;
		}
		return s;
	}
	public String toString() {
		return "Hostel name: " + name + "\nSRAs: " + sra_list();
	}
	public void add_sra(String s) {
		if (i >= 9) {
			System.out.println("Maximum capacity reached");
			return;
		}
		sras[i] = new SRA(s);
		i++;
	}
}