var sleepHook = Module.findExportByName("KERNEL32.dll", "Sleep");

if (sleepHook !== null) {
    var originalSleep = new NativeFunction(sleepHook, 'void', ['uint32']);

    Interceptor.replace(sleepHook, new NativeCallback(function (milliseconds) {
        console.log("Intercepted Sleep! Original value:", milliseconds);
        var newSleep = 1; // Change sleep time to 1 second
        console.log("Modified Sleep value:", newSleep);
        return originalSleep(newSleep);
    }, 'void', ['uint32']));
}
