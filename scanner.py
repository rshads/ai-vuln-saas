import zipfile
import os

def scan_file_content(content, filename):
    results = []
    lines = content.split("\n")

    for i, line in enumerate(lines, 1):

        if "os.system" in line:
            results.append(("Command Injection", "CRITICAL", filename, i, line))

        if "eval(" in line or "exec(" in line:
            results.append(("Code Injection", "CRITICAL", filename, i, line))

        if "select" in line.lower() and "'" in line:
            results.append(("SQL Injection", "HIGH", filename, i, line))

        if "render_template_string" in line:
            results.append(("XSS", "HIGH", filename, i, line))

        if "password" in line.lower():
            results.append(("Hardcoded Secret", "MEDIUM", filename, i, line))

    return results


def scan_zip(file_path):
    results = []

    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall("temp_scan")

    for root, _, files in os.walk("temp_scan"):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                results += scan_file_content(content, file)

    return results
