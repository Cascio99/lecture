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
typedef struct{
    int F;  //Frames
    int PF; //Page-Faults
    int REF;//Reference-Count
} report;

int num_ps = 0;         //number of loaded process
process_raw procs[10];  //max: 10
frame *pas;
int frame_number = 0;   //frame-cursor for "new PT or user-data" in PAS
report res[10];

void load_process(){    //include allocating L1PT for all process
    // printf("load_process() start\n");
    process_raw ps;
    int size = 2*sizeof(int);
    while(fread(&ps, size, 1, stdin) == 1){
        procs[num_ps].pid = ps.pid;
        procs[num_ps].ref_len = ps.ref_len;
        procs[num_ps].references = (unsigned char*) malloc(sizeof(unsigned char) * procs[num_ps].ref_len);
        // printf("%d %d\n", procs[num_ps].pid, procs[num_ps].ref_len);
        
        //allocate new frame(of PAS) for L1PT
        // pte* cur_pte = (pte*) &pas[frame_number++];  //warning: unused variable. useless code
        frame_number++;
        res[num_ps].F++;
        
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

void Start(){   //On-demand_Paging of L1PT->L2PT & L2PT->PAS
    /*==================AT_v2(3-2)==================*/
    /*ps#0: frame#0{8 PTEs}, ps#1: frame#1, ...*/
    /*in L2PT ==> 0th PTE: page#0~7, 1st PTE: page#8~15, ...*/
    //L1PT: idx(i) -> frame(cur_pte[idx].frame) {w. invalid->valid}
    //L2PT: page(procs[i].ref[j]) -> frame(cur_pte[idx].frame) {w. ref_cnt++}
    //L1PT: frame_number = i, cur_pte_idx = procs[i].ref[j]/8
    //L2PT: frame_number = L1PT's output-frame#, cur_pte_idx = procs[i].ref[j]%8
    // printf("Start() start\n");
    for(int j=0; j<MAX_REFERENCES; j++){
        for(int i=0; i<num_ps; i++){
            if(j>=procs[i].ref_len) continue;   //skip finished_process
            //OutOfMemory --> complicated to handle here?!!!
            /*if(frame_number==PAS_FRAMES){
                pte* cur_pte = (pte*) &pas[i];  //AT
                int idx = procs[i].references[j]/PAGETABLE_FRAMES;
                if(cur_pte[idx].vflag == PAGE_INVALID){ //check access to invalid "L2PT"
                    printf("Out of memory!!\n");
                    return;
                }
                int frame_num = cur_pte[idx].frame;
                cur_pte = (pte*) &pas[frame_num];
                idx = procs[i].references[j]%PAGETABLE_FRAMES;
                if(cur_pte[idx].vflag == PAGE_INVALID){
                    printf("Out of memory!!\n");
                    return;
                }
            }//escape OOM: restore index of L1PT*/
            pte* cur_pte = (pte*) &pas[i];  //AT
            int idx = procs[i].references[j]/PAGETABLE_FRAMES;
            // printf("[PID %02d REF:%03d] Page access %03d: ",procs[i].pid, res[i].REF, procs[i].references[j]);
            //L1PT: idx->frame
            // printf("(L1PT) ");
            if(cur_pte[idx].vflag == PAGE_INVALID){ //Page-Fault
                if(frame_number == PAS_FRAMES){     //OOM: can't make "L2PT"
                    printf("Out of memory!!\n");
                    return;
                }
                // printf("PF, Allocated Frame %03d -> %03d, ", idx, frame_number);
                cur_pte[idx].frame = frame_number++;    //allocate new frame for L2PT(logically "page" in L2)
                cur_pte[idx].vflag = PAGE_VALID;        //update PT
                res[i].F++;
                res[i].PF++;
            }
            // else{  //not PF
            //     // printf("Frame %03d, ", cur_pte[idx].frame);
            // }
            int frame_num = cur_pte[idx].frame; //L2PT's frame# in PAS

            //L2PT: page->frame
            // printf("(L2PT) ");
            cur_pte = (pte*) &pas[frame_num];    //AT: update frame-cursor(allocated frame for L2PT)
            idx = procs[i].references[j]%PAGETABLE_FRAMES;
            if(cur_pte[idx].vflag == PAGE_INVALID){ //Page-Fault
                if(frame_number == PAS_FRAMES){     //OOM: can't allocate new frame for "user-data"
                    printf("Out of memory!!\n");
                    return;
                }
                // printf("PF, Allocated ");
                cur_pte[idx].frame = frame_number++;    //allocate new frame for user-data: move PAS_frame-cursor here
                cur_pte[idx].vflag = PAGE_VALID;        //update PT
                res[i].F++;
                res[i].PF++;
            }
            // printf("Frame %03d\n", cur_pte[idx].frame);
            cur_pte[idx].ref++;
            res[i].REF++;
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
        for(int j=0; j<PAGETABLE_FRAMES; j++){   //L1PT has 8 PTEs: j==index of L1PT
            pte* cur_pte = (pte*) &pas[i];      //L1PT로 이동(반복문 밖에 둬서 출력 틀렸었음)
            if(cur_pte[j].vflag == PAGE_INVALID) continue;  //only check valid PTEs
            printf("(L1PT) %03d -> %03d\n", j, cur_pte[j].frame);
            int frame_num = cur_pte[j].frame; //frame# of L2PT
            cur_pte = (pte*) &pas[frame_num];
            for(int k=0; k<PAGETABLE_FRAMES; k++){//L2PT also has 8 PTEs for specific L1PT's 1 PTE(demand-paging)
                if(cur_pte[k].vflag == PAGE_INVALID) continue;
                printf("(L2PT) %03d -> %03d REF=%03d\n", j*PAGETABLE_FRAMES+k, cur_pte[k].frame, cur_pte[k].ref);
            }
        }
    }
    printf("Total: Allocated Frames=%03d Page Faults/References=%03d/%03d\n", tot_F, tot_PF, tot_REF);
}

int main(int argc, char* argv[]){
    pas = (frame*)malloc(PAS_SIZE);
    
    load_process();
    Start();
    print_all();    //print all valid-PTEs' info

    for(int i=0; i<num_ps; i++){
        free(procs[i].references);
    }
    free(pas);
    return 0;
}