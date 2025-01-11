#include <stdio.h>
#include <string.h>

int hehe(const char *input);

int ohh(const char *input) {
    if (strlen(input) != 18) return 0;

    // Splitting checks to add complexity
    if (input[0] != 'C' || input[1] != 'K' || input[2] != 'C') return 0;
    if (input[3] != 'T' || input[4] != 'F' || input[5] != '{') return 0;
    if (input[6] != 'R' || input[7] != '3' || input[8] != 'v') return 0;
    if (input[9] != '3' || input[10] != '_') return 0;

    if (input[11] != '1' || input[12] != '5' || input[13] != '_') return 0;
    if (input[14] != 'F' || input[15] != 'u' || input[16] != 'n' || input[17] != '}') return 0;

    return hehe(input);
}

// Additional check with a disguised name
int hehe(const char *input) {
    unsigned int hash = 0;
    for (int i = 0; i < strlen(input); i++) {
        hash = (hash * 31 + input[i]) ^ 0x45; // Hash-like calculation
    }
    // Simple hash comparison to confuse attackers
    return hash == 0x1F4ACB3; // Pre-calculated value for CKCTF{R3v3_15_Fun}
}

int main() {
    char user_input[64];
    printf("Enter the flag: ");
    scanf("%63s", user_input);

    if (ohh(user_input)) {
        printf("Correct! The flag is: %s\n", user_input);
    } else {
        printf("Wrong flag!\n");
    }

    return 0;
}