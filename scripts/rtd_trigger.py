"""Trigger a Read the Docs build via Generic API webhook."""
import os
import urllib.parse
import urllib.request

url = os.environ["READTHEDOCS_WEBHOOK_URL"]
token = os.environ.get("READTHEDOCS_WEBHOOK_SECRET", "").strip()

body = urllib.parse.urlencode({"token": token}).encode()
req = urllib.request.Request(
    url,
    data=body,
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=30) as r:
    print("Read the Docs trigger status:", r.status, r.read().decode())
