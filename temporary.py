import requests

url = "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=apache"

data = requests.get(url).json()

cve = data["vulnerabilities"][0]["cve"]

print("ID:", cve["id"])
print("Published:", cve["published"])
print("Description:", cve["descriptions"][0]["value"])

print(cve["metrics"].keys())

metric = cve["metrics"]["cvssMetricV31"][0]

print(metric.keys())

print(metric["cvssData"].keys())

cvss = metric["cvssData"]

normalized = {
    "id": cve["id"],
    "published": cve["published"],
    "description": cve["descriptions"][0]["value"],
    "severity": metric["cvssData"]["baseSeverity"],
    "score": metric["cvssData"]["baseScore"]
}

print(normalized)
