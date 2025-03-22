#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <limits.h>

#define offsetof(TYPE, MEMBER) ((size_t) &((TYPE *)0)->MEMBER)

#define container_of(ptr, type, member) ({                      \
        const typeof( ((type *)0)->member ) *__mptr = (ptr);    \
        (type *)( (char *)__mptr - offsetof(type,member) );})

#define LIST_POISON1  ((void *) 0x00100100)
#define LIST_POISON2  ((void *) 0x00200200)

struct list_head {
	struct list_head *next, *prev;
};

#define LIST_HEAD_INIT(name) { &(name), &(name) }

#define LIST_HEAD(name) \
	struct list_head name = LIST_HEAD_INIT(name)

#define INIT_LIST_HEAD(ptr) do { \
	(ptr)->next = (ptr); (ptr)->prev = (ptr); \
} while (0)

static inline void __list_add(struct list_head *new,
			      struct list_head *prev,
			      struct list_head *next) {
	next->prev = new;
	new->next = next;
	new->prev = prev;
	prev->next = new;
}

static inline void list_add(struct list_head *new, struct list_head *head) {
	__list_add(new, head, head->next);
}

static inline void list_add_tail(struct list_head *new, struct list_head *head) {
	__list_add(new, head->prev, head);
}

static inline void __list_del(struct list_head * prev, struct list_head * next) {
	next->prev = prev;
	prev->next = next;
}

static inline void list_del(struct list_head *entry) {
	__list_del(entry->prev, entry->next);
	entry->next = LIST_POISON1;
	entry->prev = LIST_POISON2;
}

static inline void list_del_init(struct list_head *entry) {
	__list_del(entry->prev, entry->next);
	INIT_LIST_HEAD(entry);
}

static inline void list_move(struct list_head *list, struct list_head *head) {
        __list_del(list->prev, list->next);
        list_add(list, head);
}

static inline void list_move_tail(struct list_head *list,
				  struct list_head *head) {
        __list_del(list->prev, list->next);
        list_add_tail(list, head);
}

static inline int list_empty(const struct list_head *head) {
	return head->next == head;
}

#define list_entry(ptr, type, member) \
	container_of(ptr, type, member)

#define list_for_each(pos, head) \
  for (pos = (head)->next; pos != (head);	\
       pos = pos->next)

#define list_for_each_prev(pos, head) \
	for (pos = (head)->prev; prefetch(pos->prev), pos != (head); \
        	pos = pos->prev)

#define list_for_each_safe(pos, n, head) \
	for (pos = (head)->next, n = pos->next; pos != (head); \
		pos = n, n = pos->next)

#define list_for_each_entry(pos, head, member)				\
	for (pos = list_entry((head)->next, typeof(*pos), member);	\
	     &pos->member != (head);					\
	     pos = list_entry(pos->member.next, typeof(*pos), member))

#define list_for_each_entry_reverse(pos, head, member)			\
	for (pos = list_entry((head)->prev, typeof(*pos), member);	\
	     &pos->member != (head); 	\
	     pos = list_entry(pos->member.prev, typeof(*pos), member))

#define list_for_each_entry_safe(pos, n, head, member)			\
	for (pos = list_entry((head)->next, typeof(*pos), member),	\
		n = list_entry(pos->member.next, typeof(*pos), member);	\
	     &pos->member != (head); 					\
	     pos = n, n = list_entry(n->member.next, typeof(*n), member))

#define list_for_each_entry_safe_reverse(pos, n, head, member)		\
	for (pos = list_entry((head)->prev, typeof(*pos), member),	\
		n = list_entry(pos->member.prev, typeof(*pos), member);	\
	     &pos->member != (head); 					\
	     pos = n, n = list_entry(n->member.prev, typeof(*n), member))

#if 0    //DEBUG
#define debug(fmt, args...) fprintf(stderr, fmt, ##args)
#else
#define debug(fmt, args...)
#endif

typedef struct{
    unsigned char op;
    unsigned char len;
    struct list_head list;
} code_tuple;

typedef struct{
    int pid;
    int arrival_time;
    int code_bytes;
    int pc;   // program counter
    struct list_head job, ready, wait;
    struct list_head clist; //code_tuple list
} process;

process idle_ps = {
    .pid = 100,
    .arrival_time = 0,
    .code_bytes = 2,
    .pc = -1
};

void push_job(process *node, process src, struct list_head *q){
    node->pid = src.pid;
    node->arrival_time = src.arrival_time;
    node->code_bytes = src.code_bytes;
    node->pc = -1;
    INIT_LIST_HEAD(&node->job);
    INIT_LIST_HEAD(&node->clist);
    list_add_tail(&node->job, q);
    return;
}

void push_ct(code_tuple *node, code_tuple src, process *ps){
    node->op = src.op;
    node->len = src.len;
    INIT_LIST_HEAD(&node->list);
    list_add_tail(&node->list, &ps->clist);
    return;
}

