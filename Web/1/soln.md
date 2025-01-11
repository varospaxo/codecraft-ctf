1. view page source 
2. base64 decode the script tag code
            const code = "Y29uc3QgbG9uZ2xpc3QgPSBbMTMyLCA1NiwgMTI0LCAxMDksIDU2LCAxMjMsIDEyNCwgMTA0LCA1OCwgNzMsIDEwMiwgMTIyLCA1NiwgMTAyLCA1OCwgMTA2LCA1OSwgMTE5LCA2MCwgMTMwLCA3NywgOTEsIDc0LCA4MiwgNzRdOwpjb25zdCBiYWNrZ3JvdW5kID0gKCkgPT4gewogICAgbGV0IGludGVybWVkaWF0ZUFycmF5ID0gW107CiAgICBsZXQgbGlzdCA9ICIiOwogICAgbG9uZ2xpc3QuZm9yRWFjaCgoY2hhciwgaW5kZXgpID0+IHsKICAgICAgICBpbnRlcm1lZGlhdGVBcnJheVtpbmRleF0gPSBjaGFyIF4gKGluZGV4ICUgNSk7CiAgICB9KTsKICAgIGNvbnN0IGFkZGl0aW9uYWxQcm9jZXNzaW5nID0gaW50ZXJtZWRpYXRlQXJyYXkubWFwKChjaGFyLCBpbmRleCkgPT4gewogICAgICAgIHJldHVybiAoY2hhciAqIDMgKyA1IC0gaW5kZXgpICUgMjU2OwogICAgfSk7CiAgICBhZGRpdGlvbmFsUHJvY2Vzc2luZy5mb3JFYWNoKGNoYXIgPT4gewogICAgICAgIGlmIChjaGFyID49IDMyICYmIGNoYXIgPD0gMTI2KSB7CiAgICAgICAgICAgIGxpc3QgKz0gU3RyaW5nLmZyb21DaGFyQ29kZShjaGFyKTsKICAgICAgICB9CiAgICB9KTsKICAgIGNvbnNvbGUubG9nKCJEZWJ1ZyBpbmZvOiIsIGludGVybWVkaWF0ZUFycmF5KTsKICAgIGNvbnNvbGUubG9nKCJQcm9jZXNzZWQgYXJyYXk6IiwgYWRkaXRpb25hbFByb2Nlc3NpbmcpOwogICAgY29uc29sZS5sb2cobGlzdCk7Cn07CmNvbnN0IHJ1bm5lciA9ICgpID0+IHsKICAgIGxldCBsaXN0ID0gIiI7CiAgICBsb25nbGlzdC5mb3JFYWNoKGNoYXIgPT4gewogICAgICAgIGNoYXIgLT0gNzsKICAgICAgICBsaXN0ICs9IFN0cmluZy5mcm9tQ2hhckNvZGUoY2hhcik7CiAgICB9KTsKICAgIGxpc3QgPSBsaXN0LnNwbGl0KCcnKS5yZXZlcnNlKCkuam9pbignJyk7CiAgICBjb25zb2xlLmxvZyhsaXN0KTsKfTsKYmFja2dyb3VuZCgpOw=="
3. converts to the below code
            const longlist = [132, 56, 124, 109, 56, 123, 124, 104, 58, 73, 102, 122, 56, 102, 58, 106, 59, 119, 60, 130, 77, 91, 74, 82, 74];
            const background = () => {
                let intermediateArray = [];
                let list = "";
                longlist.forEach((char, index) => {
                    intermediateArray[index] = char ^ (index % 5);
                });
                const additionalProcessing = intermediateArray.map((char, index) => {
                    return (char * 3 + 5 - index) % 256;
                });
                additionalProcessing.forEach(char => {
                    if (char >= 32 && char <= 126) {
                        list += String.fromCharCode(char);
                    }
                });
                console.log("Debug info:", intermediateArray);
                console.log("Processed array:", additionalProcessing);
                console.log(list);
            };
            const runner = () => {
                let list = "";
                longlist.forEach(char => {
                    char -= 7;
                    list += String.fromCharCode(char);
                });
                list = list.split('').reverse().join('');
                console.log(list);
            };
            background();
4. Add runner(); function call to the js code and run in an online compiler
Flag-
CKCTF{5p4c3_1s_B3aut1fu1}