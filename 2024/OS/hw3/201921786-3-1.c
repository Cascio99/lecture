#include <stdio.h>
#include <stdlib.h>

#define PAGESIZE (32)
#define PAS_FRAMES (256)    //fit for unsigned char frame in PTE
#define PAS_SIZE (PAGESIZE*PAS_FRAMES)  //32*256 = 8192 B
#define VAS_PAGES (64)
#define VAS_SIZE (PAGESIZE*VAS_PAGES)   //32*64 = 2048 B
#define PTE_SIZE (4)    //sizeof(pte)
#define PAGETABLE_FRAMES (VAS_PAGES*PTE_SIZE/PAGESIZE)  //64*4/32 = 8 consecutive frames

#define PAGE_INVALID (0)
#define PAGE_VALID (1)
#define MAX_REFERENCES (256)

typedef struct{
    unsigned char frame;    //allocated frame
    unsigned char vflag;    //valid-invalid bit
    unsigned char ref;      //reference bit
    unsigned char pad;      //padding
} pte;  //Page Table Entry (total 4 Bytes, always)
typedef struct{
    int pid;
    int ref_len;    //Less than 255
    unsigned char *references;
} process_raw;
typedef struct{
    unsigned char b[PAGESIZE];
} frame;
typedef struct{
    unsigned char page;
} access_unit;
//별도의 구조체 필요? PT: PTE 정의하여 사용 --> PAS에서 저장&관리 ==> 3-1에서 필요 없었음
// typedef struct{
//     pte entries[VAS_PAGES];
// } PageTable;
typedef struct{
    int F;  //Frames
    int PF; //Page-Faults
    int REF;//Reference-Count
} ps_result;

int num_ps = 0;     //number of loaded process
int frame_number = 0;
ps_result res[10];
process_raw procs[10]; //max: 10
frame *pas;

void load_process(){
    // printf("load_process() start\n");
    process_raw ps;
    int size = 2*sizeof(int);
    while(fread(&ps, size, 1, stdin) == 1){
        procs[num_ps].pid = ps.pid;
        procs[num_ps].ref_len = ps.ref_len;
        procs[num_ps].references = (unsigned char*) malloc(sizeof(unsigned char) * procs[num_ps].ref_len);
        // printf("%d %d\n", procs[num_ps].pid, procs[num_ps].ref_len);
        access_unit seq;
        for(int i=0; i<procs[num_ps].ref_len; i++){
            if(fread(&seq, sizeof(seq), 1, stdin) == 1){
                procs[num_ps].references[i] = seq.page;
                // printf("%02d ", procs[num_ps].references[i]);
            }
        }
        // printf("\n");
        num_ps++;
    }
    // printf("load_process() end\n");
}

void Start(){
    /*1 frame = 8 PTEs  (page frame size = 32 B, PTE_SIZE = 4 B)*/
    //ps#1: pte* cur_pte = (pte*) &pas[8]
    //typecast PAS into PTEs: frames -> PTEs
    //Address-Translation: frame_number = 8*i + procs[i].ref[j]/8, cur_pte_idx = procs[i].ref[j]%8
    // printf("Start() start\n");
    frame_number += num_ps*PAGETABLE_FRAMES;    //PT: 연속된 frame 8개 할당
    for(int i=0; i<num_ps; i++){
        res[i].F += PAGETABLE_FRAMES;
    }
    for(int j=0; j<MAX_REFERENCES; j++){
        for(int i=0; i<num_ps; i++){
            if(j>=procs[i].ref_len) continue;   //skip finished_process
            pte* cur_pte = (pte*) &pas[PAGETABLE_FRAMES*i + procs[i].references[j]/PAGETABLE_FRAMES];
            int idx = procs[i].references[j]%PAGETABLE_FRAMES;
            // printf("[PID %02d REF:%03d] Page access %03d: ", procs[i].pid, res[i].REF, procs[i].references[j]);
            if(cur_pte[idx].vflag == PAGE_INVALID){ //Page-Fault
                if(frame_number==PAS_FRAMES){       //OutOfMemory
                    if(cur_pte[idx].vflag == PAGE_INVALID){
                        printf("Out of memory!!\n");
                        return;
                    }
                }
                // printf("PF, Allocated ");
                res[i].F++;
                res[i].PF++;
                cur_pte[idx].frame = frame_number++;    //allocate new frame
                cur_pte[idx].vflag = PAGE_VALID;        //update PT
            }
            // printf("Frame %03d\n", cur_pte[idx].frame);
            res[i].REF++;
            cur_pte[idx].ref++;
        }
    }
    // printf("Start() end\n");
}
void print_all(){
    int tot_F=0, tot_PF=0, tot_REF=0;
    for(int i=0; i<num_ps; i++){
        printf("** Process %03d: Allocated Frames=%03d PageFaults/References=%03d/%03d\n", procs[i].pid, res[i].F, res[i].PF, res[i].REF);
        tot_F += res[i].F;
        tot_PF += res[i].PF;
        tot_REF += res[i].REF;
        for(int j=0; j<VAS_PAGES; j++){
            pte* cur_pte = (pte*) &pas[PAGETABLE_FRAMES*i + j/PAGETABLE_FRAMES];
            int idx = j%PAGETABLE_FRAMES;
            if(cur_pte[idx].vflag == PAGE_INVALID) continue;
            printf("%03d -> %03d REF=%03d\n", j, cur_pte[idx].frame, cur_pte[idx].ref);
        }
    }
    printf("Total: Allocated Frames=%03d Page Faults/References=%03d/%03d\n", tot_F, tot_PF, tot_REF);
}
int main(int argc, char* argv[]){
    pas = (frame*)malloc(PAS_SIZE);  //실제 메모리 할당
    
    load_process();
    Start();
    print_all();    //print all PT's info(valid only PTEs)

    for(int i=0; i<num_ps; i++){
        free(procs[i].references);
    }
    free(pas);
    return 0;
}