int main(int argc,char* argv[]){
	process *cur, *next;
    code_tuple *ccur, *cnext;

	LIST_HEAD(job_q);

    // read ps info from standard input: pid, eta, code_bytes
    process ps;
    code_tuple ct;
    int psize = 3*sizeof(int), csize = 2*sizeof(unsigned char);
    int cnt_ps=0;    //debug
    while(fread(&ps, psize, 1, stdin) == 1){
        cur = malloc(sizeof(*cur));
        push_job(cur, ps, &job_q);

        // read code: op, len
        for(int i=0; i<ps.code_bytes/2; i++){
            if(fread(&ct, csize, 1, stdin) == 1){
                ccur = malloc(sizeof(*ccur));
                push_ct(ccur, ct, cur);
            }
        }
        cnt_ps++;
    }
    
    /*========================================HW1-2 START======================================================*/
    // hw1-2_step_0: add idle process
    cur = malloc(sizeof(*cur));
    push_job(cur, idle_ps, &job_q);

    ccur = malloc(sizeof(*ccur));
    push_ct(ccur, ct, cur);
    cnt_ps++;
    // printf("---\n%d %d %d\n%d %d\n",cur->pid,cur->arrival_time,cur->code_bytes,ccur->op,ccur->len); //debug

    // step_1: implement simulation: node-traversal in job_q?
    // step_1-0: create ready queue & wait queue
    LIST_HEAD(ready_q); //LIST_HEAD(wait_q);    //hw1-3

    // printf("Start Processing. loaded procs = %d\n",cnt_ps);
    int clocks=0, flag=0, idle=0;
    int load_cnt=0, left_cnt=0, all_loaded=0;   //loaded process count, left .., if all ps loaded?
    // step_2-0: ready_q.push(jobs) if clock == process.eta
    while(1){
        if(!all_loaded){        // load process
            list_for_each_entry_safe(cur, next, &job_q, job){
                if(clocks != cur->arrival_time){
                    continue;
                }
                printf("%04d CPU: Loaded PID: %03d\tArrival: %03d\tCodesize: %03d\tPC: %03d\n",clocks, cur->pid, cur->arrival_time, cur->code_bytes, cur->pc+1);
                INIT_LIST_HEAD(&cur->ready);
                list_add_tail(&cur->ready, &ready_q);
                load_cnt++; left_cnt++;
                // printf("Loaded %d processes\n",load_cnt);
                if(load_cnt==cnt_ps){
                    all_loaded=1;
                }
                if(clocks == 0){
                    continue;       // idle_ps
                }
            }
        }
        // printf("HELP\n");    //debugging
        // All processes done: terminating last process(idle_ps)
        if(all_loaded && left_cnt==1){
            clocks -= 10+1;   // undo context-switching + ticking
            flag-=10, idle-=10, left_cnt=0;
            list_del(&cur->ready);      //delete idle_ps
            break;
        }
        // step_2-1: operation processing
        if(clocks == flag){
            // printf("At %d: all_loaded?: %d left_cnt: %d\n",clocks,all_loaded,left_cnt);
            // for each process
            list_for_each_entry_safe(cur, next, &ready_q, ready){ 
                if(cur->pid == 100){
                    continue;            // skip idle_ps
                }
                // if(clocks>300) break;    //debugging

                // terminating one process
                if(cur->pc == cur->code_bytes/2-1){
                    // printf("%04d CPU: Process is terminated PID: %03d PC: %03d\n",clocks, cur->pid, cur->pc);
                    clocks+=10, flag+=10, idle+=10;     //context-switching
                    list_del(&cur->ready);
                    left_cnt--;
                    continue;
                }
                // search current process's PC: op-processing w. code_tuples
                int pc = -1;
                /*if(clocks!=flag || pc!=cur->pc) continue; // hint for hw1-3?*/
                // for each code_tuple
                list_for_each_entry_safe(ccur, cnext, &cur->clist, list){
                    // pc matching
                    if(clocks!=flag || pc!=cur->pc){  //pc!=cur->pc만 보면 안 되는 이유?: ps#0 다 끝날 때까지 기다리는 게 아닌, 첫 OP_CPU 끝나면 바로 ps#1의 첫 작업 시작해버림
                        pc++; continue;
                    }
                    // if(pc > -1) printf("%04d Increase PC\tPID: %03d PC: %03d\n",clocks,cur->pid,cur->pc);
                    cur->pc++;
                    if(ccur->op==0){    //1. OP_CPU
                        // printf("%04d CPU: OP_CPU START len: %03d ends at: %04d\n",clocks,ccur->len,clocks+ccur->len);
                    }else{              //2. OP_IO
                        printf("%04d CPU: OP_IO START len: %03d ends at: %04d\n",clocks,ccur->len,clocks+ccur->len);
                        idle += ccur->len;
                    }
                    flag += ccur->len;
                    // printf("FLAG TEST: %d\n",flag); //debugging
                    break;  // break loop: next process in ready_q
                    /*UNSOLVED QUESTION
                    for ps#0's 1st operation ==> maintain PC=0 during 0~4 clocks?*/
                    // by setting initial_pc = -1 ==> increase when running code_tuple, not ready_q(ps)
                }
            }
        }
        // printf("flag: %d\n",flag);   //debugging
        clocks++;  //ticking
    }
    // last step: final report
    double util = (double) (clocks-idle)/clocks * 100;
    printf("*** TOTAL CLOCKS: %04d IDLE: %04d UTIL: %2.2f%%\n",clocks,idle,util);

    // printf("DONE. Freeing the process in job queue\n");
    list_for_each_entry_safe_reverse(cur, next, &job_q, job){
        // printf("PID: %03d\tARRIVAL: %03d\tCODESIZE: %03d\n", cur->pid, cur->arrival_time, cur->code_bytes);
        list_for_each_entry_safe(ccur, cnext, &cur->clist, list){
            // printf("%d %d\n",ccur->op, ccur->len);
            list_del(&ccur->list);  //remove code_tuple node
            free(ccur);
            // printf("Checking memory_leak. op: %d\n",ccur->op);
        }
        list_del(&cur->job);    //remove process node
        free(cur);
        // printf("Checking memory_leak. PID: %d\n",cur->pid);
    }
    return 0;
}