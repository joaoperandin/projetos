import java.util.Scanner;

class Main {  
  public static void main(String args[]) { 
    
	  Scanner ler = new Scanner(System.in);

    System.out.printf("Insira os valores de X e Y para saber onde eles estão no plano cartesiano:\n");

    System.out.printf("Insira o valor de X: ");
    double x = ler.nextDouble();
    System.out.printf("Insira o valor de Y: ");
    double y = ler.nextDouble();

    if (x > 0 && y > 0) {

     System.out.printf("O ponto está no Q1.");
      
    }

    else if (x < 0 && y > 0) {

      System.out.printf("O ponto está no Q2.");
    
    }
    else if (x < 0 && y < 0) {

      System.out.printf("O ponto está no Q3.");
    
    }

    else if (x > 0 && y < 0) {

      System.out.printf("O ponto está no Q4.");
    
    }
      else if (x == 0 && y == 0) {

      System.out.printf("O ponto está na origem.");
    
    }
      else if (x < 0 || x > 0 && y == 0) {

      System.out.printf("O ponto está no eixo X.");
    
    }
      else if (y < 0 || y > 0 && x == 0) {

      System.out.printf("O ponto está no eixo Y.");
    
    }
      else {

     System.out.printf("Valor(es) inválido(s)");
    }
		
  } 
}
