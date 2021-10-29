mov ah, 0x0e ; tty mode

mov bp, 0x8000
mov sp, bp ; if the stack is empty then sp points to bp

push 'A'
push 'B'
push 'C'

; to show how the stack grows downwards
mov al, [0x7ffe] ; 0x8000 - 2
int 0x10

mov al, [0x8000]
int 0x10

; recover characters using 'pop'
pop bx
mov al, bl
int 0x10 ; prints C

pop bx
mov al, bl
int 0x10 ; prints B

pop bx
mov al, bl
int 0x10 ; prints A

jmp $
times 510 - ($ - $$) db 0
dw 0xaa55