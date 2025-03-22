#include <stdio.h>
#include <stdlib.h>

typedef struct{
    unsigned char op;
    unsigned char len;
} code_tuple;

typedef struct{
    int pid;
    int arrival_time;
    int code_bytes;
} process;

int main(int argc,char* argv[]){
    process ps;
    code_tuple ct;

    while(fread(&ps, sizeof(process), 1, stdin) == 1){
        fprintf(stdout, "%d %d %d\n", ps.pid, ps.arrival_time, ps.code_bytes);
        // read code: op, len
        for(int i=0; i<ps.code_bytes/2; i++){
            if(fread(&ct, sizeof(code_tuple), 1, stdin) == 1){
                fprintf(stdout, "%d %d\n", ct.op, ct.len);
            }
        }
    }

    return 0;
}