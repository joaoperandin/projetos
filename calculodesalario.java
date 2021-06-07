import java.util.Scanner;

class Main {  
  public static void main(String args[]) {
    
    Scanner ler = new Scanner(System.in);
    
    System.out.printf("Insira o número do funcionário:\n");
    int numeroDoFuncionario = ler.nextInt();
        
    System.out.printf("Agora, insira a quantidade de horas trabalhadas:\n");
    int horasTrabalhadas = ler.nextInt();
    
    System.out.printf("Para finalizar, insira o valor da hora trabalhada:\n");
    double valorHora = ler.nextDouble();
    
    double salario = valorHora * horasTrabalhadas;

    System.out.printf("O funcionário número " + numeroDoFuncionario + " recebe " + salario + " por mês."); 
  
  } 
}
