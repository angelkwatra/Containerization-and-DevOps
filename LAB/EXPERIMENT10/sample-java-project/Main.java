public class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 0;
        // BUG: Division by zero
        int c = a / b;

        // Unused variable
        int unusedVar = 42;

        // Hardcoded password
        String dbPassword = "super_secret_password";

        System.out.println("Result: " + c);
    }
}