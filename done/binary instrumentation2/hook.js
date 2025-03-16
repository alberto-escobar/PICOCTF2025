// var GetLastError = new NativeFunction(
//     Module.getExportByName("KERNEL32.DLL", "GetLastError"),
//     "uint32",
//     []
// );

// // discover that GetModuleFileNameW was used in bininst2.exe
// // Hook GetModuleFileNameW to capture arguments and return value
// Interceptor.attach(Module.getExportByName("KERNEL32.DLL", "GetModuleFileNameW"), {
//     onEnter: function (args) {
//         console.log("[+] GetModuleFileNameW called:");
//         console.log("    hModule: " + args[0]);
//         this.lpFilename = args[1]; // Buffer where filename will be stored
//         this.nSize = args[2].toInt32();
//     },
//     onLeave: function (retval) {
//         if (retval.toInt32() > 0 && !this.lpFilename.isNull()) {
//             var filename = Memory.readUtf16String(this.lpFilename);
//             console.log("    Retrieved Filename: " + filename);
//         } else {
//             console.log("    [!] GetModuleFileNameW returned an empty or invalid filename.");
//         }
//         console.log("    Return Value: " + retval.toInt32());
//     }
// });

// // discover that CreateFileA was used in bininst2.exe
// Interceptor.attach(Module.getExportByName("KERNEL32.DLL", "CreateFileA"), {
//     onEnter: function (args) {
//         console.log("[+] CreateFileA called with arguments:");
//         var originalFilename = Memory.readAnsiString(args[0]);
//         console.log("    lpFileName: " + originalFilename);
//         console.log("    dwDesiredAccess: 0x" + args[1].toInt32().toString(16));
//         console.log("    dwShareMode: 0x" + args[2].toInt32().toString(16));
//         console.log("    lpSecurityAttributes: " + args[3]);
//         console.log("    dwCreationDisposition: 0x" + args[4].toInt32().toString(16));
//         console.log("    dwFlagsAndAttributes: 0x" + args[5].toInt32().toString(16));
//         console.log("    hTemplateFile: " + args[6]);
//     },
//     onLeave: function (retval) {
//         console.log("[+] CreateFileA returned: " + retval.toInt32());
//         if (retval.toInt32() == -1) {
//             console.log("[!] GetLastError after CreateFileA: " + GetLastError());
//         }
//     }
// });

// // tried changing file name of CreateFileA, can realloc mem, have to change memory directly
// Interceptor.attach(Module.getExportByName("KERNEL32.DLL", "CreateFileA"), {
//     onEnter: function (args) {
//         console.log("[+] CreateFileA called with arguments:");
//         var originalFilename = Memory.readAnsiString(args[0]);
//         console.log("    lpFileName: " + originalFilename);
//         console.log("    dwDesiredAccess: 0x" + args[1].toInt32().toString(16));
//         console.log("    dwShareMode: 0x" + args[2].toInt32().toString(16));
//         console.log("    lpSecurityAttributes: " + args[3]);
//         console.log("    dwCreationDisposition: 0x" + args[4].toInt32().toString(16));
//         console.log("    dwFlagsAndAttributes: 0x" + args[5].toInt32().toString(16));
//         console.log("    hTemplateFile: " + args[6]);

//         // Change the file name
//         var newFilename = "a";
//         Memory.writeAnsiString(args[0], newFilename);
//         console.log("    NEW lpFileName: " + Memory.readAnsiString(args[0]));
//     },
//     onLeave: function (retval) {
//         console.log("[+] CreateFileA returned: " + retval.toInt32());
//         if (retval.toInt32() == -1) {
//             console.log("[!] GetLastError after CreateFileA: " + GetLastError());
//         }
//     }
// });

// proper way to modify filename used in CreateFileA
Interceptor.attach(Module.getExportByName("KERNEL32.DLL", "CreateFileA"), {
    onEnter: function (args) {
        var originalFilename = Memory.readAnsiString(args[0]);
        console.log("[+] CreateFileA called with arguments:");
        console.log("    Original lpFileName: " + originalFilename);

        var newFilename = "flag.txt";

        if (newFilename.length > originalFilename.length) {
            console.log("[!] New filename is longer than the original! This might cause issues.");
            return;
        }

        // Change memory protection to allow writing
        var ptrPage = args[0];
        var size = originalFilename.length + 1; // +1 for null terminator
        var oldProtect = Memory.protect(ptrPage, size, 'rw-'); // Read-Write
        if (!oldProtect) {
            console.log("[!] Failed to change memory protection.");
            return;
        }

        console.log("    [*] Modifying filename in memory to: " + newFilename);
        Memory.writeAnsiString(args[0], newFilename); // Modify in-place

        // Restore original memory protection (assuming it's 'r--' initially)
        Memory.protect(ptrPage, size, 'r--');
    },
    onLeave: function (retval) {
        console.log("[+] CreateFileA returned: " + retval.toInt32());

        if (retval.toInt32() == -1) {
            var errorCode = new NativeFunction(Module.getExportByName("KERNEL32.DLL", "GetLastError"), 'uint32', [])();
            console.log("[!] GetLastError after CreateFileA: " + errorCode);
        }
    }
});


// WriteFile called with action to write zero bytes to file, had to modify it to write some bytes to file
Interceptor.attach(Module.getExportByName("KERNEL32.DLL", "WriteFile"), {
    onEnter: function (args) {
        var hFile = args[0];  
        var lpBuffer = args[1];  
        var nNumberOfBytesToWrite = args[2].toInt32();  

        console.log("[+] WriteFile called:");
        console.log("    hFile: " + hFile);
        console.log("    Original nNumberOfBytesToWrite: " + nNumberOfBytesToWrite);

        // Truncate to 2 bytes
        var newSize = 64;
        args[2] = ptr(newSize);
        console.log("    [*] Modified nNumberOfBytesToWrite to: " + newSize);

        // Print data being written (up to newSize bytes)
        var data = Memory.readUtf8String(lpBuffer, newSize);
        console.log("    Data being written (modified): " + data);
    },
    onLeave: function (retval) {
        console.log("[+] WriteFile returned: " + retval.toInt32());
    }
});
