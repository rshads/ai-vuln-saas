def ai_analyze(vuln):
    templates = {
        "SQL Injection": {
            "desc": "The application is vulnerable to SQL injection via unsafe query construction.",
            "fix": "Use parameterized queries or ORM frameworks."
        },
        "Command Injection": {
            "desc": "User input is being executed as a system command.",
            "fix": "Avoid os.system and sanitize input strictly."
        },
        "XSS": {
            "desc": "Unescaped user input is rendered in HTML output.",
            "fix": "Use auto-escaping templates or sanitize output."
        },
        "Code Injection": {
            "desc": "Dangerous functions like eval/exec detected.",
            "fix": "Remove eval/exec and redesign logic safely."
        },
        "Hardcoded Secret": {
            "desc": "Sensitive credentials are exposed in code.",
            "fix": "Move secrets to environment variables."
        }
    }

    return templates.get(vuln["type"], {
        "desc": "Unknown vulnerability detected.",
        "fix": "Manual review required."
    })
