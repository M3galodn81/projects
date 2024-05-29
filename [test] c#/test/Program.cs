using System;
 
namespace HelloWorld
{
    public abstract class Shape{
        public int height, width;

        public Shape(int height,int width){
            this.height = height;
            this.width = width;
        }
        
        public abstract double Calculate();
        public virtual String PrintFormula(){
            return "This shape has no specific formula.";
        }
    }
 
 
    public class Circle : Shape{
        public int radius;
        public double pi, circumference;
 
        public override double Calculate(){
            return 2 * pi * radius;
        }

        public override string PrintFormula(){
            return "2 * π * r";
        }
 
        public Circle(int radius): base (0,0) {
 
            this.radius = radius;
            pi = 3.1415;
        }
    }
 
    public class Rectangle : Shape {
        public int rectPerimeter;
 
        public override double Calculate(){
            return height * 2 + width * 2;
        }

        public override string PrintFormula()
        {
            return "2h + 2w";
        }

        public Rectangle(int height,int width): base (height,width){
            this.height = height;
            this.width = width;
 
        }
    }
 
    public class Square : Shape {
        public int area;
 
        public override double Calculate(){
            return height * width;
        }

        public override string PrintFormula()
        {
            return "s ^ 2";
        }

        public Square(int height,int width): base (height,width){
            this.height = height;
            this.width = width;
 
        }
    }
 
    public class Triangle : Shape {
        public int triArea;
 
        public override double Calculate(){
            return height * width / 2;
        }

        public override string PrintFormula()
        {
            return " (h * w) /2" ;
        }

        public Triangle(int height,int width): base (height,width){
            this.height = height;
            this.width = width;
 
        }
    }
 
 
    public class Program {
        public static void Main(string[] args) {
            int inputHeight, inputWidth, inputRadius;

            Console.WriteLine("Enter the height:");
            inputHeight = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter the width:");
            inputWidth = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter the radius:");
            inputRadius = int.Parse(Console.ReadLine());

 
            Circle testCircle = new Circle (inputRadius);
            Rectangle testRectangle = new Rectangle (inputHeight,inputWidth);
            Square testSquare = new Square (inputHeight,inputWidth);
            Triangle testTriangle = new Triangle (inputHeight,inputWidth);
 
            Console.WriteLine("====================================================================");
            Console.WriteLine("Formula of circumference of a circle: " + testCircle.PrintFormula());
            Console.WriteLine("Circumference of a circle is : " + testCircle.Calculate());
            Console.WriteLine("====================================================================");
            Console.WriteLine("Formula of perimeter of a rectangle: " + testRectangle.PrintFormula());
            Console.WriteLine("Perimeter of a rectangle is : " + testRectangle.Calculate());
            Console.WriteLine("====================================================================");
            Console.WriteLine("Formula of area of a square is : " + testSquare.PrintFormula());
            Console.WriteLine("Area of a square is : " + testSquare.Calculate());
            Console.WriteLine("====================================================================");
            Console.WriteLine("Formula of area of a triangle is : " + testTriangle.PrintFormula());
            Console.WriteLine("Area of a triangle is : " + testTriangle.Calculate());
            Console.WriteLine("====================================================================");
              
        }
    }
}