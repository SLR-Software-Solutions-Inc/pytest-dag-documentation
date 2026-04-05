"""Trigger a Read the Docs build via webhook with HMAC-SHA256 signing."""
import hashlib
import hmac
import os
import urllib.request

url = os.environ["READTHEDOCS_WEBHOOK_URL"]
secret = os.environ.get("READTHEDOCS_WEBHOOK_SECRET", "").strip()
payload = b"{}"

headers = {"Content-Type": "application/json"}
if secret:
    sig = hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()
    headers["X-Hub-Signature-256"] = f"sha256={sig}"

req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
with urllib.request.urlopen(req, timeout=30) as r:
    print("Read the Docs trigger status:", r.status)
