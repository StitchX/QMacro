package shangguigu.foundation;
/*
this关键字的使用：
    1、this可以用来修饰/调用：属性、方法、构造器
    2、修饰属性和方法
        this理解为：当前对象 或 当前正在创建的对象

    2.1、在类的方法中，我们可以使用this.属性 或 this.方法 的方式，调用当前对象属性或方法。但是
       通常情况下，我们都选择省略 this. 。特殊情况下，如果方法的形参和类的属性同名时，我们必须显示
       的使用 this.变量 的方式，表明此变量是属性，而非形参。
    2.2、在类的构造器中，我们可以使用this.属性 或 this.方法 的方式，调用当前对象属性或方法。但是
       通常情况下，我们都选择省略 this. 。特殊情况下，如果方法的形参和类的属性同名时，我们必须显示
       的使用 this.变量 的方式，表明此变量是属性，而非形参。
    3、this调用的构造器
     1）我们在类的构造器中，可以显示的使用“this（形参列表）”的方式，调用本类中指定的其他构造器
     2）构造器中不能通过“this(形参列表)”调用自己
     3）如果一个类中有n个构造器，则最多有n-1构造器中使用了“this(形参列表)”
     4）规定：“this(形参列表)”必须声明在当前构造器的首行
     5）构造器内部，最多只能声明一个“this(形参列表)”，用来调用其他的构造器

 */
public class AM4This {

    int age;
    private double ss;
    public AM4This(int age){
        this.age = age; // 就近原则
    }

    public AM4This(){
        this.eat();
        System.out.println('1');
    }

    public AM4This(double b){
        this();  // 唯一且首行
        System.out.println("调用构造器");
    }

    public void eat(){
        this.age = 19;
        this.drink();
        System.out.println("调用方法");
    }

    public void drink(){
        System.out.println("调用属性");
    }
}
