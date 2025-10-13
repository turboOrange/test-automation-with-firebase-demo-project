from getgauge.python import step
import requests

FIRESTORE_URL = (
    "http://localhost:8080/v1/projects/demo-project/databases/(default)/documents/items"
)


@step("Add an item through the REST API")
def add_item_via_api():
    payload = {"fields": {"name": {"stringValue": "API Test Item"}}}
    r = requests.post(FIRESTORE_URL, json=payload)
    assert r.status_code == 200


@step("Verify the item appears when fetched via API")
def verify_item_via_api():
    r = requests.get(FIRESTORE_URL)
    assert any("API Test Item" in str(doc) for doc in r.json().get("documents", []))
