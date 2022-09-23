import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int s_hour = sc.nextInt();
		int s_minute = sc.nextInt();
        int minutes = sc.nextInt();
        
        if (minutes+s_minute > 59){
            s_hour += (minutes+s_minute)/60;
            s_minute = (minutes+s_minute)%60;
        }else {
            s_minute += minutes;
        }
        if (s_hour>23){
            s_hour = s_hour%24;
        }
        
		System.out.printf("%d %d",s_hour,s_minute);
	}
}