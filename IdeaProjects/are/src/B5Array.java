// 数组
public class B5Array {
    /*
    Java 语言中提供的数组是用来存储固定大小的同类型元素。
     */

//    数组作为参数
    public void arraydemo(int[] i){
        for (int j:i){
            System.out.println(j);
        }
    }

//    数组作为返回值
    public int[] arraydemo2(){
        int[] aa = new int[]{11,2,23,4,5,6};
        return aa;
    }

    public static void main(String[] args) {
//        声明
        double[] a1; // 首选的方法
        double a2[]; //Java中采用是为了让 C/C++ 程序员能够快速理解java语言

//        创建 和 赋值
        a1 = new double[10];
        a1[0]=1.0;
//        a1[10]=2.2;  //Index 10 out of bounds for length 10
        a2 = new double[]{1.2,3.4,5.6};

        int[] a3={1,2,6,4};

//        for增强
        for (double i :a2){
            System.out.println(i);
        }

//        数组作为函数 的 参数
        B5Array b5 = new B5Array();
        b5.arraydemo(new int[]{1,2,3,4,5,6,7});

//        数组作为函数的返回值
        System.out.println(b5.arraydemo2()[3]);
    }
}
