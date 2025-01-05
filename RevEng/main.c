#include <stdio.h>
#include <string.h>

int check_flag(const char *flag) {
    if (strlen(flag) != 18) return 0;

    if (flag[0] == 'C' && flag[1] == 'K' && flag[2] == 'C' && flag[3] == 'T' && flag[4] == 'F' && flag[5] == '{' &&
        flag[6] == 'R' && flag[7] == '3' && flag[8] == 'v' && flag[9] == '3' && flag[10] == '_' &&
        flag[11] == '1' && flag[12] == '5' && flag[13] == '_' && flag[14] == 'F' &&
        flag[15] == 'u' && flag[16] == 'n' && flag[17] == '}') {
        return 1;
    }
// CKCTF{R3v3_15_Fun}

    return 0;
}

int main() {
    char input[64];
    printf("Enter the flag: ");
    scanf("%63s", input);

    if (check_flag(input)) {
        printf("Correct! The flag is: %s\n", input);
    } else {
        printf("Wrong flag!\n");
    }

    return 0;
}