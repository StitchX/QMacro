package shangguigu.foundation.project2.util;

import java.util.Scanner;

/**4、
 * 工具类
 * 将不同的功能封装为方法，就是可以通过直接调用方法使用它的功能，而无需考虑具体地实现细节
 */

public class CMUtility {
    private static Scanner scanner = new Scanner(System.in);
    /**
     * 用于界面菜单的选择。改方法读取键盘，如果用户键入1-5中的任意字符，则方法返回。返回值为用户所选
     */
    public static char readMenuSelection(){
        char c;
        while (true){
            String str = readKeyBoard(1,false);
            c = str.charAt(0);
            if (c!='1'&&c!='2'&&c!='3'&&c!='4'&&c!='5'){
                System.out.println("选择错误，请重新输入：");
            }else break;
        }
        return c;
    }

    /**
     * 键盘读取一个字符，将其作为方法的返回值。
     * 如果用户不输入字符而直接回车，方法将以defaultValue 作为返回值
     * @param defaultValue
     */
    public static char readChar(char defaultValue){
        String str = readKeyBoard(1,true);
        return (str.length() == 0)? defaultValue:str.charAt(0);
    }

    /**
     * 从键盘读取一个长度不超过2位的整数，并将其作为方法的返回值
     */
    public static int readInt(){
        int n;
        for (;;){
            String str = readKeyBoard(2,false);
            try {
                n = Integer.parseInt(str);
                break;
            }catch(NumberFormatException e){
                System.out.println("数字输入错误，请重新输入");
            }
        }
        return n;
    }

    /**
     * 从键盘读取一个不超过limit的字符串，并将其作为方法的放回值。
     */
    public static String readString(int limit){
        return readKeyBoard(limit,false);
    }

    /**
     * 从键盘读取一个长度不超过Limit的字符串，并将其作为方法的返回值。
     * 如果用户不输入字符而直接回车，方法将以defaultvalue 作为返回值。
     */
    public static String readString(int limit,String defaultValue){
        String str = readKeyBoard(limit, true);
        return str.equals("")?defaultValue:str;
    }

    /**
     * 用于确认选择的输入，该方法从键盘读取‘Y’ ‘N'，并将其作为方法的返回值
     */
    public static char readConfirmSelection(){
        char c;
        for (;;){
            String str = readKeyBoard(1,false).toUpperCase();
            c=str.charAt(0);
            if (c == 'Y' || c=='N'){
                break;
            } else {
                System.out.println("选择错误，请重新输入：");
            }
        }
        return c;
    }

    private static String readKeyBoard(int limit,boolean blankReturn){
        String line = "";
        while (scanner.hasNextLine()){
            line = scanner.nextLine();
            if (line.length() == 0){   // 提供必填校验
                if (blankReturn) return line;
                else continue;
            }
            if (line.length()<1||line.length()>limit){   // 提供长度校验
                System.out.print("输入长度（不大于"+limit+")错误，请重新输入");
                continue;
            }
            break;
        }

        return line;
    }
}
