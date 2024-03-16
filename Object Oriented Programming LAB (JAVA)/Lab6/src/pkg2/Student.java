package pkg2;

public class Student {
	String name, reg_no;
	Student(String n, String reg){
		name = n;
		reg_no = reg;
	}
	public String toString() {
		return "Name: " + name + "\nRegister number: "+reg_no;
	}
}