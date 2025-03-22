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
    int io_flag;
    struct list_head job, ready, wait;
    struct list_head clist; //code_tuple list
} process;

process idle_ps = {
    .pid = 100,
    .arrival_time = 0,
    .code_bytes = 2,
    .pc = -1,
    .io_flag = 0
};

void push_job(process *node, process src, struct list_head *q){
    node->pid = src.pid;
    node->arrival_time = src.arrival_time;
    node->code_bytes = src.code_bytes;
    node->pc = -1;
    node->io_flag = 0;
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
    LIST_HEAD(ready_q); LIST_HEAD(wait_q);    //hw1-3

    // printf("Start Processing. loaded procs = %d\n",cnt_ps);
    int clocks=0, flag=0, idle=0;
    int load_cnt=0, left_readys=0, all_arrived=0;   //arrived_process_count, left procs in ready_q .., all procs arrived?
    // step_2-0: ready_q.push(jobs) if clock == process.eta
    
    /*=======new var for hw1-3*/
    int prev_pid=-1;
    int IO_FIN=0;   // time of all processes's OP_IO finished
    int cnt_term=0; // number of terminated processes
    while(1){
        if(!all_arrived){        // load process
            list_for_each_entry_safe(cur, next, &job_q, job){
                if(clocks != cur->arrival_time){
                    continue;
                }
                printf("%04d CPU: Loaded PID: %03d\tArrival: %03d\tCodesize: %03d\tPC: %03d\n",clocks, cur->pid, cur->arrival_time, cur->code_bytes, cur->pc+1);
                INIT_LIST_HEAD(&cur->ready);
                list_add_tail(&cur->ready, &ready_q);
                load_cnt++; left_readys++;
                // printf("Loaded %d processes\n",load_cnt);
                if(load_cnt==cnt_ps){
                    printf("WTH\n");
                    all_arrived=1;
                }
                if(clocks == 0){
                    continue;       // idle_ps
                }
            }
        }
        // All processes done: terminating last process(idle_ps)
        if(all_arrived && left_readys==0){
            // clocks -= 10+1;   // undo context-switching + ticking
            // flag-=10, idle-=10, left_readys=0;
            // list_del(&cur->ready);      //delete idle_ps
            break;
        }
        // step_2-1: operation processing
        if(clocks == flag){
            // printf("At %d: all_arrived?: %d left_readys: %d\n",clocks,all_arrived,left_readys);
            // for each process
            list_for_each_entry_safe(cur, next, &ready_q, ready){
                if(clocks!=flag) break;
                // printf("Previous PID: %d, Current PID: %d\n",prev_pid, cur->pid);
                // printf("%d procs terminated\n",cnt_term);
                // if(cur->pid==1) printf("prev_pid: %d\n",prev_pid);
                // printf("%d terminated\n",cnt_term);
                // printf("left ready_procs: %d\n",left_readys);
                // printf("cur->pc: %d, code_bytes/2: %d\n",cur->pc,cur->code_bytes/2);
                
                if(clocks>0 && prev_pid!=cur->pid){   // Context-switching
                    if(cur->pid==100){
                        if(!all_arrived){
                            continue;
                        }
                        if(left_readys>1){
                        printf("HELP\n");
                            continue;
                        }
                    }
                    printf("%04d CPU: Reschedule\t PID: %03d\t Status: ??\n",clocks,prev_pid);  // Reschedule
                    clocks += 10, flag +=10, idle +=10; // time setting
                    printf("%04d CPU: Switched from: PID:%03d\t to: %03d\n",clocks,prev_pid,cur->pid);  // Switched
                    prev_pid = cur->pid;
                }
                if(cur->pid == 100){    // handling idle_ps
                    // printf("%06d: PREV PID: %d\n",clocks,prev_pid);
                    // // if(left_readys>2)
                    // if(all_arrived!=1){
                    //     continue;
                    // }
                    // if(left_readys>2){
                    //     printf("%06d: HELP, prev: %d, cur: %d\n",clocks,prev_pid,cur->pid);
                    //     continue;
                    // }
                    // if(prev_pid != cur->pid){
                    //     if(clocks != IO_FIN){
                    //         printf("%04d CPU: OP_IDLE START\n",clocks);
                    //         flag++; idle++;
                    //         break;
                    //     }
                    // }else continue;
                    if(!all_arrived)continue;
                    if(left_readys>1) continue;
                    if(clocks < IO_FIN) continue;
                }
                // if(clocks>300) break;    //debugging

                if(cur->pc > -1) printf("%04d CPU: Increase PC\t PID: %03d\t Status: ??\n",clocks,cur->pid);
                cur->pc++;  // Increase PC here?

                if(cur->pc == cur->code_bytes/2){   // terminating one process
                    printf("%04d CPU: Process is terminated PID: %03d PC: %03d\n",clocks, cur->pid, cur->pc);
                    list_del(&cur->ready);
                    if(cur->pid==100){
                        if(clocks < IO_FIN) list_add_tail(&cur->ready, &ready_q);   //idle_ps
                    }
                    left_readys--;
                    cnt_term++;
                    printf("PID: %d LEFT READY_Procs in ready_q: %d, prev PID: %d, cur PID: %d\n",cur->pid,left_readys,prev_pid,cur->pid);
                    // prev_pid = cur->pid;
                    // printf("ALL arrived?: %d\n",all_arrived);
                    continue;
                }
                // search current process's PC: op-processing w. code
                int pc = 0;
                /*if(clocks!=flag || pc!=cur->pc) continue; // hint for hw1-3?*/
                // for each code_tuple
                list_for_each_entry_safe(ccur, cnext, &cur->clist, list){
                    // pc matching
                    if(pc!=cur->pc){  //clocks!=flag도 보는 이유?: ps#0 다 끝날 때까지 기다리는 게 아닌, 첫 OP_CPU 끝나면 바로 ps#1의 첫 작업 시작해버림
                        pc++; continue;
                    }
                    // if(pc > -1) printf("%04d Increase PC\tPID: %03d PC: %03d\n",clocks,cur->pid,cur->pc);
                    // cur->pc++;
                    if(ccur->op==0){    //1. OP_CPU
                        printf("%04d CPU: OP_CPU START len: %03d ends at: %04d\n",clocks,ccur->len,clocks+ccur->len);
                        prev_pid = cur->pid;    // current running process#
                        // INIT_LIST_HEAD(&cur->ready);
                        // list_add_tail(&cur->ready, &ready_q);
                        flag += ccur->len;
                        // printf("flag: %d\n",flag);   //debug
                    }else if(ccur->op==1){              //2. OP_IO
                        printf("%04d CPU: OP_IO START len: %03d ends at: %04d\n",clocks,ccur->len,clocks+ccur->len);
                        cur->io_flag = clocks + ccur->len;
                        if(cur->io_flag > IO_FIN){
                            IO_FIN = cur->io_flag;  // update the finished time of all io
                            printf("IO_FIN: %d\n",IO_FIN);
                        }
                        idle += ccur->len;
                        flag++;                                                     // IO_CALLING_COST??????????
                        list_del(&cur->ready);  //ready_q.pop(ps)
                        left_readys--;
                        INIT_LIST_HEAD(&cur->wait); //wait_q.push(cur)
                        list_add_tail(&cur->wait, &wait_q);
                    }// printf("FLAG TEST: %d\n",flag); //debugging
                    break;  // break loop: next process in ready_q
                }
                // break;
            }
        }
        // printf("flag: %d\n",flag);   //debugging
        //ticking
        clocks++;
        list_for_each_entry_safe(cur, next, &wait_q, wait){
            if(clocks!=cur->io_flag) continue;
            printf("%04d IO : COMPLETED! PID: %03d\t IOTIME: %03d PC: %03d\n",clocks,cur->pid,clocks,cur->pc);
            INIT_LIST_HEAD(&cur->ready);
            list_add_tail(&cur->ready, &ready_q);
            left_readys++;
        }
        if(list_empty(&ready_q) && list_empty(&wait_q)){
            break;
        }
        if(clocks>280) break;
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