import java.io.*;

public class CompulsoryQuestion {
    public static void main (String[] args)throws IOException {
        File d = new File("NewDirectory");
        if (!d.exists()) {
            d.mkdir();
        }
        System.out.println("Directory created");
        File f = new File("filename.txt");
        if (!f.exists()){
            f.createNewFile();
        }
        System.out.println("File created");
        System.out.println(f.getAbsolutePath());
        //renaming a file
        File f2 = new File("newfile.txt");
        System.out.println("File renamed");
        f.renameTo(f2);
        f.delete();//delete old file
        System.out.println("Old file deleted");
        
        boolean empty = true;
        for (File l: d.listFiles()) {
            empty = false;
            System.out.println(l);
        }
        if (empty) {
            System.out.println("The diretory is empty.");
        }		
	}
}