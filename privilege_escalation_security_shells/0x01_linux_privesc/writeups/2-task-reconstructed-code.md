#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void functional_logic(char *input) {
    char buffer[64]; // Estimated size based on the crash threshold
    
    // Debug mark 1
    // printf("11111111\n"); 

    // The vulnerability: bounded source copied into a static destination
    strcpy(buffer, input); 
    printf("Buffer: %s\n", buffer);

    // Character frequency analysis logic loop observed in runtime output
    int counts[256] = {0};
    int len = strlen(buffer);
    for (int i = 0; i < len; i++) {
        counts[(unsigned char)buffer[i]]++;
    }
    for (int i = 0; i < 256; i++) {
        if (counts[i] > 0) {
            printf("%c: %d\n", i, counts[i]);
        }
    }
}

int main(int argc, char *argv[]) {
    // Structural SUID/SGID preservation
    setuid(0);
    setgid(0);

    if (argc < 2) {
        printf("Usage: %s <input>\n", argv[0]);
        return 1;
    }

    // Checking for a hidden or specific flag option via strcmp
    if (strcmp(argv[1], "secret_parameter_here") == 0) {
        // Debug mark 2
        // printf("22222222\n");
        system("/bin/bash");
    } else {
        functional_logic(argv[1]);
    }

    return 0;
}
