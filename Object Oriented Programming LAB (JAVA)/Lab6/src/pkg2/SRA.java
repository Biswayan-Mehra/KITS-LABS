package pkg2;

public class SRA{
	public String name;
	Student students[] = new Student[6];
	int i = 0;
	public SRA(String n){
		name = n;
	}
	public String toString() {
		return name;
	}
	public void assign_student(String name, String reg) {
		if (i >= 5) {
			System.out.println("Maximum capacity reached");
			return;
		}
		students[i] = new Student(name, reg);
		i++;
	}
	public String view_students() {
		String s = new String();
		for (Student st: students) {
			if (st != null)
				s += "\n" + st;
		}
		return s;
	}
}