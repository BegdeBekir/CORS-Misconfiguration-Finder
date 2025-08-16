import argparse
import requests

# Farklı Origin header’ları denenir
test_origins = [
    "https://evil.com",
    "https://attacker.com",
    "null"
]

def test_cors(url):
    findings = []
    for origin in test_origins:
        try:
            headers = {"Origin": origin}
            resp = requests.get(url, headers=headers, timeout=10)
            aca_origin = resp.headers.get("Access-Control-Allow-Origin", "")
            aca_credentials = resp.headers.get("Access-Control-Allow-Credentials", "")
            
            note = ""
            if aca_origin == "*" and aca_credentials.lower() == "true":
                note = "⚠️ Wildcard with credentials - critical misconfiguration!"
            elif aca_origin == origin:
                note = "⚠️ Reflective ACAO - potential CORS vulnerability!"
            
            if note:
                findings.append(f"Origin: {origin} | ACAO: {aca_origin} | ACAC: {aca_credentials} | Note: {note}")
        except requests.RequestException as e:
            findings.append(f"Origin: {origin} | Error: {e}")
    return findings


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CORS Misconfiguration Finder (Advanced)")
    parser.add_argument("--input", required=True, help="Input file with target URLs")
    parser.add_argument("--output", required=True, help="Output file to save findings")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    all_findings = []
    for url in urls:
        print(f"🔍 Testing {url}")
        findings = test_cors(url)
        if findings:
            for fline in findings:
                all_findings.append(f"{url} | {fline}")

    with open(args.output, "w", encoding="utf-8") as f:
        for line in all_findings:
            f.write(line + "\n")

    print(f"✅ CORS misconfiguration scan completed. Results saved to {args.output}")
