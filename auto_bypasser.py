import subprocess

def get_target_endpoints():
    file_path = input("Target file: ").strip() 
    target_endpoints = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                target_endpoints.append(line.strip())
    except Exception as e:
        print(f"[-] Getting target endpoints got error: {e}")
        return []
    
    return target_endpoints


def run_shell(url):
    shell_command = f"./403-bypass.sh -u {url} --exploit"

    try:
        print("\n")
        print(f"[+] Checking \"{url}\"")
        result = subprocess.run(shell_command, shell=True, check=True, capture_output=True, text=True)

        if result.stderr: 
            print("[!] Warning: Script produced error output:\n", result.stderr)

        filtered_output = "\n".join(
            line for line in result.stdout.splitlines()
            if "Status:" in line and "Status: 403" not in line and "Status: 000" not in line
        )

        if filtered_output:
            print(filtered_output)
        
        print("\n")
    except subprocess.CalledProcessError as e: 
        print(f"[-] Shell command execution failed => ", e.output or e.stderr)


endpoints = get_target_endpoints()
if endpoints:
    for endpoint in endpoints:
        run_shell(endpoint)
else:
    print("[-] Empty endpoints")
