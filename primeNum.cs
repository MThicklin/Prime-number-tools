using System;

namespace primeNum{
    class primeNum{
        public static void Main(){
            int num, i, ctr;
            int stNo = 2;
            int enNo = 10;

            for(num=stNo;num<=enNo;num++){
                ctr = 0;

                for(i=2;i<=num;i++){
                    if(num%i==0){
                        ctr++;
                        break;
                    }
                }
                if (ctr==0 && num!=1)
                    Console.Write("{0}", num);
            }
            Console.Write("\n");
        }
    }
}