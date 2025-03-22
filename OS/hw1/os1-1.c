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
    struct list_head job, ready, wait;
    // code_tuple* operations;
    struct list_head clist; //code_tuple list
} process;

void push_ps(process *node, process src, struct list_head *q){
    node->pid = src.pid;
    node->arrival_time = src.arrival_time;
    node->code_bytes = src.code_bytes;
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

    process ps;
    code_tuple ct;
    
    int psize = sizeof(ps.pid) + sizeof(ps.arrival_time) + sizeof(ps.code_bytes);
    int csize = sizeof(ct.op) + sizeof(ct.len);
    
    // read ps info from standard input: pid, eta, code_bytes
    while(fread(&ps, psize, 1, stdin) == 1){
        cur = malloc(sizeof(*cur));

        push_ps(cur, ps, &job_q);
        // cur->pid = ps.pid;
        // cur->arrival_time = ps.arrival_time;
        // cur->code_bytes = ps.code_bytes;
        // INIT_LIST_HEAD(&cur->job);
        // INIT_LIST_HEAD(&cur->clist);
        // list_add_tail(&cur->job, &job_q);

        // read code: op, len
        for(int i=0; i<ps.code_bytes/2; i++){
            if(fread(&ct, csize, 1, stdin) == 1){
                ccur = malloc(sizeof(*ccur));

                push_ct(ccur, ct, cur);
                // ccur->op = ct.op;
                // ccur->len = ct.len;
                // INIT_LIST_HEAD(&ccur->list);
                // list_add_tail(&ccur->list, &cur->clist);
            }
        }
    }
    
    // milestone
    // list_for_each_entry(cur, &job_q, job){
    //     printf("pid=%d\n",cur->pid);
    // }

    list_for_each_entry_safe_reverse(cur, next, &job_q, job){
        printf("PID: %03d\tARRIVAL: %03d\tCODESIZE: %03d\n", cur->pid, cur->arrival_time, cur->code_bytes);
        list_for_each_entry_safe(ccur, cnext, &cur->clist, list){
            printf("%d %d\n",ccur->op, ccur->len);
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