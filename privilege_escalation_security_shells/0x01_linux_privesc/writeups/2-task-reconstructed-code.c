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


---
---
---
---

---

OR


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[]) {
    // [rbp-0x21] to [rbp-0x19]: An 8-byte key buffer + 1 byte for null terminator
    char key[9];
    
    // [rbp-0x470]: A 1024-byte array tracking frequencies for 256 possible ASCII characters
    // (Initialized via standard compiler `rep stos` optimization)
    unsigned int counts[256];
    memset(counts, 0, sizeof(counts));

    // Initialize the key variable to "11111111" (0x3131313131313131)
    *(unsigned long long *)key = 0x3131313131313131ULL;
    key[8] = '\0';

    // [rbp-0x70]: Local buffer for the input string.
    char buffer[79]; 

    // Loop counters
    int i = 0; // [rbp-0x14]
    int j = 0; // [rbp-0x18]

    // Verify command-line arguments (argc == 2)
    if (argc != 2) {
        printf("Usage: %s <input>\n", argv[0]); 
        return 1;
    }

    // VULNERABLE: Unbounded string copy into a bounded stack buffer
    strcpy(buffer, argv[1]);

    // Print the received buffer
    printf("Buffer: %s\n", buffer);

    // Character frequency counting loop
    for (i = 0; (size_t)i < strlen(buffer); i++) {
        unsigned char ch = (unsigned char)buffer[i];
        counts[ch] = counts[ch] + 1;
    }

    // Loop through all possible ASCII values to print counts
    for (j = 0; j <= 255; j++) {
        if ((int)counts[j] > 0) {
            printf("%c: %d\n", j, counts[j]);
        }
    }

    // Privilege escalation safety check
    // Compares our key against the hidden secret key "22222222"
    if (strcmp(key, "22222222") == 0) {
        setuid(0);
        setgid(0);
        system("/bin/bash");
    }

    return 0;
}
