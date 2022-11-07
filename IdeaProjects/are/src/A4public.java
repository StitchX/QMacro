// 访问修饰符
public class A4public {
    //    访问修饰符 关键字 返回类型 方法名 String类型 字符串数组
    public static void main(String[] args) {

    }
    /*
    修饰符用来定义类、方法或者变量
    Java语言提供了很多修饰符，主要分为以下两类：
        访问修饰符:当前类、同一包内、子孙类(同一包)、子孙类(不同包)、其他包
            default (即默认，什么也不写）: 在同一包内可见，不使用任何修饰符。使用对象：类、接口、变量、方法。不能：子孙类(不同包)、其他包
            private : 在同一类内可见。使用对象：变量、方法。
                    -----------------注意：不能修饰类（外部类） 注意：不能修饰类（外部类）
            public : 对所有类可见。使用对象：类、接口、变量、方法
            protected : 对同一包内的类和所有子类可见。使用对象：变量、方法。
                        ------------ 注意：不能修饰类（外部类）。不能：与default对比
        非访问修饰符

     */
}